"""
# Use a design of experiments

The `DOEScenario` defines an evaluation problem
from one or more disciplines,
a design space
and a DOE (design of experiments) algorithm.

In this example,
we want to sample the
[Rosenbrock function](https://en.wikipedia.org/wiki/Rosenbrock_function)
$f(x,y)=(1-x)^2+100*(y-x^2)^2$
over the design space $[-2,2]^2$
with a latin hypercube sampling (LHS) algorithm
improved by simulated annealing.
"""
from gemseo import configure_logger
from gemseo.algos.design_space import DesignSpace
from gemseo.disciplines.analytic import AnalyticDiscipline
from gemseo.scenarios.doe_scenario import DOEScenario

# %%
# First,
# we activate the logger.
configure_logger()

# %%
# Then,
# we create a discipline to evaluate $(1-x)^2+100*(y-x^2)^2$:
discipline = AnalyticDiscipline(
    {"z": "(1-x)**2+100*(y-x**2)**2"},
    name="Rosenbrock",
)
# %%
# !!! note
#
#     The `AnalyticDiscipline` allows us to define functions from strings
#     and automatically get the expression of the derivatives,
#     based on [sympy](https://www.sympy.org/fr/),
#     a Python library for symbolic mathematics.
#
# Then,
# we create the design space $[-2,2]^2$:
design_space = DesignSpace()
design_space.add_variable("x", lower_bound=-2, upper_bound=2)
design_space.add_variable("y", lower_bound=-2, upper_bound=2)

# %%
# Thirdly,
# we create a `DOEScenario` from this discipline and this design space:
disciplines = [discipline]
scenario = DOEScenario(disciplines, "z", design_space, formulation_name="DisciplinaryOpt")
# %%
# !!! note
#
#     `"DisciplinaryOpt"` means that we evaluate the `disciplines` sequentially;
#     then,
#     if the output of a discipline is the input of one of the following,
#     its value will be used
#     (in this case,
#     there is only one discipline but the argument is mandatory).
#
# !!! note
#
#     In the case where there is more than one output of interest,
#     you can use the method `add_observable`
#     to store the evaluations of the other outputs of interest:
#
#     ```python
#        scenario = create_scenario(
#            disciplines, "DisciplinaryOpt", "foo", design_space, scenario_type="DOE"
#        )
#        scenario.add_observable("bar")
#        scenario.add_observable("baz")
#     ```
#
# Now,
# we can sample the discipline to get 100 evaluations of the triple $(x,y,z)$:
scenario.execute(algo_name="OT_OPT_LHS", n_samples=100)

# %%
#
# !!! note
#
#     `DOEScenario` is mainly used to solve an optimization problem
#     with a DOE algorithm instead of an optimization algorithm.
#     This is the reason why
#     the log presents an optimization problem and optimization result.
#
# Lastly,
# we can export the result to an `IODataset`
# which is a subclass of `Dataset`,
# which is a subclass of `pandas.DataFrame`:
dataset = scenario.to_dataset(opt_naming=False)
dataset

# %%
# !!! seealso
#
#     - [Dataset examples](https://gemseo.readthedocs.io/en/stable/examples/dataset/index.html)
#     - [DOE examples](https://gemseo.readthedocs.io/en/stable/examples/doe/index.html)
