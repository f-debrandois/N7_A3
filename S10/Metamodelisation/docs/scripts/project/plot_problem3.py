r"""
# Problem 3 - Surrogate modeling and robust optimization

This code creates a surrogate model with respect to both design parameters (x) 
and uncertain parameters (u), then performs robust optimization to find the best 
aircraft concept taking into account the uncertainty of technological choices.
"""

import numpy as np
from lh2pac.utils import update_default_inputs
from gemseo import configure_logger, sample_disciplines, from_pickle, to_pickle
from gemseo.algos.design_space import DesignSpace
from gemseo.algos.parameter_space import ParameterSpace
from gemseo.disciplines.auto_py import AutoPyDiscipline
from gemseo.disciplines.surrogate import SurrogateDiscipline
from gemseo.scenarios.mdo_scenario import MDOScenario
from gemseo.uncertainty.statistics.empirical_statistics import EmpiricalStatistics
from gemseo_umdo.scenarios.umdo_scenario import UMDOScenario
from gemseo_oad_training.unit import convert_from, convert_to
from gemseo_oad_training.models import (
    aerodynamic, approach, battery, climb, engine, fuel_tank,
    geometry, mass, mission, operating_cost, take_off, total_mass
)
import matplotlib.pyplot as plt


# %%
# Define the use cases
use_cases = {
    "UC1": {"fuel_type": "kerosene", "engine_type": "turbofan", "design_range": 5500000},
    "UC2": {"fuel_type": "liquid_h2", "engine_type": "turbofan", "design_range": 5500000}
}
case = "UC1"  # Select the use case to work with

# %%
# Define the design space (design parameters x)
class OADDesignSpace(DesignSpace):
    """Design space for the OAD problem with 4 design parameters."""
    
    def __init__(self):
        super().__init__(name="OAD_DesignSpace")
        
        # Design parameters from the problem description
        # Maximum sea level static thrust (100 kN ≤ slst ≤ 200 kN, default: 150 kN)
        self.add_variable("slst", lower_bound=convert_from("kN", 100.), 
                         upper_bound=convert_from("kN", 200.), 
                         value=convert_from("kN", 150.))
        
        # Number of passengers (120 ≤ n_pax ≤ 180, default: 150)
        self.add_variable("n_pax", lower_bound=120.0, upper_bound=180.0, value=150.0)
        
        # Wing area (100 m² ≤ area ≤ 200 m², default: 180 m²)
        self.add_variable("area", lower_bound=100.0, upper_bound=200.0, value=180.0)
        
        # Wing aspect ratio (5 ≤ ar ≤ 20, default: 9.)
        self.add_variable("ar", lower_bound=5.0, upper_bound=20.0, value=9.0)

design_space = OADDesignSpace()


# %%
# Define the uncertain space (uncertain parameters u)
class OADUncertainSpace(ParameterSpace):
    """Uncertain space for the OAD problem with uncertain parameters."""
    
    def __init__(self, use_case="UC1"):
        super().__init__(name="OAD_UncertainSpace")
        self.use_case = use_case
        
        # Common uncertain parameters for all use cases
        # aef (aerodynamics efficiency factor): T(0.99, 1., 1.03)
        self.add_random_variable("aef", "OTTriangularDistribution", 
                                minimum=0.99, mode=1.0, maximum=1.03)
        
        # cef (combustion efficiency factor): T(0.99, 1., 1.03) 
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

# Update default inputs for the disciplines based on the use case
update_default_inputs(disciplines, use_cases[case])


