# TeachBooks versioning with changelog

Versions combined with a changelog can be a very effective way to communicate book changes to the reader and allow reuse of specific versions. We recommend [TeachBooks versioning](../features/versioning.md), which comes in two flavors:

1. `academic_year.additions.errata` versioning for books tailed-made for courses in which content is added / adapted during the course and might be restructured extensively every year while remaining to be available in the original form. An example can be seen in [the source repository of the Engineering Systems Optimization book](https://github.com/TUDelft-books/CME4501/tags) showing tags for different versions.
2. `major.errata` versioning for books which are more stable over years, in which big changes are covered only by the version number.

The details of TeachBooks versioning are covered [here](../features/versioning.md)

## Changelog
To communicate changes, we advise creating a changelog in the book. The [template](https://github.com/TeachBooks/template/blob/main/book/changelog.md) contains an empty changelog to fill:

```md
# Changelog

## `<latest version>`: `<date>`
- `<Added/modified/deleted>` [](`<relative link to changed file>`)
- ...
- Full Changelog: `[<previous version>...<current version>](<link to diff as provided by GitHub>)'

## `<previous version>`: <...>
- <...>

<...>
```

An example can be found [here](https://ciem5000-2025.github.io/book/changelog.html)

## Note on version change on page
When making errata changes or additions, it's advised to notify the reader not only in the changelog, but also on the relevant pages. You can do so using the `versionadded` and `versionchanged` admonitions:

```md
::::::{versionchanged} <version_number> <date of version release>
<explanation of change on current page>
::::::
```

and

```md
::::::{versionadded} <version_number> <date of version release>
<explanation of addition on/of current page>
::::::
```

Leads to for example:
::::::{versionchanged} v2025.3.5 2025-02-23
TeachBooks versioning added
::::::

An example can be found [here](https://oit.tudelft.nl/CME4501/2024/pages/linear_constrained_optimization_class.html)

## Implement tags and releases
Tags can be added to your source code by adding the version number as a tag to a specific commit.

You can do so in GitHub when creating a new release (on the `Code` page of your repository.) There, you can enter a name for your tag and select one of your branches or recent commits:

```{figure} figures/tags_github.png
---
width: 500px
align: center
---

```

Locally, you can do so in GitHub Desktop by clicking 'Create Tag...` for a specific commit in the History tab.

```{figure} figures/tags.png
---
width: 500px
align: center
---

```

Once the tags is pushed to GitHub/GitLab. You can create a release of the version by clicking `Release` on the `Code` page of your repository. There you can select a tag and generate release notes.

It's recommended to add the relevant part of the changelog to the release notes on GitHub. An example can be found [here](https://github.com/CIEM5000-2025/book/releases/tag/v2025.2.0)


