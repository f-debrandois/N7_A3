# The LH2PAC project

LH2PAC is a Python-based academic project proposed by Matthias De Lozzo and Thierry Druot
in the frame of the course **"Metamodels"**
from the [ModIA program](https://www.math.insa-toulouse.fr/fr/enseignement/apprentissage-modia.html).

## Installation

### Git

#### Clone (only once)

In your favorite working directory,
e.g. `"my_wd"`,

```
git clone git@gitlab.com:MatthiasDeLozzo/lh2pac.git
```

This will create a directory `"lh2pac"` in `"my_wd"`.

#### Create a working branch (only once)

In the directory `"lh2pac"`:

```
git checkout origin/modia2025 -b my_modia2025  
```

#### Rebase your working branch

From time to time, 
I can update the _git_ project with miscellaneous information; 
you will then have to rebase your branch.

Make sure you are on `my_modia2025`; 
otherwise: `git checkout my_modia2025`.

In the directory `"my_wd/lh2pac"`:

```
git fetch origin
git rebase origin/modia2025
```

### Create a virtual environment (only once)

In the directory `"lh2pac"`:

=== "Linux"

    ```
    python -m venv .venv
    source .venv/bin/activate
    pip install --editable .
    source .venv/bin/deactivate
    ```

=== "Windows"

    ```
    python -m venv .venv
    .venv\Scripts\activate.bat
    pip install --editable .
    .venv\Scripts\deactivate.bat
    ```

### Configure your IDE (only once)

Select the Python interpreter: 

=== "Linux"

    `"my_wd/lh2pac/.venv/bin/python"`

=== "Windows"

    `"lh2pac\.venv\Scripts\python.exe"`

### Use your virtual environment in a Python console

In the directory `"lh2pac"`:

=== "Linux"

    ```
    source .venv/bin/activate
    ```

=== "Windows"

    ```
    .venv\Scripts\activate.bat
    ```

and use Python as usual.

### Compile the documentation

#### Compile each time you save a file (temporary doc)

=== "Linux"

    ```
    mkdocs serve
    ```

=== "Windows"

    ```
    mkdocs.exe serve
    ```

The documentation is generated and can be accessed at a local domain,
e.g. [http://127.0.0.1:8000](http://127.0.0.1:8000).

Then,
every time you save a file,
the documentation will be updated automatically.

#### Compile (permanent doc)

The previous command does not save the website;
to do so, use the following command.

=== "Linux"

    ```
    mkdocs build
    ```

=== "Windows"

    ```
    mkdocs.exe build
    ```

The LH2PAC adventure starts here!