# %%
# Create combined parameter space (design + uncertain parameters)
def create_combined_parameter_space(design_space, uncertain_space):
    """
    Create a combined parameter space with both design and uncertain parameters.
    
    Args:
        design_space: Design space with design parameters
        uncertain_space: Parameter space with uncertain parameters
        
    Returns:
        Combined parameter space
    """
    combined_space = ParameterSpace(name="Combined_DesignUncertain_Space")
    
    # Add design variables (deterministic)
    print(design_space.variable_names)
    print("Design space attributes:")
    for attr in dir(design_space):
        if not attr.startswith("_"):
            print(f"  {attr}: {getattr(design_space, attr)}")
    for var_name in design_space.variable_names:
        var_info = design_space.variables[var_name]
        combined_space.add_variable(
            var_name,
            size=var_info.size,
            lower_bound=var_info.lower_bound,
            upper_bound=var_info.upper_bound,
            value=var_info.value
        )
    
    # Add uncertain variables (random)
    for var_name in uncertain_space.variable_names:
        var_info = uncertain_space.get_variable(var_name)
        # Copy the random variable
        distribution = uncertain_space.distributions[var_name]
        combined_space.add_random_variable(
            var_name,
            distribution.distribution_name, 
            **distribution.parameters
        )
    
    return combined_space

# %%
# Create surrogate model for robust optimization
def create_robust_surrogate_model(disciplines, combined_space, n_samples=100):
    """
    Create a surrogate model for both design and uncertain parameters.
    
    Args:
        disciplines: List of GEMSEO disciplines
        combined_space: Combined parameter space (design + uncertain)
        n_samples: Number of samples for training
        
    Returns:
        SurrogateDiscipline object and training dataset
    """
    print(f"Sampling disciplines with {n_samples} samples for robust optimization...")
    
    # Define outputs of interest
    outputs_of_interest = ["mtom", "tofl", "vapp", "vz", "span", "length", "fm"]
    
    # Sample the disciplines to create training data
    training_dataset = sample_disciplines(
        disciplines=disciplines,
        input_space=combined_space,
        output_names=outputs_of_interest,
        algo_name="OT_OPT_LHS",  # Optimal Latin Hypercube Sampling
        n_samples=n_samples
    )
    
    print("Creating robust surrogate model...")
    
    # Create surrogate discipline using RBF (Radial Basis Functions)
    surrogate_discipline = SurrogateDiscipline(
        "RBFRegressor", 
        training_dataset,
        name="OAD_Robust_Surrogate"
    )
    
    return surrogate_discipline, training_dataset

# %%
# Robust optimization formulations
class RobustObjective:
    """Define robust objective functions."""
    
    @staticmethod
    def mean_objective(disciplines, uncertain_space, design_vars, n_mc_samples=100):
        """
        Compute mean of objective function over uncertainty.
        
        Args:
            disciplines: List of disciplines
            uncertain_space: Uncertain parameter space
            design_vars: Current design variables
            n_mc_samples: Number of Monte Carlo samples
            
        Returns:
            Mean objective value
        """
        # Sample uncertain parameters
        samples = uncertain_space.sample(n_mc_samples)
        objective_values = []
        
        for i in range(n_mc_samples):
            # Set uncertain parameters
            uncertain_inputs = {name: samples[name][i] for name in uncertain_space.variable_names}
            # Combine with design variables
            inputs = {**design_vars, **uncertain_inputs}
            
            # Evaluate disciplines
            for discipline in disciplines:
                discipline.execute(inputs)
            
            # Get objective value (MTOM)
            objective_values.append(inputs.get("mtom", 0.0))
        
        return np.mean(objective_values)
    
    @staticmethod
    def robust_objective(mean_obj, std_obj, robustness_factor=1.0):
        """
        Compute robust objective: mean + robustness_factor * std.
        
        Args:
            mean_obj: Mean objective value
            std_obj: Standard deviation of objective
            robustness_factor: Weight for robustness (higher = more robust)
            
        Returns:
            Robust objective value
        """
        return mean_obj + robustness_factor * std_obj

