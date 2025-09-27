
(deploy-book-workflow-intro)=
## Deploy Book Workflow

The [Deploy Book Workflow](../external/deploy-book-workflow/README.md) is by default incorporated into any book that has been created using the [TeachBooks Template](../external/template/README.md). We also strongly encourage anyone to consider this tool as an alternative to the "standard" workflow provided by Jupyter Book, as ours automatically builds a different version of your book for every branch in your respository, along with a number of settings that can be used to customize the build process and URL structure of your book(s). This tool is described in more detail on [the Deploy Book Workflow page of this manual](../external/deploy-book-workflow/README.md), and one should note that it influences a number of other aspects of a TeachBook.

### Related Features

A list of tools and features that are dependent on, or related to, the Deploy Book Workflow (DBW) is provided here:

Important for these features:
- [](../external/deploy-book-workflow/README.md): the main DBW page
- [](../external/template/README.md): books created from the Template include DBW by default
- [](./draft-release.md): can be configured directly using the DBW
- [](./update_env.md): behaviors of this tool may influence the DBW
- {ref}`TeachBooks Python Package <teachbooks_package>`: included by default in the DBW
- [](./pull_request_build.md): created to provide DBW-like behavior for PR's from forked repositories
- [](./apa.md): a temporary fix is included in `teachbooks` to enable use in the DBW

### Book Build Commands

By default the DBW builds books using the following command:

```
teachbooks build book/
```

To use the [Draft-Release Workflow](./draft-release.md) with the Deploy Book Workflow the `BRANCHES_TO_PREPROCESS` variable must be configured for a specific branch, which will then execute the following command:

```
teachbooks build --release book/
```

### Environments and Caching

As described on the [DBW page](../external/deploy-book-workflow/README.md), there is a lot going on "under the hood" with regards to caching of GitHub Action artifacts. This can lead to undesired behavior when using the DBW, especially if package version numbers are not precisely defined. In general we expect the risk of this occurring to be low, as it should only happen when multiple branches are being actively used (new commits on each branch at least once per week), a package from the `requirements.txt` file is updated in the time between creation of two or more branches, and that package _also_ has a significant impact on the book building process. As the Python virtual environment cache is replaced by default if older than one week, the issue should resolve itself within that time frame.

Note that Specifying package version numbers explicitly and updating them via [Dependabot](./update_env.md) is an excellent way to ensure that environments in the DBW are always up to date and this issue is avoided.

If you are _not_ using Dependabot and are not able to get your packages updated when the DBW is running, delete the cache manually and rerun your GitHub Actions job (go to Actions tab, then looking for the "Caches" section under the "Management" pane on the left hand side of the screen).