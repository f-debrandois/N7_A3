r"""
# Problem 2 - Surrogate modeling and uncertainty quantification

This code creates a surrogate model with respect to uncertain parameters and 
performs uncertainty propagation and sensitivity analysis for the OAD problem.
"""

import numpy as np
from lh2pac.utils import update_default_inputs
from gemseo import configure_logger, sample_disciplines, from_pickle, to_pickle
from gemseo.algos.design_space import DesignSpace
from gemseo.algos.parameter_space import ParameterSpace
from gemseo.disciplines.auto_py import AutoPyDiscipline
from gemseo.disciplines.surrogate import SurrogateDiscipline
from gemseo.uncertainty.statistics.empirical_statistics import EmpiricalStatistics
from gemseo.uncertainty.sensitivity.morris_analysis import MorrisAnalysis
from gemseo.uncertainty.sensitivity.sobol_analysis import SobolAnalysis
from gemseo_oad_training.unit import convert_from, convert_to
from gemseo_oad_training.models import (
    aerodynamic, approach, battery, climb, engine, fuel_tank,
    geometry, mass, mission, operating_cost, take_off, total_mass
)
import matplotlib.pyplot as plt

# %%
# Define the use cases
use_cases = {
    "UC1" : {"fuel_type": "kerosene", "engine_type": "turbofan", "design_range": 5500000},
    "UC2" : {"fuel_type": "liquid_h2", "engine_type": "turbofan", "design_range": 5500000}
}
case = "UC1"  # Select the use case to work with

# %%
# Define the design space for reference (default values)
class OADDesignSpace(DesignSpace):
    """Design space for the OAD problem with 4 design parameters."""
    
    def __init__(self):
        super().__init__(name="OAD_DesignSpace")
        
        # Design parameters from the problem description (default values)
        self.add_variable("slst", value=convert_from("kN", 150.))
        self.add_variable("n_pax", value=150.0)
        self.add_variable("area", value=180.0)
        self.add_variable("ar", value=9.0)
        
design_space = OADDesignSpace()
design_space

# %%
# Define the uncertain space based on the problem description
class OADUncertainSpace(ParameterSpace):
    """Uncertain space for the OAD problem with uncertain parameters."""
    
    def __init__(self, use_case="UC1"):
        super().__init__(name="OAD_UncertainSpace")
        self.use_case = use_case
        
        # Common uncertain parameters for all use cases
        # aef (aerodynamics efficiency factor): T(0.99, 1., 1.03)
        self.add_random_variable("aef", "OTTriangularDistribution", 
                                minimum=0.99, mode=1.0, maximum=1.03)
        
        # cef (??efficiency factor): T(0.99, 1., 1.03) 
        self.add_random_variable("cef", "OTTriangularDistribution",
                                minimum=0.99, mode=1.0, maximum=1.03)
        
        # sef (structure efficiency factor): T(0.99, 1., 1.03)
        self.add_random_variable("sef", "OTTriangularDistribution",
                                minimum=0.99, mode=1.0, maximum=1.03)
        
        # Use case specific uncertain parameters
        if use_case == "UC2":  # Liquid H2 case
            # gi: T(0.35, 0.4, 0.405) for liquid_h2
            self.add_random_variable("gi", "OTTriangularDistribution",
                                    minimum=0.35, mode=0.4, maximum=0.405)
            
            # vi: T(0.755, 0.800, 0.805) for liquid_h2
            self.add_random_variable("vi", "OTTriangularDistribution",
                                    minimum=0.755, mode=0.800, maximum=0.805)
            
            # fc_pwd: T(0.8, 1, 1.02) for liquid_h2 + electrofan
            self.add_random_variable("fc_pwd", "OTTriangularDistribution",
                                    minimum=0.8, mode=1.0, maximum=1.02)
        
        elif use_case == "UC4":  # Battery case
            # bed: U(400,700) for battery
            self.add_random_variable("bed", "OTUniformDistribution",
                                    minimum=400.0, maximum=700.0)


uncertain_space = OADUncertainSpace(use_case=case)
uncertain_space