# %%
# Solve robust optimization problem using UMDO
def solve_robust_optimization_umdo(disciplines, design_space, uncertain_space, 
                                   statistic="Mean", robustness_factor=1.0):
    """
    Solve robust optimization using GEMSEO-UMDO.
    
    Args:
        disciplines: List of disciplines
        design_space: Design space
        uncertain_space: Uncertain parameter space
        statistic: Statistic for robust optimization ("Mean", "Margin", etc.)
        robustness_factor: Robustness factor for margin-based approaches
        
    Returns:
        UMDO scenario with results
    """
    print(f"Setting up UMDO scenario with {statistic} statistic...")
    
    try:
        # Create UMDO scenario
        scenario = UMDOScenario(
            disciplines=disciplines,
            formulation_name="DisciplinaryOpt",
            objective_name="mtom",
            design_space=design_space,
            uncertain_space=uncertain_space,
            objective_statistic_name=statistic,
            objective_statistic_parameters={"factor": robustness_factor} if statistic == "Margin" else {}
        )
        
        # Add robust constraints
        constraint_names = ["tofl", "vapp", "vz", "span", "length", "fm"]
        constraint_types = ["ineq", "ineq", "ineq", "ineq", "ineq", "ineq"]
        constraint_positive = [False, False, True, False, False, True]
        constraint_values = [1900.0, 135.0, 300.0, 40.0, 45.0, 0.0]
        
        for name, ctype, positive, value in zip(constraint_names, constraint_types, 
                                               constraint_positive, constraint_values):
            scenario.add_constraint(
                name,
                constraint_type=ctype,
                positive=positive,
                value=value,
                constraint_statistic_name=statistic,
                constraint_statistic_parameters={"factor": robustness_factor} if statistic == "Margin" else {}
            )
        
        print("Executing UMDO optimization...")
        
        # Execute robust optimization
        scenario.execute(
            algo_name="NLOPT_COBYLA",
            max_iter=50,  # Reduced for computational efficiency
            u_samples=100  # Number of uncertainty samples per design evaluation
        )
        
        return scenario
        
    except Exception as e:
        print(f"UMDO optimization failed: {e}")
        return None

# %%
# Alternative robust optimization using surrogate model
def solve_robust_optimization_surrogate(surrogate_discipline, design_space, uncertain_space,
                                       robustness_approach="mean_plus_std"):
    """
    Solve robust optimization using surrogate model and Monte Carlo evaluation.
    
    Args:
        surrogate_discipline: Trained surrogate model
        design_space: Design space
        uncertain_space: Uncertain parameter space
        robustness_approach: Approach for robustness ("mean", "mean_plus_std", "quantile")
        
    Returns:
        Optimization results
    """
    print(f"Solving robust optimization with surrogate model using {robustness_approach} approach...")
    
    class RobustSurrogateDiscipline(AutoPyDiscipline):
        """Wrapper discipline for robust evaluation using surrogate."""
        
        def __init__(self, surrogate, uncertain_space, approach="mean_plus_std", n_mc=100):
            self.surrogate = surrogate
            self.uncertain_space = uncertain_space
            self.approach = approach
            self.n_mc = n_mc
            
            # Define the robust evaluation function
            def robust_evaluate(**design_vars):
                """Evaluate robust objective and constraints."""
                
                # Sample uncertain parameters
                uncertain_samples = uncertain_space.sample(self.n_mc)
                
                # Evaluate surrogate for all uncertainty samples
                results = {"mtom": [], "tofl": [], "vapp": [], "vz": [], 
                          "span": [], "length": [], "fm": []}
                
                for i in range(self.n_mc):
                    # Combine design and uncertain parameters
                    inputs = design_vars.copy()
                    for param_name in uncertain_space.variable_names:
                        inputs[param_name] = uncertain_samples[param_name][i]
                    
                    # Evaluate surrogate
                    outputs = surrogate.execute(inputs)
                    
                    # Store results
                    for output_name in results.keys():
                        if output_name in outputs:
                            results[output_name].append(outputs[output_name])
                
                # Compute robust statistics
                robust_outputs = {}
                
                for output_name, values in results.items():
                    values = np.array(values).flatten()
                    
                    if approach == "mean":
                        robust_outputs[output_name] = np.mean(values)
                    elif approach == "mean_plus_std":
                        robust_outputs[output_name] = np.mean(values) + np.std(values)
                    elif approach == "quantile":
                        robust_outputs[output_name] = np.percentile(values, 95)  # 95th percentile
                    else:
                        robust_outputs[output_name] = np.mean(values)
                
                return robust_outputs
            
            # Initialize AutoPyDiscipline
            super().__init__(robust_evaluate, name="RobustSurrogate")
    
    # Create robust surrogate discipline
    robust_discipline = RobustSurrogateDiscipline(
        surrogate_discipline, uncertain_space, robustness_approach
    )
    
    # Create MDO scenario
    scenario = MDOScenario(
        disciplines=[robust_discipline],
        objective_name="mtom",
        design_space=design_space,
        formulation_name="DisciplinaryOpt"
    )
    
    # Add robust constraints
    scenario.add_constraint("tofl", constraint_type="ineq", positive=False, value=1900.0)
    scenario.add_constraint("vapp", constraint_type="ineq", positive=False, value=135.0)
    scenario.add_constraint("vz", constraint_type="ineq", positive=True, value=300.0)
    scenario.add_constraint("span", constraint_type="ineq", positive=False, value=40.0)
    scenario.add_constraint("length", constraint_type="ineq", positive=False, value=45.0)
    scenario.add_constraint("fm", constraint_type="ineq", positive=True, value=0.0)
    
    print("Executing robust optimization...")
    
    # Execute optimization
    scenario.execute(
        algo_name="NLOPT_COBYLA",
        max_iter=50
    )
    
    return scenario

