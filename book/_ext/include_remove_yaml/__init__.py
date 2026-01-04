from __future__ import annotations
from sphinx.util import logging
logger = logging.getLogger(__name__)

def _strip_yaml(lines: list[str]) -> list[str]:

    if not lines:
        return lines
    for ix,lines_set in enumerate(lines):
        new_lines = lines_set.splitlines()
        if new_lines[0].strip() != "---":
            continue
        # yaml front matter detected
        # find closing delimiter
        index_end = 1
        for i in range(1, len(new_lines)):
            tok = new_lines[i].strip()
            if tok == "---":
                index_end = i
                break
        new_lines = new_lines[index_end+1 :]
        lines[ix] = "\n".join(new_lines)
    return lines  # no closing delimiter -> leave unchanged

def on_include_read(app, docname, path, content):
    # content is a list[str]; modify in-place
    new = _strip_yaml(content)
    if new is not content:
        content[:] = new

def setup(app):
    app.connect("include-read", on_include_read)
    return {}
