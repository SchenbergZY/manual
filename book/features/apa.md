````{margin}
```{admonition} User types
:class: tip
This page is useful for user type 4 and 5.
```

{bdg-primary}`Sphinx Extension`

````

(apa)=
# APA References

## Introduction

Do you include references in your book, but you're tired of the default options available in a TeachBook / Jupyter Book v1? For example, the square-bracket style of citation and reference, where the first three letters of the name year are combined in a way that seems designed to minimize transparency?

There is a solution! This extension allows you to have APA formatting in your book.

## Installation

To use APA-references, install the [Sphinx-APA-References extension](https://github.com/TeachBooks/Sphinx-APA-References) by following these two steps:

**Step 1: Install the Package**

Install the module `sphinx-apa-references` package using `pip`:
```
pip install sphinx-apa-references
```
    
**Step 2: Add to `requirements.txt`**

Make sure that the package is included in your project's `requirements.txt` to track the dependency:
```
sphinx-apa-references
```

**Step 3: Enable in `_config.yml`

In your `_config.yml` file, add the extension to the list of Sphinx extra extensions (**important**: underscore, not dash this time):
```
sphinx: 
    extra_extensions:
        .
        .
        .
        - sphinx_apa_references
        .
        .
        .
```

## Usage

All references are now made in APA-style. Here are five examples how to create a citation in APA style:

| Syntax | Result with 1 author | Result with many authors | Explanation |
| :---: | :---: | :---: | :---: |
|`{cite:t}` | {cite:t}`jason_moore` | {cite:t}`dummyreference` | Textual citation |
|`{cite:p}`| {cite:p}`jason_moore` | {cite:p}`dummyreference` | Parenthetical citation |
|`{cite}`| {cite}`jason_moore` | {cite}`dummyreference` | Same as `{cite:p}` |
|`{cite:ts}` | {cite:ts}`jason_moore` | {cite:ts}`dummyreference` | Same as `{cite:t}`, but without abbreviation of authors |
|`{cite:ps}`| {cite:ps}`jason_moore` | {cite:ps}`dummyreference` |Same as `{cite:p}`, but without abbreviation of authors |

For more options on the in-line citation style, see https://jupyterbook.org/v1/content/citations.html#change-the-in-line-citation-style.

The references section at the end of your book will also be formatted in APA style:

::::{admonition} Example of APA References
:class: example

```{iframe} ../references.html
:class: no-blend
```
::::

## Implementation

The extension is based on [`pybtex`](https://pybtex.org/), which is a BibTeX-compatible bibliography processor in Python that is extendible with plugins. 

Although some customization is possible with the standard Jupyter Book v1 features, [as described here](https://jupyterbook.org/v1/content/citations.html#change-the-in-line-citation-style), this extension implements a complete APA style, as well as enforcing round brackets (like this).
