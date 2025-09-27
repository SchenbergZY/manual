````{margin}
```{admonition} User types
:class: tip
This section is useful for user type 3-5.
```

{bdg-link-light}`GitHub Reusable Action: Deploy Book workflow <https://teachbooks.io/manual/favourites/external/deploy-book-workflow/README.html>`
{bdg-link-light}`Part of TeachBooks Template <https://teachbooks.io/manual/favourites/external/template/README.html>`

````

# Write book fully in GitHub interface

Using the GitHub tooling in combination with TeachBook's software, users are able to write their book fully online, without the need to install any software locally. This is especially useful for users that are not familiar with Git and GitHub, or do not have the rights to install software on their computer. To make this possible, users can start with the [TeachBooks Template](https://teachbooks.io/manual/favourites/external/template/README.html) after which they make use of the [Deploy Book Workflow](https://teachbooks.io/manual/favourites/external/deploy-book-workflow/README.html) to automatically build and release their book online.

## How to do this

New users can start writing their book by following the steps shown in the [TeachBooks Template repository](https://github.com/TeachBooks/template).

Users who already have a TeachBook repository can add the Deploy Book Workflow as explained [here](https://teachbooks.io/manual/favourites/external/deploy-book-workflow/README.html)

After that, users can start writing and editing their book fully online in the GitHub interface. This is supported with:
- [Automatic book builds for all version](https://teachbooks.io/manual/favourites/external/deploy-book-workflow/README.html)
- A summary describing where the TeachBook is released, errors in the build process per branch and how the release step is configured

## Example of summary

Whenever the workflow is triggered, its progress and a summary can be seen under the <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path></svg>`Actions`- `All workflows` -  `call-deploy-book` in GitHub! It shows you a descriptive summary. This summary includes, among others:
- Errors in the build process 

Here's an example for a summary for the template book:

> ### Branches deployed
> | Branch 🎋 | Link 🔗 | Build status ☑️ |
> | :--- | :--- | :--- |
> | main | [https://teachbooks.github.io/template/main](https://teachbooks.github.io/template/main) | ✅ `Released` |
> | version2 | [https://teachbooks.github.io/template/version2](https://teachbooks.github.io/template/version2) | 🔴 `Build failed [1]` |
> | version3 | [https://teachbooks.github.io/template/version3](https://teachbooks.github.io/template/version3) | ⭕ `Build failed [2]` |
> 
> #### Legend for build status
> ✅ `Released` - build success, new version released.
>
> 🔴 `Build failed [1]` - build failure, previous version of the book reused.
>
> ⭕ `Build failed [2]` - build failure, no previous version reused.
>
> ### Preview of build errors & warnings
> For more details please see the corresponding `build-books` jobs in the left pane.
>
> On branch `version2`:
> ```
> �[91m/home/runner/work/template/template/book/some_content/overview.md:5: WARNING: Non-consecutive header level increase; H1 to H3 [myst.header]�[39;49;00m
> ``` 
>
> On branch `version3`:
> ```
> /home/runner/work/_temp/ff8c8325-8d8b-4c0b-a2b2-32d2169c55bc.sh: line 8: teachbooks: command not found
> ```
>

## Exercise
Check out [the exercises](https://teachbooks.io/template/exercises.html) in the TeachBooks template to see for yourself how you can write and edit your book fully online in GitHub!