# %%
# Create OAD disciplines
def create_oad_disciplines():
    """Create OAD disciplines."""
    disciplines = []
    
    model_functions = [
        aerodynamic,
        approach,
        battery,
        climb,
        engine,
        fuel_tank,
        geometry,
        mass,
        mission,
        operating_cost,
        take_off,
        total_mass
    ]
    
    for model_func in model_functions:
        try:
            discipline = AutoPyDiscipline(model_func)
            disciplines.append(discipline)
            print(f"Successfully created discipline for {model_func.__name__}")
        except Exception as e:
            print(f"Warning: Could not create discipline for {model_func.__name__}: {e}")
     
    return disciplines

disciplines = create_oad_disciplines()
update_default_inputs(disciplines, use_cases[case])


# %%
# Update disciplines with optimal design point from Problem 1
optimization_result = from_pickle("optimization_result.pkl")
optimal_design_point = {k: v[0] for k, v in optimization_result.x_opt_as_dict.items()}
update_default_inputs(disciplines, optimal_design_point)
print("Optimal design variables:")
for variables_name, value in optimal_design_point.items():
    print(f"  {variables_name}: {value:.3f}")


# %%
# Create a sample dataset from the OAD disciplines
def create_sample_dataset(disciplines, design_space, algo = "", n_samples=50):
    """
    Create a sample dataset from the OAD disciplines.
    
    Args:
        disciplines: List of GEMSEO disciplines
        design_space: Design space for sampling
        n_samples: Number of samples to generate
        
    Returns:
        Sample dataset
    """
    print(f"Sampling disciplines with {n_samples} samples...")
    
    # Define outputs of interest
    outputs_of_interest = ["mtom", "tofl", "vapp", "vz", "span", "fm"]
    
    # Sample the disciplines to create training data
    sample_dataset = sample_disciplines(
        disciplines=disciplines,
        input_space=design_space,
        output_names=outputs_of_interest,
        algo_name=algo,
        n_samples=n_samples
    )
    
    return sample_dataset

# We perform uncertainty propagation using Monte Carlo sampling.
sample_dataset = create_sample_dataset(disciplines, uncertain_space, algo="OT_MONTE_CARLO", n_samples=1000)


# %% 
# Create surrogate model
surrogate_discipline = SurrogateDiscipline("RBFRegressor", sample_dataset)

# Evaluate surrogate quality
print("\n=== UQ Surrogate Model Quality ===")
r2_measure = surrogate_discipline.get_error_measure("R2Measure")
print("R² scores:", r2_measure.compute_learning_measure(as_dict=True))


# %%
# Analyze uncertainty propagation results
def analyze_uncertainty_results(dataset, output_names=None):
    """
    Analyze uncertainty propagation results.
    
    Args:
        dataset: Monte Carlo dataset
        output_names: List of output names to analyze
    """
    if output_names is None:
        output_names = ["mtom", "tofl", "vapp", "vz", "span", "fm"]
    
    print("\n=== Uncertainty Propagation Results ===")
    
    # Create empirical statistics object
    statistics = EmpiricalStatistics(dataset)
    
    # Compute and display statistics for each output
    for output_name in output_names:
        if output_name in dataset.variable_names:
            print(f"\n{output_name.upper()}:")
            
            # Mean
            mean_val = statistics.compute_mean()[output_name][0]
            print(f"  Mean: {mean_val:.6f}")
            
            # Standard deviation
            std_val = np.sqrt(statistics.compute_variance()[output_name][0])
            print(f"  Std Dev: {std_val:.6f}")
            
            # Coefficient of variation
            cv = std_val / abs(mean_val) * 100 if abs(mean_val) > 1e-10 else 0
            print(f"  Coeff. of Variation: {cv:.2f}%")
            
            # Percentiles
            data = dataset.get_view(variable_names=output_name).to_numpy().flatten()
            p5, p95 = np.percentile(data, [5, 95])
            print(f"  5th percentile: {p5:.6f}")
            print(f"  95th percentile: {p95:.6f}")
            
analyze_uncertainty_results(sample_dataset)

# We can also plot the histogram of the three random variables:
fig, axes = plt.subplots(1, 3)
for ax, name in zip(axes, ["aef", "cef", "sef"]):
    ax.hist(sample_dataset.get_view(variable_names=name))
    ax.set_title(name)

