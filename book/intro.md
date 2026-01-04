---
file_format: mystnb
kernelspec:
  name: python3
---

# TeachBooks Manual

## Nesting inside of a start-directive

### Different directives

::::{prf:theorem-start} The parent theorem
:label: parent-theorem-label

This is a parent theorem. This text is inside the parent theorem.

:::{prf:axiom-start} A child axiom
:label: child-axiom-label

This is a child axiom. This text is inside the child directive.
:::

This is text after the child-start, before the child-end, inside the parent theorem.

:::{prf:axiom-end}
Text inside the end. This text will not be rendered.
:::

Finally some text after the entire child, inside the theorem start.

::::

Some text after the entire parent theorem start, but before the parent theorem end.

:::{prf:theorem-end}
:::

### Same directives

::::{prf:theorem-start} The parent theorem
:label: parent-theorem-label2

This is a parent theorem. This text is inside the parent theorem.

:::{prf:theorem-start} A child theorem
:label: child-theorem-label

This is a child theorem. This text is inside the child directive.
:::

This is text after the child-start, before the child-end, inside the parent theorem.

:::{prf:theorem-end}
:::

Finally some text after the entire child, inside the theorem start.

::::

Some text after the entire parent theorem start, but before the parent theorem end.

:::{prf:theorem-end}
:::

## Nesting outside of a start-directive

### Different directives

::::{prf:theorem-start} The parent theorem
:label: parent-theorem-label3

This is a parent theorem. This text is inside the parent theorem.
::::

Some text outside the parent theorem start, before the child start directive.

:::{exercise-start} A child exercise
:label: child-exercise-label2

This is a child exercise. This text is inside the child directive.
:::

This is text after the child-start, before the child-end.

:::{exercise-end}
:::

Finally some text after the entire child, outside the theorem start, before the end.

:::{prf:theorem-end}
:::

:::{exercise} This is an exercise outside any theorem.
:label: exercise-outside-theorem

Solve this exercise.
:::

### Same directives

::::{prf:theorem-start} The parent theorem
:label: parent-theorem-label4

This is a parent theorem. This text is inside the parent theorem.
::::

Some text outside the parent theorem start, before the child start directive.

:::{prf:theorem-start} A child theorem
:label: child-theorem-label5

This is a child theorem. This text is inside the child directive.
:::

This is text after the child-start, before the child-end.

:::{prf:theorem-end}
:::

Finally some text after the entire child, outside the theorem start, before the end.

:::{prf:theorem-end}
:::

### Nested exercise directives

:::{exercise-start} An outer exercise with an inner exercise between start and end
:label: outer-exercise-label
This is an outer exercise. This text is inside the outer exercise.
:::

:::{exercise-start} An inner exercise
:label: inner-exercise-label
This is an inner exercise. This text is inside the inner exercise.
:::
This is text after the inner exercise start, before the inner exercise end.

:::{exercise-end}
:::

Finally some text after the entire inner exercise, inside the outer exercise.

:::{exercise-end}
:::

## Examples with code

### Block directive with also a figure

:::{prf:theorem-start} A title
:label: theorem-label

This is a theorem. This text is inside the directive.
:::

Now some extra text that should come inside the theorem.

:::{figure} images/sphinx-logo.svg
:alt: Sphinx logo
:width: 200px
:align: center

Sphinx is a great tool for documentation! This figure should be inside the theorem.
:::

```{code-cell} ipython3
a = "This is some"
b = "Python code"
c = "that should be inside the theorem."
print(f"{a} {b} {c}")
```

:::{prf:theorem-end}
:::

### Figure directive with nothing with also another figure

:::{figure-start} images/nothing.svg
:name: figure-label
:alt: Nothing
:align: center

This is a figure. This text is inside the caption.
:::

```{code-cell} ipython3
a = "This is some"
b = "Python code"
c = "that should be inside the figure,"
d = "above the caption."
print(f"{a} {b} {c} {d}")
```

Now some extra text that should come inside the figure, above the caption.

:::{figure} images/sphinx-logo.svg
:alt: Sphinx logo
:width: 200px
:align: center

Sphinx is a great tool for documentation! This figure should be inside the parent figure, above the parent caption.
:::

:::{figure-end}
:::

This manual is primarily designed for and by teachers for use in education, but should be a useful resource for anyone interested in creating and collaborating on a TeachBook: a <a href="https://jupyterbook.org/v1/"><img  style="display:inline-block; height:1.5em; width:auto; transform:translate(0, -0.15em)" src="images/logo-wide.svg" alt="Jupyter book v1"> v1</a> using the <a href="https://www.sphinx-doc.org/"><img  style="display:inline-block; height:1.5em; width:auto; transform:translate(0, -0.15em)" src="images/sphinx-logo.svg" alt="Sphinx logo"> Sphinx backend</a> with additional editing tools and book features. Our aim is to provide a simple way to start book-making for new users (it only takes 10 clicks!), ease the editing process for anyone, and provide additional features developed for education-purposes. We hope you find this resource useful and refer back to it often.

TeachBooks originated at Delft University of Technology in the Netherlands, and some of the material in this Manual reflects tools and resources specific to TU Delft. With the exception of a few tools for which we have educational licenses at Delft, everything in this Manual is open source. Despite this, we are happy to grow our open source community beyond Delft and welcome contributions from all users.

For more information about TeachBooks, visit [https://teachbooks.io/](https://teachbooks.io/). Do not hesitate to reach out via email at [info@teachbooks.io](mailto:info@teachbooks.io) or contribute on GitHub via discussions, issues or pull requests.

Happy book building!

## How to Use this Manual

There are several "parts" to the manual:
- **Your First TeachBook!** introduces the essential platforms and workflows, and contains a _workshop_ that can be completed independently or as part of a TeachBooks training. We recommend even experienced Jupyter Book v1 users go through this material to better understand the TeachBooks vision on how to make books collaboratively, as this drives much of our tool development. The workshop is designed to be completed in 1-2 hours and does not require any prior knowledge or installation (just a GitHub account).
- **Getting Going!** begins with an overview of _User Types_, which are used to help understand which parts of the Manual are most relevant to you. Detailed software installation instructions, book and team setup and workflows are also provided in this part.
- The **Features** part describes a suite of tools that are useful for teachers, many of which are developed by TeachBooks contributors specifically for use in education. Many of these tools are illustrated in the **Examples**.
- A few special tools are included in the **Editing Tools** that are useful when writing content.

See the final chapters of this book (under **Miscellaneous**) for additional information about References, Credits, etc.