# %%
# Analyze robust optimization results
def analyze_robust_results(scenario, disciplines, uncertain_space, n_validation=1000):
    """
    Analyze robust optimization results.
    
    Args:
        scenario: Optimization scenario with results
        disciplines: Original disciplines for validation
        uncertain_space: Uncertain parameter space
        n_validation: Number of validation samples
    """
    print("\n=== Robust Optimization Results ===")
    
    # Get optimal design
    optimal_design = scenario.get_optimum().x_opt
    
    print("Optimal robust design variables:")
    for var_name, var_value in optimal_design.items():
        print(f"  {var_name}: {var_value:.6f}")
    
    print(f"\nOptimal robust objective: {scenario.get_optimum().f_opt:.6f}")
    
    # Validate robustness with Monte Carlo simulation
    print(f"\nValidating robustness with {n_validation} Monte Carlo samples...")
    
    # Sample uncertain parameters
    validation_samples = uncertain_space.sample(n_validation)
    
    # Evaluate at optimal design with uncertainty
    objective_values = []
    constraint_values = {name: [] for name in ["tofl", "vapp", "vz", "span", "length", "fm"]}
    
    for i in range(n_validation):
        # Combine optimal design with uncertain sample
        inputs = optimal_design.copy()
        for param_name in uncertain_space.variable_names:
            inputs[param_name] = validation_samples[param_name][i]
        
        # Evaluate disciplines (or surrogate)
        try:
            if len(disciplines) == 1 and hasattr(disciplines[0], 'execute'):
                # Single surrogate discipline
                outputs = disciplines[0].execute(inputs)
            else:
                # Multiple disciplines
                for discipline in disciplines:
                    outputs = discipline.execute(inputs)
                    inputs.update(outputs)
                outputs = inputs
            
            # Store objective
            if "mtom" in outputs:
                objective_values.append(outputs["mtom"])
            
            # Store constraints
            for constraint_name in constraint_values.keys():
                if constraint_name in outputs:
                    constraint_values[constraint_name].append(outputs[constraint_name])
                    
        except Exception as e:
            print(f"Evaluation failed for sample {i}: {e}")
    
    # Analyze validation results
    if objective_values:
        obj_array = np.array(objective_values).flatten()
        print(f"\nObjective (MTOM) validation statistics:")
        print(f"  Mean: {np.mean(obj_array):.6f}")
        print(f"  Std Dev: {np.std(obj_array):.6f}")
        print(f"  5th percentile: {np.percentile(obj_array, 5):.6f}")
        print(f"  95th percentile: {np.percentile(obj_array, 95):.6f}")
    
    # Analyze constraint robustness
    print(f"\nConstraint violation analysis:")
    constraint_limits = {"tofl": 1900.0, "vapp": 135.0, "vz": 300.0, 
                        "span": 40.0, "length": 45.0, "fm": 0.0}
    constraint_directions = {"tofl": "<=", "vapp": "<=", "vz": ">=", 
                           "span": "<=", "length": "<=", "fm": ">="}
    
    for constraint_name, values in constraint_values.items():
        if values:
            values_array = np.array(values).flatten()
            limit = constraint_limits[constraint_name]
            direction = constraint_directions[constraint_name]
            
            if direction == "<=":
                violations = np.sum(values_array > limit)
            else:  # ">="
                violations = np.sum(values_array < limit)
            
            violation_rate = violations / len(values_array) * 100
            
            print(f"  {constraint_name}: {violation_rate:.1f}% violations "
                  f"(mean: {np.mean(values_array):.3f}, limit: {direction} {limit})")

