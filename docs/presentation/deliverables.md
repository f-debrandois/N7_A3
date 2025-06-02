# Deliverables

## Code

A series of Python scripts containing:

- Python code,
- documentation.

These scripts must be placed in the directory **docs/scripts/project**.

Moreover, they must be properly formatted
in order to be correctly compiled when using `mkdocs build` and `mkdocs serve`
(or `mkdocs.exe build` and `mkdocs.exe serve` under Windows):

* the header docstring will be converted into an HTML block,
* the Python comment blocks whose first line is `# %%` will be converted into HTML blocks,
* the Python code will be executed if and only if the file name starts with `"plot_"` (e.g. `"plot_example_name.py"`);
  do not prefix the file name if the execution is long.  
* the string representation of objects will be displayed in webpage in a nice way
  (e.g. table for pandas DataFrame, console output for strings, etc.)
  and the matplotlib figures will be plotted in the webpage.

!!! note

    You do not need to compile the project every time you change the Python script.
    You can use this Python script like any other Python script
    and compile the project only after the script writing is finished.
    When the project is compiled,
    only the scripts that have evolved are recompiled.

Here is an example of a well-formatted and documented Python code:

```

   r"""
   # Sum function

   In this example,
   we implement a function summing the elements of a vector $x\in\mathbb{R}^d$:

   $$f(x)=\sum_{i=1}^d x_i$$
   """
   import matplotlib.pyplot as plt
   from numpy import array

   # %%
   # Firstly,
   # we define the function:
   def f(x):
       return x.sum()

   # %%
   # Then,
   # we evaluate this function from the input vector $x=[1,2]$:
   y = f(array([1.,2.]))

   # %%
   # and we display the output value:
   y

   # Contrarily to the previous ones,
   # this comment will not be converted into an HTML block
   # because it does not start with #%%.
   # It will appear as a Python comment.
   
   # %%
   # Lastly,
   # we can draw a line using matplotlib
   plt.plot([0, 1], [0, 2])
```

## Report

### Content

A report containing:

* the author names,
* a title
* from four to six keywords,
* an abstract (no more than 1 300 characters),
* an introduction,
* a section for each problem, ending with a synthesis.
* a general conclusion.

The syntheses and the general conclusion summarize the main facts
for someone who does not want to read the details.

Furthermore, all the results provided must be interpreted.

### Format

Either a markdown-based HTML document or a PDF document.

In the case of a markdown-based HTML report,
the markdown files must be placed in the directory **lh2pac/docs/report**
and referenced in the **nav/Report** section of the *mkdocs.yml* file.