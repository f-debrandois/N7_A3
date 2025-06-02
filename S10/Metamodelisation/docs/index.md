# Overall aircraft design (OAD)

An OAD is a multidisciplinary design process
considering various disciplines 
such as flight mission, aerodynamics, structural sizing, mass distributions, propulsion, systems, etc.

## Motivations

The aim of this project is to do OAD
by combining several models with three mathematical fields,
namely surrogate modeling, uncertainty quantification and optimization:

- optimization algorithms are commonly used to solve design problems,
  with the multidisciplinary-design optimization (MDO) branch in the case of several models, a.k.a. disciplines,
- uncertainty quantification (UQ) is becoming increasingly popular 
  to take into account various sources of uncertainties
  that may occur during the design cycle,
- surrogate models, a.k.a. metamodels, are enablers for optimization and UQ
  because the numerical simulators are often computationally expensive
  and do not allow a sufficient number of evaluations to be obtained 
  to estimate statistics properly or to converge a numerical optimization algorithm.

## Problems

### Introduction

The design problem aims to minimize the maximal take-off mass of an aircraft
whilst ensuring some constraints 
such as a maximal take-off field length and a maximal approach speed.

For this purpose,
it will be possible to play with four design parameters.

By the way,
the design takes place in an uncertain environment
where the technological choices can be probabilized.

In the following,
we will note $f:x,u\mapsto f(x,u)$
the outputs of interest of the models
where $x$ are the design parameters and $u$ the uncertain ones.

We will assume that their evaluation cost is very high,
and so we will try to replace $f$ with a surrogate model
to address the following problem. 

### Problem 1 - Surrogate modeling and optimization

We will create a surrogate model of $\hat{f}:x\mapsto \hat{f}(x)=f(x,u_{\mathrm{default}})$
to approximate the objective and constraints of the design problem
with respect to the design parameters $x$.
Then,
we will use this surrogate model in an optimization process
to minimize the objective whilst ensuring the constraints
by varying the design parameters.

### Problem 2 - Surrogate modeling and uncertainty quantification

We will create a surrogate model of $\hat{f}:u\mapsto \hat{f}(x)=f(x_{\mathrm{default}},u)$
to approximate the objective and constraints of the design problem
with respect to the uncertain parameters $u$.
Then,
we will use this surrogate model in an uncertainty study
to propagate the uncertainty related to the technological choices,
quantify the resulting output uncertainty
and explain it from the uncertainty sources (sensitivity analysis).

### Problem 3 - Surrogate modeling and robust optimization

We will create a surrogate model of $\hat{f}:x,u\mapsto \hat{f}(x)=f(x,u)$
to approximate the objective and constraints of the design problem
with respect to both design parameters $x$ and uncertain parameters $u$.
Then,
we will use this surrogate model to to seek the best aircraft concept
taking into account the uncertainty of technological choices.

## Software

To solve these problems,
we will use the [GEMSEO](https://gemseo.readthedocs.io/en/stable/) Python library 
for problem definition, optimization, surrogate modeling and uncertainty quantification.
GEMSEO relies on popular Python libraries,
such as 
[scikit-learn](https://github.com/scikit-learn/scikit-learn>) for surrogate modeling,
[OpenTURNS](https://github.com/openturns/openturns>) for uncertainty quantification,
[NumPy](https://numpy.org/) and [SciPy](https://scipy.org/) for scientific computing
and [matplotlib](https://matplotlib.org/) for visualization.

GEMSEO includes the main package [gemseo](https://gitlab.com/gemseo/dev/gemseo)
as well as extensions and plugins.
In particular,
we will use:

- [gemseo-oad-training](https://gitlab.com/gemseo/dev/gemseo-oad-training)
  ([documentation](https://gemseo.gitlab.io/dev/gemseo-oad-training/develop/))
  to create the models and their settings,
- [gemseo-umdo](https://gitlab.com/gemseo/dev/gemseo-umdo)
  ([documentation](https://gemseo.gitlab.io/dev/gemseo-umdo/develop/))
  for MDO under uncertainty,
- [gemseo-mlearning](https://gitlab.com/gemseo/dev/gemseo-mlearning)
  ([documentation](https://gemseo.gitlab.io/dev/gemseo-mlearning/develop/))
  for advanced machine learning techniques.

## What should I do?

1. Discover GEMSEO through [these examples](generated/scripts/examples/index.md) and the software documentations.
2. Read the descriptions of the [use cases](presentation/use_cases.md).
4. Solve Problem 1 for Use Case 1 and Use Case 2.
5. Solve Problem 2 for Use Case 1 and Use Case 2
     - at the initial design,
     - at the optimal design found at Step 4.
6. Solve Problem 3 for Use Case 1 and Use Case 2.
7. Write the report.