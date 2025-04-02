(feature_overview)=
# Overview

As TeachBooks, we collect a suite of existing open-source software so you don't have to! Some of the software is developed with our TA's to improve the learning experience of our students and ease the book-development process for our teachers. As the open-source software landscape changes rapidly, it is essential to keep in contact and share resources amongst ourselves to minimize maintenance and downtime for our book websites and focus on what really matters: teaching!

Since the list of TeachBook features is getting quite long, we have grouped them in categories:
- Original Jupyter Book and Sphinx features
- Easy editing process
- Additional functionality
- Book styling
- TeachBooks student-view features

Additionally, not all features are built and shared in the same way. We do our best to make sure that as many tools as possible are included automatically when using our TeachBooks Template Book; if you are not using the Template, we try to make sure each of our tools can be used independently. For transparency, tags will help differentiate between the different backgrounds of the features:
- {bdg-warning}`Javascript overlay`
- {bdg-success}`Chrome Extension`
- {bdg-white}`GitHub App and Javascript script`
- {bdg-link-secondary}`Python Package: teachbooks <./overview.html#teachbooks-python-package>`
- {bdg-light}`GitHub Reusable Action`
- {bdg-light}`GitHub Template`
- {bdg-dark}`Git Workflow`
- {bdg-primary}`Sphinx Extension`
- {bdg-danger}`iframe`

Finally, the purpose, installation process and usage of each features is elaborated on in the respective sub-sections.

To see examples for these features, go to the [Examples chapter](../examples/overview.md).

As the TeachBooks Python Package and the Deploy Book Workflow are important tools that incorporate and deploy more than one feature, an additional explanation is provided on this page in more detail, with links to the pages in this manual where individual features are described.

(teachbooks_package)=
## TeachBooks Python Package

```{admonition} User types
:class: tip
This section is useful for user type 4-5.
```

The TeachBooks Python package is a collection of tools that are used to enhance the Jupyter Book software package by adding features and making customization easier. In general, it is only of interest to user types 4 and 5 when building a book locally. However, it may be important for other users to know what the package does, as it is incorporated in the [Deploy Book Workflow](./deploy-book-workflow.md) and, therefore, any book created from the [TeachBooks Template](../external/template/README.md). This raises two important points:

1. If you are a book user using the [TeachBooks Template](../external/template/README.md) and/or the {ref}`Deploy Book Workflow <deploy-book-workflow-intro>`, your book is by default built with the `teachbooks` package, and the way your book is built and features that are included in the book may change automatically when it is updated (these will be non-breaking changes; if not, we will notify our mailing list).
2. If you are using the `jupyter-book` package to build your book, some of the features described in this Manual may not be available to you (i.e., those listed on this page). This will be the case if you are using a [setup described in the Jupyter Book Manual](https://jupyterbook.org/en/stable/publish/web.html), for example, [this GitHub workflow](https://jupyterbook.org/en/stable/publish/gh-pages.html).

For those who wish to use the package, it is available on [PyPI](https://pypi.org/project/teachbooks/) and can be installed using `pip install teachbooks`. As `teachbooks` is a wrapper, the package is meant to replace the usage of `jupyter-book` commands (although it does indeed add a few new commands to the CLI, e.g., `serve`). It is conventionally used in an identical way, as follows: 

```
teachbooks build book
```

### List of Features

Items in the list here are currently implemented in the TeachBooks package and described on other pages of this manual:
- [Draft-Release Workflow](./draft-release.md)
- [External Contents](./external_toc.md)
- [Local Server](./local_server.md) 

The package is also set up to handle [APA references](./apa) when using the Draft-Release Workflow (the `_ext` subdirectory and its contents are manually copied during the pre-build phase). This will not be necessary once the APA Reference feature is turned into a proper Sphinx extension or Pybtext plugin.

(deploy-book-workflow-intro)=
## Deploy Book Workflow

The [Deploy Book Workflow](../external/deploy-book-workflow/README.md) is by default incorporated into any book that has been created using the [TeachBooks Template](../external/template/README.md). We also strongly encourage anyone to consider this tool as an alternative to the "standard" workflow provided by Jupyter Book, as ours automatically builds a different version of your book for every branch in your respository, along with a number of settings that can be used to customize the build process and URL structure of your book(s). This tool is described in more detail on [the Deploy Book Workflow page of this manual](../external/deploy-book-workflow/README.md), and one should note that it influences a number of other aspects of a TeachBook.

### Related Features

A list of tools and features that are dependent on, or related to, the Deploy Book Workflow (DBW) is provided here:

Important for these features:
- [](../external/deploy-book-workflow/README.md): the main DBW page
- [](../external/template/README.md): books created from Template include DBW by default
- [](./draft-release.md): can be configured directly using the DBW
- [](./update_env.md): behaviors of this tool may influence the DBW
- {ref}`TeachBooks Python Package <teachbooks_package>`: included by default in the DBW
- [](./pull_request_build.md): created to provide DBW-like behavior for PR's from forked repositories
- [](./apa.md): a temporary fix is included in `teachbooks` to enable use in the DBW

### Environmnets and Caching

_Work in progress._