"""
# Create an uncertain space

GEMSEO does not offer an uncertain space but a `ParameterSpace`,
grouping both deterministic and uncertain variables.
This is a subclass of `DesignSpace`
with a method `add_random_variable`.

If you want to create an uncertain space,
create a `ParameterSpace` and only use its `add_random_variable` method.

## Create an uncertain space

Firstly,
we create an empty `ParameterSpace`
from the high-level function `create_parameter_space`:
"""

from gemseo.algos.parameter_space import ParameterSpace

uncertain_space = ParameterSpace()

# %%
# and add a first uncertain variable $u$,
# following the standard Gaussian distribution
uncertain_space.add_random_variable("u", "OTNormalDistribution")

# %%
# !!! note
#     OT stands for OpenTURNS, the UQ library used for sampling.

# %%
# We can also add a second uncertain variable $v$
# following the Gaussian distribution with mean 2 and standard deviation 0.5:
uncertain_space.add_random_variable("v", "OTNormalDistribution", mu=2, sigma=0.5)

# %%
# as well as a third uncertain variable $w$
# following a triangular distribution:
uncertain_space.add_random_variable(
    "z", "OTTriangularDistribution", minimum=-1.0, mode=0.5, maximum=1.0
)

# %%
# We can print this `ParameterSpace`:
uncertain_space

# %%
# .. note::
#    The initial current value corresponds to the mean of the random variables.

# %%
# ## Create a class of uncertain space
# If we want to use this uncertain space more than once,
# it can be more convenient and Pythonic to use the object-oriented paradigm
# and subclass `ParameterSpace`:

from gemseo.algos.parameter_space import ParameterSpace


class MyUncertainSpace(ParameterSpace):
    def __init__(self):
        super().__init__()
        self.add_random_variable("u", "OTNormalDistribution")
        self.add_random_variable("v", "OTNormalDistribution", mu=2, sigma=0.5)
        self.add_random_variable(
            "z", "OTTriangularDistribution", minimum=-1.0, mode=0.5, maximum=1.0
        )


# %%
# Then,
# we only have to instantiate `MyUncertainSpace`:
uncertain_space = MyUncertainSpace()
uncertain_space
