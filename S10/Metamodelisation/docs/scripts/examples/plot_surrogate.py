r"""
# Create a surrogate model

In this example,
we will build a surrogate model of the Rosenbrock function
and a constraint related to an Rosenbrock-based optimization problem.
"""
from numpy import array

from gemseo import from_pickle
from gemseo import sample_disciplines
from gemseo import to_pickle
from gemseo.algos.design_space import DesignSpace
from gemseo.disciplines.analytic import AnalyticDiscipline
from gemseo.disciplines.surrogate import SurrogateDiscipline

# %%
# Firstly,
# we define the discipline computing the Rosenbrock function
# and the Euclidean distance to the optimum:
discipline = AnalyticDiscipline(
    {"z": "(1-x)**2+100*(y-x**2)**2", "c": "((x-1)**2+(y-1)**2)**0.5"},
    name="Rosenbrock",
)

# %%
# Then, we create the design space:
design_space = DesignSpace()
design_space.add_variable("x", lower_bound=-2.0, upper_bound=2.0, value=0.0)
design_space.add_variable("y", lower_bound=-2.0, upper_bound=2.0, value=0.0)

# %%
# Then,
# we sample the discipline with an optimal LHS:
training_dataset = sample_disciplines([discipline], design_space, ["z", "c"], algo_name="OT_OPT_LHS", n_samples=30)

# %%
# and create a test dataset for validation, using a full-factorial design of experiments:
test_dataset = sample_disciplines([discipline], design_space, ["z", "c"], algo_name="OT_FULLFACT", n_samples=30**2)

# %%
# before creating a surrogate discipline:
surrogate_discipline = SurrogateDiscipline("RBFRegressor", training_dataset)

# %%
# and using it for prediction:
surrogate_discipline.execute({"x": array([1.0])})

# %%
# !!! note
#     When the first argument of the function ``sample_disciplines`` is a collection of disciplines,
#     the function uses the MDF formulation for handling the multidisciplinary couplings.
#     In other words,
#     a DOE algorithm is used to create $N$ input samples
#     and for each input sample,
#     the disciplines are evaluated and the coupling equations are solved.

# %%
# This surrogate discipline can be used in a scenario.
# The underlying regression model can also be assessed,
# with the R2 measure for instance:
r2 = surrogate_discipline.get_error_measure("R2Measure")
# %%
# either with respect to the training dataset
r2.compute_learning_measure(as_dict=True)
# %%
# by cross-validation
r2.compute_cross_validation_measure(as_dict=True)
# %%
# or with respect to the test dataset
r2.compute_test_measure(test_dataset, as_dict=True)

# %%
# or with the root mean squared error:
rmse = surrogate_discipline.get_error_measure("RMSEMeasure")
# %%
# either with respect to the training dataset
rmse.compute_learning_measure(as_dict=True)
# %%
# by cross-validation
rmse.compute_cross_validation_measure(as_dict=True)
# %%
# or with respect to the test dataset
rmse.compute_test_measure(test_dataset, as_dict=True)

# %%
# Lastly,
# you can save your surrogate discipline
to_pickle(surrogate_discipline, "my_surrogate.pkl")

# %%
# to use it later in another script:
surrogate_discipline = from_pickle("my_surrogate.pkl")
surrogate_discipline.execute({"x": array([1.0])})
