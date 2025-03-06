(setup-local-server)=
# Local Server to view interactive elements locally

```{admonition} User types
:class: tip
This section is useful for user type 4-5.
```

{bdg-secondary}`Python Package: teachbooks`

Perhaps you have already noticed that when building a book and testing it locally on your computer, some features do not work the way you expect, or worse---do not work at all! This is because many interactive features rely on browser functionality to work properly, for example: Grasple/H5p iframe exercises, Sphinx-Thebe Python interactivity and HTML/Javascript elements. Although the website is _static_ (i.e., there is no code running on a webserver that generates the content), modern web browsers have their own internal computing environments that run processes to deliver the rich content we desire in our books.

Technically what is needed to facilitate this during the editing and checking of your book locally is a **static web server** that can serve the files in the `./book/_build/html` directory of your book (this subdirectory is created as a result of the command `build book`). We refer to this as a **local server** because it is running on your local machine.

```{admonition} Why do you need a local server?
:class: tip

A Jupyter Book is really just a _static website._ This means that all book content _and interactivity_ is available via the (static) files that are provided to you by a webserver when you visit a specific URL. After this initial request, all required files are available in your web browser, however, some features require the request and response protocol to work properly. 
```

We recommend you use the **TeachBooks Python Package**, which has a `serve` command in the CLI tool to start and stop local servers. Find out more on {ref}`the TeachBooks Package page <teachbooks-serve>`.

This page presents just a few additional examples that are used by TeachBooks collaborators. There are many more options available out there, for example, [this list illustrates many servers that can be activated with a single line of code!](https://gist.github.com/willurd/5720255).

```{tip}
Remember that the browser is serving static files provided by the local server and does not always keep track when they are updated. 

You should reload the page if you are editing and rebuilding the book. You can try `CTRL+R` `ctrl`+`F5`. If this does not work, on Chrome try right-clicking somewhere on the page, select \"Inspect\", open the \"Network\" tab, then reload with `CTRL+R`.
```

## TeachBooks Server: `teachbooks serve`

If you have the TeachBooks Python package installed (`pip install teachbooks`), starting a server is as simple as:

```bash
teachbooks serve
```

See the {ref}`TeachBooks Package page <teachbooks-serve>` for additional guidance on using the CLI tool.

## Live Server: a VS Code Extension

A local server is easy to initialize directly in VS Code using the Live Server extension. Once installed, it can be activated with a "Go Live" button in the bottom right corner of VS Code. The extension will automatically serve index.html, so depending on your book build settings you may need to navigate to the correct directory/file manually using the URL address in the browser.

````{admonition} Install Live Serve Extension
:class: tip

You can install this extension by searching for `Live Server` (or even easier, extension ID `ritwickdey.LiveServer`)in the Visual Studio Code extensions marketplace.

```{figure} https://github.com/ritwickdey/live-server-web-extension/raw/master/img/icon.png
---
width: 10%
name: live-server-icon
```
````


## Python Server: `python -m http.server`

The Python standard library has a built-in server that can be activated from the command line. This is a simple way to serve a book locally  

```
python -m http.server
```

If you don't mind typing a bit more, you can specify the port number and the directory to serve:

```
python -m http.server 8000 --directory book/_build/html
```

This is actually what the `teachbooks serve` command is using, but there we have added additional features to make the process more user-friendly for the book edit and check workflow.

### Stopping the Python Server

It can be challenging to stop the Python server, especially when using Windows OS. Even though you may force end the process (e.g., with `CMD+C`), the server may still be running in the background.

For Mac and Linux users (or for Windows if you have Git Bash installed or another Unix-type terminal), you can try this:

```bash 
pid=$(ps aux | grep http.server | head -n 1 | awk '{ print $2 }')
kill -9 $pid
```

Or this:

```bash
tskill python
```

A Windows-specific command for the CMD prompt or Powershell is:

```
TASKKILL /IM python.exe /F
```