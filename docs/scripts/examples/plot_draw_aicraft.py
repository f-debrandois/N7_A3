"""# Draw an aircraft"""

from gemseo_oad_training.utils import draw_aircraft

# %%
# First,
# we draw the default aircraft:
draw_aircraft()

# %%
# Then,
# we draw an aircraft with a larger wing area:
draw_aircraft(area=200, title="Area = 200")

# %%
# Lastly,
# we draw an aircraft with a smaller wing area:
draw_aircraft(area=80, title="Area = 80")
