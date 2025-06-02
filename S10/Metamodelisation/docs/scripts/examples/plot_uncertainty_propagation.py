r"""
# Propagate uncertainties

In this example,
we will propagate uncertainties through a discipline $f:u,v\mapsto u+v$
"""
from matplotlib import pyplot as plt

from gemseo import sample_disciplines
from gemseo.algos.parameter_space import ParameterSpace
from gemseo.disciplines.analytic import AnalyticDiscipline
from gemseo.uncertainty.statistics.empirical_statistics import EmpiricalStatistics

# %%
# Firstly,
# we define a uncertain space with two normal random variables $u$ and $v$
# with mean -1 and +1 and unit standard deviation.
uncertain_space = ParameterSpace()
uncertain_space.add_random_variable("u", "OTNormalDistribution", mu=-1.0)
uncertain_space.add_random_variable("v", "OTNormalDistribution", mu=1.0)

# %%
# Then,
# we define the discipline from analytic formula:
discipline = AnalyticDiscipline({"w": "u+v"})

# %%
# Thirdly,
# we sample the discipline with a Monte Carlo algorithm:
dataset = sample_disciplines([discipline], uncertain_space, ["w"], algo_name="OT_MONTE_CARLO", n_samples=1000)

# %%
# Lastly,
# we create an `EmpiricalStatistics` object to estimate statistics,
# such as mean:
statistics = EmpiricalStatistics(dataset)
mean = statistics.compute_mean()
mean

# %%
# and variance:
variance = statistics.compute_variance()
variance

# %%
# !!! note
#
#     The mean and standard deviation of the output are almost equal to 0 and 2,
#     which is the expected behavior
#     of the sum of two independent Gaussian random variables.

# %%
# We can also plot the histogram of the three random variables:
fig, axes = plt.subplots(1, 3)
for ax, name in zip(axes, ["u", "v", "w"]):
    ax.hist(dataset.get_view(variable_names=name))
    ax.set_title(name)
