r"""
# Perform a sensitivity analysis

In this example,
we will use the Sobol' analysis to quantify
the sensitivity of the output of the Ishigami function to its inputs:

$$f(x_1,x_2,x_3)=\sin(x_1)+7\sin(x_2)^2+0.1*x_3^4\sin(x_1)$$

where $x_1,x_2,x_3\in[-\pi,\pi]$.
"""

import pprint

from gemseo.algos.parameter_space import ParameterSpace
from gemseo.disciplines.analytic import AnalyticDiscipline
from gemseo.uncertainty.sensitivity.sobol_analysis import SobolAnalysis
from numpy import pi

# %%
# Firstly,
# we create the Ishigami function:
discipline = AnalyticDiscipline(
    {"y": "sin(x2)+7*sin(x1)**2+0.1*x3**4*sin(x2)"},
    name="Ishigami",
)

# %%
# Then,
# we define the uncertain space with uniform distributions:
uncertain_space = ParameterSpace()
for name in ["x1", "x2", "x3"]:
    uncertain_space.add_random_variable(
        name, "OTUniformDistribution", minimum=-pi, maximum=pi
    )

# %%
# From that,
# we launch a Sobol' analysis with a maximum of 10000 samples:
#
# !!! warning
#
#     The estimation of Sobol' indices relies on the pick-and-freeze (PF) DOE algorithm
#     and most of the UQ libraries generates $(1+p)N$ evaluations
#     where $p$ is the dimension of the input space
#     and $N$ is presented as *the number of samples*.
#     In fact,
#     $N$ is not the number of samples of the simulators
#     but the number of samples in the sense of the PF-based estimators,
#     which is misleading.
#     This is reason why GEMSEO considers a maximum number of samples $n$,
#     *i.e* a maximum number of simulations,
#     and then $N$ is deduced from this number: $N=\lceil n/(1+p)\rceil$.
#
sobol = SobolAnalysis()
sobol.compute_samples([discipline], uncertain_space, 10000)
sobol.compute_indices()

# %%
# and print the results:
pprint.pprint(sobol.indices.first)
pprint.pprint(sobol.indices.total)

# %%
# We can also visualize both first-order and total Sobol' indices
# that are automatically sorted by magnitude:
sobol.plot("y", save=False, show=True)
