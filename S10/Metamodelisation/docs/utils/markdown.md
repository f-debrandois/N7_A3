# Introduction to the markdown syntax


[markdown](https://en.wikipedia.org/wiki/Markdown) is an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax and parser system.
This is the plaintext markup language used by [mkdocs](https://www.mkdocs.org/),
the generator of the current HTML project.
Here is a short but normally sufficient introduction to markdown.
For a deeper insight, 
please refer to this [markdown presentation](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html).
and to this [Material-for-MkDocs page](https://squidfunk.github.io/mkdocs-material/reference/).

## Sections

Split a page into sections:

```
    # Main title

    ## Sub-title

    ### Sub-sub-title
```    

## Paragraphs

Separate paragraph with blank lines.

```
    This is a paragraph.
    This is the same paragraph.

    This is a new paragraph separated from the previous one with a blank line.
```    

This is a paragraph.
This is the same paragraph.

This is a new paragraph separated from the previous one with a blank line.

## Text formatting

Surround a text with one asterisk
and without whitespace between the text and the asterisk.

```
    Put a expression in *italics*.

    Put a expression in **bold**.

    Cannot but an expression both in ***italics and bold***.
```    

Put an expression in *italics*.

Put an expression in **bold**.

Cannot but an expression both in ***italics and bold***.

## Hyperlink

Use `[expression](url)`.

This is a hyperlink to an external content: [DuckDuckGo](https://duckduckgo.com/).

## Lists

### Unnumbered list

```
    - An item.
    - Another item.

        * A sub-item (pay attention to the indentation: 4 spaces).
        * Another sub-item.

    - Another item
      written on two lines.

        1. A first sub-item (pay attention to the indentation: 4 spaces).
        2. A second sub-item.
```

- An item.
- Another item.

    * A sub-item (pay attention to the indentation: 4 spaces).
    * Another sub-item.

- Another item
  written on two lines.

    1. A first sub-item (pay attention to the indentation: 4 spaces).
    2. A second sub-item.

### Numbered list

```
    1. An item.
    1. A second item.

        - A sub-item (pay attention to the indentation: 4 spaces).
        - Another sub-item.

    1. A third item
       written on two lines.

        1. A first sub-item (pay attention to the indentation: 4 spaces).
        1. A second sub-item.
```

1. An item.
1. A second item.

    - A sub-item (pay attention to the indentation: 4 spaces).
    - Another sub-item.

1. A third item
   written on two lines.

    1. A first sub-item (pay attention to the indentation: 4 spaces).
    1. A second sub-item.

## Code insertion

```
    Insert inline code: `y = f(x)`
```

Insert inline code: `y = f(x)`

Insert a block code using triple backquotes:

```
    ```python

       def f(x):
          return 2*x
    ```
```

```python
   def f(x):
      return 2*x
```

## Image insertion

!!! warning

    Use of relative file paths.

```
![gemseo](../images/gemseo.png)
```

![gemseo](../images/gemseo.png)

## LaTeX-based mathematics

!!! warning

    Do not hesitate to refresh your browser if the equations are not displayed. 

```
    Einstein wrote $E=mc^2$.
```

Einstein wrote $E=mc^2$.

```
    $$
    \begin{align}
       (a + b)^2  &=  (a + b)(a + b) \\
                  &=  a^2 + 2ab + b^2
    \end{align}       
    $$
```

$$
\begin{align}
   (a + b)^2  &=  (a + b)(a + b) \\
              &=  a^2 + 2ab + b^2
\end{align}
$$

```
    $$(a - b)^2 = a^2 - 2ab + b^2$$
```
$$
(a - b)^2 = a^2 - 2ab + b^2
$$

## Admonitions

Here are a few qualifiers. 
Other are available [here](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types).

```

    !!! note

       This is a *note* block.

    !!! note "Custom title"

       This is a *note* block with a custom title.       

    !!! seealso

       This is a *seealso* block.

    !!! warning

       This is a *warning* block.
```


!!! note

    This is a *note* block.

!!! note "Custom title"

    This is a *note* block with a custom title.       

!!! seealso

    This is a *seealso* block.

!!! warning

    This is a *warning* block.

## Citation

GEMSEO[^1] is an open source software to solve multidisciplinary problem.

[^1]: Gallard, F., Vanaret, C., Guénot, D, et al., GEMS: A Python Library for Automation of Multidisciplinary Design Optimization Process Generation. In : 2018 AIAA/ASCE/AHS/ASC Structures, Structural Dynamics, and Materials Conference. 2018. p. 0657.