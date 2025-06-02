# Installation

## Git

### Clone (only once)

In your favorite working directory,
e.g. `"my_wd"`,

```
git clone git@gitlab.com:MatthiasDeLozzo/lh2pac.git
```

This will create a directory `"lh2pac"` in `"my_wd"`.

### Create a working branch (only once)

In the directory `"lh2pac"`:

```
git checkout origin/modia2024 -b my_modia2024  
```

### Rebase your working branch

From time to time, 
I can update the _git_ project with miscellaneous information; 
you will then have to rebase your branch.

Make sure you are on `my_modia2024`; 
otherwise: `git checkout my_modia2024`.

In the directory `"my_wd/lh2pac"`:

```
git fetch origin
git rebase origin/modia2024
```

## Create a virtual environment (only once)

In the directory `"lh2pac"`:

=== ":fontawesome-brands-linux: Linux"

    ```
    python -m venv .venv
    source .venv/bin/activate
    pip install --editable .
    source .venv/bin/deactivate
    ```

=== ":fontawesome-brands-windows: Windows"

    ```
    python -m venv .venv
    .venv\Scripts\activate.bat
    pip install --editable .
    .venv\Scripts\deactivate.bat
    ```

## Configure your IDE (only once)

Select the Python interpreter: 

=== ":fontawesome-brands-linux: Linux"

    `"my_wd/lh2pac/.venv/bin/python"`

=== ":fontawesome-brands-windows: Windows"

    `"lh2pac\.venv\Scripts\python.exe"`

## Use your virtual environment in a Python console

In the directory `"lh2pac"`:

=== ":fontawesome-brands-linux: Linux"

    ```
    source .venv/bin/activate
    ```

=== ":fontawesome-brands-windows: Windows"

    ```
    .venv\Scripts\activate.bat
    ```

and use Python as usual.

## Compile the documentation

### Compile each time you save a file (temporary doc)

=== ":fontawesome-brands-linux: Linux"

    ```
    mkdocs serve
    ```

=== ":fontawesome-brands-windows: Windows"

    ```
    mkdocs.exe serve
    ```

The documentation is generated and can be accessed at a local domain,
e.g. [http://127.0.0.1:8000](http://127.0.0.1:8000).

Then,
every time you save a file,
the documentation will be updated automatically.

### Compile (permanent doc)

The previous command does not save the website;
to do so, use the following command.

=== ":fontawesome-brands-linux: Linux"

    ```
    mkdocs build
    ```

=== ":fontawesome-brands-windows: Windows"

    ```
    mkdocs.exe build
    ```