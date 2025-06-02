"""
# Create a discipline from a Python function
"""

from gemseo.disciplines.auto_py import AutoPyDiscipline


# %%
# Let us consider the Python function computing the area of a rectangle:
def compute_area(width: float = 1., length: float = 1.) -> float:
    """Compute the area of a rectangle.

    Args:
        width: The width of the rectangle.
        length: The length of the rectangle.

    Returns:
        The area of the rectangle.
    """
    area = width * length
    return area

# %%
# We can easily a GEMSEO discipline from this Python function:
discipline = AutoPyDiscipline(compute_area)

# %%
# and check its inputs:
list(discipline.io.input_grammar)

# %%
# outputs:
list(discipline.io.output_grammar)

# %%
# and default input values:
discipline.io.input_grammar.defaults

# %%
# By default,
# its execution evaluates the Python functions using its default argument values:
discipline.execute()

# %%
# We can change the value of the width:
discipline.execute({"width": 2.})

# %%
# of the length:
discipline.execute({"length": 3.})

# %%
# of the width and the length:
discipline.execute({"width": 2., "length": 3.})
