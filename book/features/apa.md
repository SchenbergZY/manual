````{margin}
```{admonition} User types
:class: tip
This page is useful for user type 4 and 5.
```

{bdg-primary}`(To be converted into) Sphinx Extension`
{bdg-link-secondary}`Supported by TeachBooks package <./teachbooks_intro.html>`


````

(apa)=
# APA References

```{note}
This feature is stable but because it relies on a local extension that is part of your book files and _not_ managed as part of a computing environment (e.g., `pip` or `conda`), unknown issues may arise. We would like to convert this feature into an independent Sphinx extension and/or Pybtext plugin. Visit the README in the [project page on GitHub](https://github.com/orgs/TeachBooks/projects/17?pane=info) to learn more.

The instructions provided here will work under conventional usage with Jupyter Book (e.g., `jupyter book build book`).

A temporary fix has also been implemented in the TeachBooks package for use with the Deploy Book Workflow (release mode) (see [release notes from v0.1.0](https://github.com/TeachBooks/TeachBooks/releases/tag/v0.1.0)).

_Update, October 21, 2025: a new fix was necessitated due to dependency issues with docutils making it no longer necessary to pin this package. See [PR 207 of the Manual for a description](https://github.com/TeachBooks/manual/pull/207).
```

## Introduction

Do you include references in your book, but you're tired of the default options available in Jupyter Book? For example, the square-bracket style of citation and reference, where the first three letters of the name year are combined in a way that seems designed to minimize transparency?

There is a solution! This extension allows you to have APA formatting in your book.

## Installation
To use APA-references, a set of Python files need to be manually loaded into your book.

**Step 1: files to root directory of your book**

Download this zip-file [`apa_config.zip`](apa_config.zip), which contains the necessary files, located in _two_ subdirectories: `_ext` and `_static`. Unzip and place the contents in the root of your book directory so that it looks like the schematic here:

```
book
├── _ext/
│   ├── pybtexapastyle/
│   ├── apastyle.py
│   └── bracket_citation_style.py
├── _static/
|   ├── ...
│   └── apastyle.css
├── _config.yml
├── _toc.yml
├── requirements.txt
├── <book files>
```

Note that you may or may not already have a `_static` subdirectory, to which the file `apastyle.css` should be added.

**Step 2: Enable in `_config.yml`**

In your `_config.yml` file, add a `bibtex_default_style`, `bybtex_reference_style` and the local extensions `apastyle` and `bracket_citation_style.py`. This enables the (local) extension.

```
sphinx:
  config:
    ...
    bibtex_default_style: myapastyle
    bibtex_reference_style: author_year_round
  local_extensions:
    apastyle: _ext/
    bracket_citation_style: _ext/
  ...
```

**Step 3: Enable in `_config.yml`**

In your `_config.yml` file, add a `_static` is listed under `html_static_path`. This ensures the CSS file is included.

```
sphinx:
  config:
    ...
    html_static_path: ["_static", ...]
  ...
```

## Usage

All references are now made in APA-style. See for example this reference: {cite:t}`jason_moore` which shows up on the [references page](../references.md) too. The form of the citation looks like this:

```
{cite:t}`jason_moore`
```

Here are three examples for making citations:

| Syntax | Result |
| :---: | :---: |
|`{cite:t}` | {cite:t}`jason_moore` |
|`{cite:p}`| {cite:p}`jason_moore` |
|`{cite}`| {cite}`jason_moore` |

For more options on the in-line citation style, see https://jupyterbook.org/en/stable/content/citations.html#change-the-in-line-citation-style.

### Known Issues

Two issues are known:
- During the build, warning will be raised with `... WARNING: duplicate label for keys ...`. In most cases, these warnings can be ignored. As noted above, the book will not build references properly 
- In case you have both an `.ipynb` and `.md` version of a file, the `.md` version will always be used whenever this extension is used. This removes the possibility to show code outputs.

## Implementation

The extension is based on [`pybtex`](https://pybtex.org/), which is a BibTeX-compatible bibliography processor in Python that is extendible with plugins. 

Although some customization is possible with the standard Jupyter Book features, [as described here](https://jupyterbook.org/en/stable/content/citations.html#change-the-in-line-citation-style), this extension implements the complete APA style, as well as enforcing round brackets (like this).

The need to include a CSS file is an easy solution to the issue where empty brackets `[]` are left on the references page (to try it, simply delete `apastyle.css`).

## Contribute

This tool needs to be developed further to make it into a proper sphinx-extension (and/or an independent `pybtext` plugin). The process is described in the README of this [project page on GitHub](https://github.com/orgs/TeachBooks/projects/17?pane=info). If you've ideas or questions, please reach out to us at info@teachbooks.io!
