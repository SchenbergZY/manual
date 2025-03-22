# TeachBooks Python Package

```{admonition} User types
:class: tip
This section is useful for user type 4-5.
```

{bdg-secondary}`Python Package: teachbooks`

The TeachBooks Python package is a collection of tools that are used to enhance the Jupyter Book software package by adding features and making customization easier. In general, it is only of interest to user types 4 and 5 when building a book locally. However, it may be important for other users to know what the package does, as it is incorporated in the [Deploy Book Workflow](./deploy-book-workflow.md) and, therefore, any book created from the [TeachBooks Template](./teachbooks-template.md). This raises two important points:

1. If you are a book user using the [TeachBooks Template](./teachbooks-template.md) or the [Deploy Book Workflow](./deploy-book-workflow.md), your book is by default built with the `teachbooks` package, and the way your book is built and features that are included in the book may change automatically when it is updated (these will be non-breaking changes; if not, we will notify our mailing list).
2. If you are using the `jupyter-book` package to build your book, some of the features described in this Manual may not be available to you (i.e., those listed on this page). This will be the case if you are using a [setup described in the Jupyter Book Manual](https://jupyterbook.org/en/stable/publish/web.html), for example, [this GitHub workflow](https://jupyterbook.org/en/stable/publish/gh-pages.html).

For those who wish to use the package, it is available on [PyPI](https://pypi.org/project/teachbooks/) and can be installed using `pip install teachbooks`. It adds a few commands to the CLI (e.g., `serve`), but otherwise is meant to be used instead of the `jupyter-book` commands. It is conventionally used in an identical way: 

```
teachbooks build book
```

## List of Features

Items in the list here are currently implemented in the TeachBooks package and described on other pages of this manual:
- Draft-Release Workflow: read more here
- External Contents: 
- Local Server: 

The package is also set up to handle [APA references](./apa) when using the Draft-Release Workflow (the `_ext` subdirectory and its contents are manually copied during the pre-build phase). This will not be necessary once the APA Reference feature is turned into a proper Sphinx extension or Pybtext plugin.