# %%
# Main function for Problem 3
def main():
    """Main function to solve Problem 3 for both use cases."""
    
    results = {}
    
    # Process both use cases
    for case in ["UC1", "UC2"]:
        print(f"\n{'='*60}")
        print(f"Processing Problem 3 for {case}")
        print(f"{'='*60}")
        
        try:
            # Create spaces
            design_space = OADDesignSpace()
            uncertain_space = OADUncertainSpace(use_case=case)
            combined_space = create_combined_parameter_space(design_space, uncertain_space)
            
            print(f"Design space: {len(design_space.variable_names)} variables")
            print(f"Uncertain space: {len(uncertain_space.variable_names)} variables")
            print(f"Combined space: {len(combined_space.variable_names)} variables")
            
            # Create disciplines
            disciplines = create_oad_disciplines()
            update_default_inputs(disciplines, use_cases[case])
            
            print(f"Created {len(disciplines)} disciplines")
            
            # Create robust surrogate model
            surrogate_discipline, training_dataset = create_robust_surrogate_model(
                disciplines, combined_space, n_samples=150
            )
            
            # Evaluate surrogate quality
            print("\n=== Robust Surrogate Model Quality ===")
            r2_measure = surrogate_discipline.get_error_measure("R2Measure")
            r2_scores = r2_measure.compute_learning_measure(as_dict=True)
            print("R² scores:", r2_scores)
            
            # Try UMDO approach first
            print("\n--- Attempting UMDO Approach ---")
            umdo_scenario = solve_robust_optimization_umdo(
                [surrogate_discipline], design_space, uncertain_space, 
                statistic="Mean"
            )
            
            if umdo_scenario is not None:
                analyze_robust_results(umdo_scenario, [surrogate_discipline], uncertain_space)
                results[f"{case}_umdo"] = umdo_scenario
            
            # Try surrogate-based approach
            print("\n--- Surrogate-based Robust Optimization ---")
            
            # Test different robustness approaches
            for approach in ["mean", "mean_plus_std", "quantile"]:
                print(f"\n... Testing {approach} approach ...")
                
                try:
                    surrogate_scenario = solve_robust_optimization_surrogate(
                        surrogate_discipline, design_space, uncertain_space, approach
                    )
                    
                    if surrogate_scenario is not None:
                        print(f"\n--- Results for {approach} approach ---")
                        analyze_robust_results(surrogate_scenario, [surrogate_discipline], uncertain_space, n_validation=500)
                        results[f"{case}_{approach}"] = surrogate_scenario
                        
                except Exception as e:
                    print(f"Surrogate approach {approach} failed: {e}")
            
            # Save results
            if results:
                to_pickle(results, f"robust_optimization_results_{case}.pkl")
                print(f"\nResults saved for {case}")
                
        except Exception as e:
            print(f"Error processing {case}: {e}")
            import traceback
            traceback.print_exc()
    
    # Compare approaches
    if results:
        print(f"\n{'='*60}")
        print("COMPARISON OF ROBUST OPTIMIZATION APPROACHES")
        print(f"{'='*60}")
        
        for result_name, scenario in results.items():
            print(f"\n{result_name.upper()}:")
            print(f"  Optimal objective: {scenario.get_optimum().f_opt:.6f}")
            print("  Optimal design:")
            for var_name, var_value in scenario.get_optimum().x_opt.items():
                print(f"    {var_name}: {var_value:.6f}")

if __name__ == "__main__":
    main()