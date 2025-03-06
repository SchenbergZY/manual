(teachbooks-package)=
# Pre- and postprocessing book

```{admonition} User types
:class: tip
This page is useful for all users to understand how the book building process works and can be influenced, although the implementation is likely going to be carried out by User Types 3, 4 or 5.
```

{bdg-secondary}`Python Package: teachbooks`

The package is a CLI tool that primarily provides a wrapper around the Jupyter Book package which is used for pre- and postprocessing. In this case "wrapper" refers to the CLI usage: CLI commands generally invoke `jupyter-book` commands internally; the `jupyter-book` package is _not_ distributed within the `teachbooks` package.

The source code and function of the package will eventually be documented on a Sphinx-built website ([teachbooks.io/TeachBooks/](https://teachbooks.io/TeachBooks/)), however, this is currently still under construction.

## Primary Features

Key features (described in the sections below) include:
- pre- and post-processing steps for the Jupyter Book package
- Draft-Release Workflow (`teachbooks build --release book`)
- Start and stop a local server to check your book (`teachbooks serve`)

This list will be updated periodically as features are added. Check the [Release Notes](https://github.com/TeachBooks/TeachBooks/releases) in the GitHub repository for the most up-to-date information.

## Installation

The package is currently only [available on PyPI](https://pypi.org/project/teachbooks/) and can be installed as follows:

```
pip install teachbooks
```

The first stable release (`v1.0.0`) is expected to be released in Spring 2025. Until then the package is very much useable but will be updated frequently. Therefore, get in the habit of updating the package regularly:

```bash
pip install --upgrade teachbooks
```

We recommend you install this in an environment that is specifically dedicated for building books. Python virtual environments are a good way to manage this and would be consistent with what is used by the GitHub servers via the {ref}`Deploy Book Workflow <deploy-book-workflow>`. However, if you use non-Python tools to edit and check your book, a Conda environment may be a better choice.

## Contribute

This tool's repository is stored on [GitHub](https://github.com/TeachBooks/TeachBooks). The `README.md` of the repository describes how you can contribute---don't hesitate to make an issue if you would like to request new features!

## Description of Features

(teachbooks-pre-post)=
### Jupyter Book Pre- and Post-Processing

Using the teachbooks CLI in the book building process generally invokes Jupyter Book. Many of the features in this package are then invoked in the stages before and after this command. The process generally includes the following steps:

1. Edit source code and prepare to build a book
2. Execute `teachbooks [OPTIONS] COMMAND [ARGS]`
3. Pre-processing step: carried out by `teachbooks`
4. Build step: book is built using `jupyter book [OPTIONS] COMMAND [ARGS]`
5. Post-processing step: carried out by `teachbooks`

Additional options like those used in jupyterbook (`--all` for example) can be used with `teachbooks` in an identical usage as with the `jupyter-book` command.

```{note}
The pre- and post-processing steps have not yet bet formally defined; they only exist implicitly in the source code for the `build` CLI command. If you are interested in suggesting a feature or contributing to the package, please visit the [GitHub repository](https://github.com/teachbooks/teachbooks) and take a look at the Discussions and Issues. For example, [this one](https://github.com/orgs/TeachBooks/discussions/28).
```

(teachbooks-draft-release)=
### Draft-Release Workflow

Often it is necessary to prepare, review and edit materials in parallel to material that is currently being used by students, or another target audience. This workflow enables an author to easily maintain separate versions of a book without having to repeatedly comment out lines of a table of contents or page when building different versions. It is also easy to implement in CI/CD settings (it is already implemented in the {ref}Deploy Book Workflow <deploy-book-workflow>`, which builds our TeachBooks).

```{admonition} Why is this useful?
:class: tip

Consider a case where you have been using two branches to develop and maintain a book: `release` (shared with students) and `draft` (shared with colleagues to review contents before release). You are probably also using other branches to develop contents, but rely on the `draft` branch as a way to collect the "finalized-but-not-yet-released" material. Things go smoothly as long as you add pages to the `draft` branch one at a time, then merge the branch into `release` as they are needed.

But what happens when you have 2 pages: one is ready to share with students, but the other is still being reviewed by your colleague. The only way to get the proper page into release is to comment the undesired page in the ToC using a commit on `draft`, merge the commit into `release`, then uncomment the ToC in a new commit on `draft`. This is very tedious, and prone to error as there it is not straightforward to tell which pages are available in the `draft` versus `release` books!

The Draft-Release workflow solves this problem by using commented tags to clearly denote which pages are available in the `draft` book and which are left out of the `release` book.
``` 

The workflow is enabled by a `teachbooks` CLI feature that identifies and removes any lines from the files `_config.yml` and `_toc.yml` file that are surrounded by `REMOVE-FROM-RELEASE` tags.

For example, pages in a developed book (e.g., `draft` branch) can be manually stripped out of the table of contents when a merge request from `draft` to `release` is made. This prevents the page being included in the released book. Pages marked with this feature are still visible in the `draft` book. Lines tagged in the configuration file `_config.yml` can be used in exactly the same manner. The tag is applied as follows:

```
format: jb-book
root: intro

parts:
  - caption: ...
    chapters: 
    - file: ...
      ...
# START REMOVE-FROM-PUBLISH
    - file: files_to_remove
# END REMOVE-FROM-PUBLISH
```

There is no limit to the number of stripped sections, they can be sequential and indentation does not matter.

To invoke the tag and remove content during the book build process, use the following optional argument when building the book with the `teachbooks` package:

```
teachbooks build --publish book
```

Note that `teachbooks build book` would build a book without stripping the tagged lines, just as `jupyter-book build book` would. This is called "draft mode" and is the default behavior. You can recognize it in the stdout after running the `build` command:

```bash
TeachBooks: running build with strategy 'draft'
```

(teachbooks-serve)=
### Local Python server

```{tip}
Visit the {ref}`Local Server page <setup-local-server>` for an explanation of why you need a local server.
```

The TeachBooks Python package includes a command line interface (CLI) that can be used to start a local server:

```bash
teachbooks serve
```
By default it assumes you have a book in `./book/`, are running the command from the root `./` of your repository and will serve `./book/_build/html`. If not, it will serve the repository root. You can also specify the directory to serve:

```bash
teachbooks serve path unconventional_book_dir/_build/html
```

```{tip}
Remember that the browser is serving static files provided by the local server and does not always keep track when they are updated. 

You should reload the page if you are editing and rebuilding the book. You can try `CTRL+R` `ctrl`+`F5`. If this does not work, on Chrome try right-clicking somewhere on the page, select \"Inspect\", open the \"Network\" tab, then reload with `CTRL+R`.
```

To stop the server, simply run

```bash
teachbooks serve stop
```

The CLI tool is set up to make the book edit and check workflow as easy as possible locally:
- you can rebuild the book without restarting the server.
- it reuses an existing server if already running.
- it prints the URL where the book is served after building the book to easily access it by clicking the link in standard output.
- the `teachbooks serve stop` command prevents Python processes running in the backgroudn and slowing down your computer (it saves the server state in a pickle file). 