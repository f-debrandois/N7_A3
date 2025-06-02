"""# Convert units

The data presented in the use case description are often expressed with usual units
but the simulator requires standard units.
This example illustrates how to convert a data from a unit to another.

First,
we load the `convert_from` and `convert_to` functions:
"""
from gemseo_oad_training.unit import convert_from
from gemseo_oad_training.unit import convert_to

# %%
# Then,
# we consider a time value expressed in hours:
time_in_hours = 1

# %%
# Lastly,
# we convert it into seconds:
time_in_seconds = convert_from("h", time_in_hours)
time_in_seconds

# %%
# and convert this number of seconds into minutes:
time_in_minutes = convert_to("min", time_in_seconds)
time_in_minutes

# %%
# !!! seealso
#     [The available units](https://gemseo.gitlab.io/dev/gemseo-oad-training/develop/reference/gemseo_oad_training/unit/)