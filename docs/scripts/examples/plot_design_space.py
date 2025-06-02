"""
# Create a design space

A `DesignSpace` defines the space in which the design variables belongs
and is required to set the optimization problem,
in the same way as the objective and the constraints.

## Create a design space

The simplest is to use the function `create_design_space`:
"""

from numpy import array

from gemseo.algos.design_space import DesignSpace

design_space = DesignSpace()

# %%
# This design space can include a design variable $x$
# without bounds and without current value:
design_space.add_variable("x")

# %%
# a design variable $y$ of dimension 2
# with a lower bound and a current value:
design_space.add_variable("y", size=2, lower_bound=0.0, value=array([0.5, 0.75]))

# %%
# as well as a design variable $z$
# with both lower and upper bounds but without default value:
design_space.add_variable("z", lower_bound=-1.0, upper_bound=1.0)

# %%
# Let's take a look at this design space:
design_space

# %%
# ## Create a class of design space
# If we want to use this design space more than once,
# it can be more convenient and Pythonic to use the object-oriented paradigm
# and subclass `DesignSpace`:
class MyDesignSpace(DesignSpace):
    def __init__(self):
        super().__init__(name="foo")
        self.add_variable("x")
        self.add_variable("y", size=2, lower_bound=0.0, value=array([0.5, 0.75]))
        self.add_variable("z", lower_bound=-1.0, upper_bound=1.0)


# %%
# Then,
# we only have to instantiate `MyDesignSpace`:
design_space = MyDesignSpace()
design_space
