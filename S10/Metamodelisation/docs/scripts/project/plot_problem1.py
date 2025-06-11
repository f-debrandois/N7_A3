r"""
# Problem 1 - Surrogate modeling

This code creates a surrogate model of the OAD problem and uses it for optimization
to minimize the maximum take-off mass (MTOM) under operational constraints.
"""

import numpy as np
from lh2pac.utils import update_default_inputs
from gemseo import configure_logger, sample_disciplines, generate_coupling_graph, to_pickle, from_pickle
from gemseo.algos.design_space import DesignSpace
from gemseo.disciplines.auto_py import AutoPyDiscipline
from gemseo.disciplines.surrogate import SurrogateDiscipline
from gemseo.scenarios.mdo_scenario import MDOScenario
from gemseo_oad_training.unit import convert_from, convert_to
from gemseo.utils.discipline import get_all_inputs
from gemseo_oad_training.models import (
    aerodynamic, approach, battery, climb, engine, fuel_tank,
    geometry, mass, mission, operating_cost, take_off, total_mass
)

# %%
# Define the use cases
use_cases = {
    "UC1" : {"fuel_type": "kerosene", "engine_type": "turbofan", "design_range": 5500000},
    "UC2" : {"fuel_type": "liquid_h2", "engine_type": "turbofan", "design_range": 5500000}
}
case = "UC1"  # Select the use case to work with


# %% 
# Define the design space for the OAD problem
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
design_space

# %% 
# Create OAD disciplines
def create_oad_disciplines():
    """
    Create OAD disciplines for a specific use case.
        
    Returns:
        List of GEMSEO disciplines
    """
    disciplines = []
    
    # Create disciplines from the OAD models
    # Each model is wrapped as an AutoPyDiscipline
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

# Generate coupling graph
generate_coupling_graph(disciplines, file_path="")


# %%
# Display all input variables
get_all_inputs(disciplines)

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
    outputs_of_interest = ["mtom", "tofl", "vapp", "vz", "span", "length", "fm"]
    
    # Sample the disciplines to create training data
    sample_dataset = sample_disciplines(
        disciplines=disciplines,
        input_space=design_space,
        output_names=outputs_of_interest,
        algo_name=algo,
        n_samples=n_samples
    )
    
    return sample_dataset

# Sample datasets for training and testing
train_dataset = create_sample_dataset(disciplines, design_space, "OT_OPT_LHS", n_samples=50)
test_dataset = create_sample_dataset(disciplines, design_space, "OT_FULLFACT", n_samples=30**2)

# %% 
# Create surrogate model
surrogate_discipline = SurrogateDiscipline("RBFRegressor", train_dataset)

# %%
# Evaluate surrogate quality
def evaluate_surrogate_quality(surrogate_discipline, test_dataset=None):
    """
    Evaluate the quality of the surrogate model.
    
    Args:
        surrogate_discipline: Trained surrogate model
        test_dataset: Optional test dataset for validation
    """
    print("\n=== Surrogate Model Quality Assessment ===")
    
    # R² measure
    r2_measure = surrogate_discipline.get_error_measure("R2Measure")
    
    print("R² scores:")
    print("- Learning (training):", r2_measure.compute_learning_measure(as_dict=True))
    print("- Cross-validation:", r2_measure.compute_cross_validation_measure(as_dict=True))
    
    if test_dataset is not None:
        print("- Test dataset:", r2_measure.compute_test_measure(test_dataset, as_dict=True))
    
    # RMSE measure
    rmse_measure = surrogate_discipline.get_error_measure("RMSEMeasure")
    
    print("\nRMSE scores:")
    print("- Learning (training):", rmse_measure.compute_learning_measure(as_dict=True))
    print("- Cross-validation:", rmse_measure.compute_cross_validation_measure(as_dict=True))
    
    if test_dataset is not None:
        print("- Test dataset:", rmse_measure.compute_test_measure(test_dataset, as_dict=True))