# %%
# Perform sensitivity analysis
def perform_sensitivity_analysis(disciplines, uncertain_space, output_names=None):
    """
    Perform sensitivity analysis using Morris and Sobol methods.
    
    Args:
        disciplines: List of disciplines
        uncertain_space: Uncertain parameter space
        output_names: List of output names for sensitivity analysis
    """
    if output_names is None:
        output_names = ["mtom", "tofl", "vapp", "vz", "span", "fm"]
    
    print("\n=== Sensitivity Analysis ===")
    
    # Morris Analysis (screening method)
    print("\nPerforming Morris sensitivity analysis...")
    try:
        morris = MorrisAnalysis()
        morris.compute_samples(disciplines, uncertain_space, n_samples=1000)
        morris.compute_indices(output_names)
        
        print("Morris sensitivity indices:")
        for output_name in output_names:
            if output_name in morris.indices.mu_star:
                print(f"\n{output_name.upper()}:")
                print("  Mu* indices:")
                for param_name, value in morris.indices.mu_star[output_name][0].items():
                    print(f"    {param_name}: {float(value):.6f}")
                print("  Sigma indices:")
                for param_name, value in morris.indices.sigma[output_name][0].items():
                    print(f"    {param_name}: {float(value):.6f}")
    
    except Exception as e:
        print(f"Morris analysis failed: {e}")
    
    # Sobol Analysis (variance-based method)
    print("\nPerforming Sobol sensitivity analysis...")
    try:
        sobol = SobolAnalysis()
        sobol.compute_samples(disciplines, uncertain_space, n_samples=10000)
        sobol.compute_indices(output_names)
        
        print("Sobol sensitivity indices:")
        for output_name in output_names:
            if output_name in sobol.indices.first:
                print(f"\n{output_name.upper()}:")
                # sobol.indices.first[output_name] is a list of dicts with arrays as values
                first_indices_dict = sobol.indices.first[output_name][0]
                total_indices_dict = sobol.indices.total[output_name][0]

            print("  First-order indices:")
            for param_name, value in first_indices_dict.items():
                print(f"    {param_name}: {float(value):.6f}")

            print("  Total indices:")
            for param_name, value in total_indices_dict.items():
                print(f"    {param_name}: {float(value):.6f}")
        
    except Exception as e:
        print(f"Sobol analysis failed: {e}")

perform_sensitivity_analysis([surrogate_discipline], uncertain_space)

# %%
# Plot uncertainty results
def plot_uncertainty_results(mc_dataset, uncertain_space, output_names=None):
    """
    Plot uncertainty propagation results.
    
    Args:
        mc_dataset: Monte Carlo dataset
        uncertain_space: Uncertain parameter space
        output_names: List of output names to plot
    """
    if output_names is None:
        output_names = ["mtom", "tofl", "vapp", "vz", "span", "fm"]
    
    # Plot histograms of outputs
    n_outputs = len(output_names)
    fig, axes = plt.subplots(1, n_outputs, figsize=(4*n_outputs, 4))
    
    if n_outputs == 1:
        axes = [axes]
    
    for i, output_name in enumerate(output_names):
        if output_name in mc_dataset.variable_names:
            data = mc_dataset.get_view(variable_names=output_name).to_numpy().flatten()
            axes[i].hist(data, bins=30, alpha=0.7, edgecolor='black')
            axes[i].set_title(f'{output_name.upper()} Distribution')
            axes[i].set_xlabel(output_name)
            axes[i].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()
    
    # Plot correlation matrix if multiple uncertain parameters
    uncertain_params = list(uncertain_space.variable_names)
    if len(uncertain_params) > 1:
        # Create input-output correlation plots
        fig, axes = plt.subplots(len(uncertain_params), len(output_names), 
                                figsize=(4*len(output_names), 3*len(uncertain_params)))
        
        if len(uncertain_params) == 1:
            axes = axes.reshape(1, -1)
        if len(output_names) == 1:
            axes = axes.reshape(-1, 1)
        
        for i, param_name in enumerate(uncertain_params):
            for j, output_name in enumerate(output_names):
                if param_name in mc_dataset.variable_names and output_name in mc_dataset.variable_names:
                    x_data = mc_dataset.get_view(variable_names=param_name).to_numpy().flatten()
                    y_data = mc_dataset.get_view(variable_names=output_name).to_numpy().flatten()
                    
                    axes[i, j].scatter(x_data, y_data, alpha=0.5, s=1)
                    axes[i, j].set_xlabel(param_name)
                    axes[i, j].set_ylabel(output_name)
                    axes[i, j].set_title(f'{param_name} vs {output_name}')
        
        plt.tight_layout()
        plt.show()
        
plot_uncertainty_results(sample_dataset, uncertain_space)
