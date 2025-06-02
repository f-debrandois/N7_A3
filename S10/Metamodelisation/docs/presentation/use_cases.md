# 4 OAD use cases

In this project,
we seek to optimize an aircraft of approximately 150 passengers that flies at Mach 0.78,
using different engine and fuel technologies.

## The OAD problem

The OAD problem is to find the values of the design parameters 
that minimize the maximum take-off mass (MTOM, `mtom` in the code) under some operation constraints.
Note that the MTOM of an airplane is a good criterion to optimize the design.
Alternative objectives are the cash operating cost (COC, `coc` in the code) or the direct operating cost (DOC, `doc` in the code).

### The design parameters

The **design parameters** are :

- the maximum sea level static thrust  (100 kN ≤ slst ≤ 200 kN, default: 150 kN),
- the number of passengers  (120 ≤ n_pax ≤ 180, default: 150),
- the wing area (100 m² ≤ area ≤ 200 m², default: 180 m²),
- the wing aspect ratio  (5 ≤ ar ≤ 20, default: 9.).

### The operational constraints

The **operational constraints** are :

- the take-off field length (tofl ≤ 1900 m),
- the approach speed (vapp ≤ 135 kt),
- the vertical speed (300 ft/min ≤ vz),
- the wing span (span ≤ 40 m),
- the wing length (length ≤ 45 m),
- the fuel margin (0% ≤ fm).

## The uncertain parameters

In Problems 2 and 3,
some parameters are considered as uncertain.

These uncertain parameters are modelled as random variables defined by probability distributions:

| Variable | Distribution          | Fuel type | Engine type |
|----------|-----------------------|-----------|-------------|
| `gi`     | T(0.35, 0.4, 0.405)   | liquid_h2 | All         |
| `vi`     | T(0.755, 0.800, 0805) | liquid_h2 | All         |
| `aef`    | T(0.99, 1., 1.03)     | All       | All         |
| `cef`    | T(0.99, 1., 1.03)     | All       | All         |
| `aef`    | T(0.99, 1., 1.03)     | All       | All         |
| `fc_pwd` | T(0.8, 1, 1.02)       | liquid_h2 | electrofan  |
| `bed`    | U(400,700)            | battery   | All         |

where `T(minimum, mode, maximum)` and `U(minimum,maximum)`
represent the [triangular distribution](https://en.wikipedia.org/wiki/Triangular_distribution)
and the [uniform distribution](https://en.wikipedia.org/wiki/Continuous_uniform_distribution) respectively.
the last two columns indicate the type of fuel and the type of engine
for which these uncertain parameters are relevant.

The parameters `aef`, `cef` and `aef` are related
to the three main technical areas involved in aircraft design,
namely aerodynamics, propulsion and structure.
The lower, the better.
These factors are representing the unknown
included in any creative activity.
Their probability distributions are not symmetrical
as it is always easier to make something less efficient than expected...

## The 12 models

The 12 models are defined in `gemseo-oad` as Python functions:

```python
from gemseo_oad_training.models import aerodynamic
from gemseo_oad_training.models import approach
from gemseo_oad_training.models import battery
from gemseo_oad_training.models import climb
from gemseo_oad_training.models import engine
from gemseo_oad_training.models import fuel_tank
from gemseo_oad_training.models import geometry
from gemseo_oad_training.models import mass
from gemseo_oad_training.models import mission
from gemseo_oad_training.models import operating_cost
from gemseo_oad_training.models import take_off
from gemseo_oad_training.models import total_mass
```

Some models do not make sense for certain aircraft configurations,
e.g. battery for an aircraft equipped with a turbofan engine,
but you can still include them in your multidisciplinary process,
and they will remain silent.

!!! seealso "About the models"
    You will find more information about these models on 
    [this page](https://gemseo.gitlab.io/dev/gemseo-oad-training/develop/reference/gemseo_oad_training/models).

## The units

The use cases are written using common units.

The models only know STANDARD UNITS which means
that all data provided to the function MUST be expressed in standard units
and that all data retrieved by the function are expressed in standard units.

!!! tip "Convert units"
    The functions `convert_from` and `convert_to` from `gemseo_oad_training.unit` can make the conversion easier.

## The four use cases

| Id  | Fuel type | Engine type | Design range (km) |
|-----|-----------|-------------|-------------------|
| UC1 | Kerosene  | Turbofan    | 5500              |
| UC2 | Hydrogen  | Turbofan    | 5500              |
| UC3 | Hydrogen  | Electrofan  | 5500              |
| UC4 | Battery   | Electrofan  | 500               |

## Credits

This OAD problem uses the models presented in [gemseo-oad-training](https://gemseo.gitlab.io/dev/gemseo-oad-training/latest/) 
that have been developed by the CADO (Conceptual Airplane Design & Operations) team,
made up of Nicolas PETEILH, Pascal ROCHES, Nicolas MONROLIN, Thierry DRUOT,
from the Aircraft & Systems, Air Transport Department at [ENAC](https://www.enac.fr/fr).
This team also strongly inspired the use cases (UCs) proposed in this project.