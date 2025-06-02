"""
# Update the default input values of given disciplines
"""
from gemseo.disciplines.analytic import AnalyticDiscipline
from numpy import array

from lh2pac.utils import update_default_inputs

discipline_1 = AnalyticDiscipline({"y": "a+b"})
discipline_2 = AnalyticDiscipline({"z": "a+d"})

# %%
# The default input values before updating
discipline_1.io.input_grammar.defaults, discipline_2.io.input_grammar.defaults

# %%
# Updating default input values
update_default_inputs([discipline_1, discipline_2], {"a": array([1.])})

# %%
# The default input values after updating
discipline_1.io.input_grammar.defaults, discipline_2.io.input_grammar.defaults