evaluate_surrogate_quality(surrogate_discipline, test_dataset)

# %%
# Solve the optimization problem using the surrogate model
def solve_optimization_problem(discipline, design_space, algo_name="NLOPT_COBYLA", max_iter=100, sample=None):
    """
    Solve the optimization problem using the surrogate model.
    
    Args:
        discipline: Discipline
        design_space: Design space for optimization
        
    Returns:
        Optimization scenario with results
    """
    print("Setting up optimization problem...")
    
    # Create MDO scenario with the surrogate discipline
    scenario = MDOScenario(
        disciplines=discipline,
        objective_name="mtom",  # Minimize maximum take-off mass
        design_space=design_space,
        formulation_name="DisciplinaryOpt"
    )
    
    # Add operational constraints
    # Take-off field length (tofl ≤ 1900 m)
    scenario.add_constraint("tofl", constraint_type="ineq", positive=False, value=1900.0)
    
    # Approach speed (vapp ≤ 135 kt)
    scenario.add_constraint("vapp", constraint_type="ineq", positive=False, value=convert_from("kt", 135.))
    
    # Vertical speed (300 ft/min ≤ vz) - converted to inequality constraint
    scenario.add_constraint("vz", constraint_type="ineq", positive=True, value=convert_from("ft/min", 300.))
    
    # Wing span (span ≤ 40 m)
    scenario.add_constraint("span", constraint_type="ineq", positive=False, value=40.0)
    
    # Wing length (length ≤ 45 m)
    scenario.add_constraint("length", constraint_type="ineq", positive=False, value=45.0)
    
    # Fuel margin (0% ≤ fm) - converted to inequality constraint
    scenario.add_constraint("fm", constraint_type="ineq", positive=True, value=0.0)
    
    return scenario

configure_logger()
surrogate_scenario = solve_optimization_problem([surrogate_discipline], design_space)
surrogate_scenario.execute(algo_name="NLOPT_COBYLA", max_iter=100)


# %%
# Display optimization results
print("\n=== Optimization Results ===")
    
# Post-process to visualize optimization history
surrogate_scenario.post_process(post_name="OptHistoryView", save=False, show=True)

# Get optimization result
opt_result = surrogate_scenario.optimization_result

print("Optimal design variables:")
var_names = list(design_space.variable_names)
x_opt = opt_result.x_opt

for i, var_name in enumerate(var_names):
    if i < len(x_opt):
        print(f"  {var_name}: {x_opt[i]:.3f}")

print(f"\nOptimal objective (MTOM): {opt_result.f_opt:.3f}")

print("\nConstraint values at optimum:")
if opt_result.constraint_values is not None:
    for constraint_name, value in opt_result.constraint_values.items():
        print(f"  {constraint_name}: {value:.3f}")

print(f"\nOptimization status: {opt_result.is_feasible}")


# %%
# Save the optimization result to a file
to_pickle(surrogate_scenario.optimization_result, "optimization_result.pkl")


# %%
# Scenario
optimal_results = np.array([opt_result.x_opt])
scenario = solve_optimization_problem(disciplines, design_space, algo_name="CustomDOE", sample=optimal_results)
scenario.execute(algo_name="CustomDOE", samples=optimal_results)


# %%
# Display optimization results
print("\n=== Optimization Results ===")


# Get optimization result
opt_result = scenario.optimization_result

print("Optimal design variables:")
var_names = list(design_space.variable_names)
x_opt = opt_result.x_opt
for i, var_name in enumerate(var_names):
    if i < len(x_opt):
        print(f"  {var_name}: {x_opt[i]:.3f}")
        
print(f"\nOptimal objective (MTOM): {opt_result.f_opt:.3f}")

print("\nConstraint values at optimum:")
if opt_result.constraint_values is not None:
    for constraint_name, value in opt_result.constraint_values.items():
        print(f"  {constraint_name}: {value:.3f}")
        
print(f"\nOptimization status: {opt_result.is_feasible}")
