# startify_directives_all.py
"""
Create a '-start' companion for every registered directive (class-based).

Rules:
  - Skip originals whose name already ends with '-start' or '-end'.
  - Skip if '<name>-start' already exists.
  - Class-based originals -> register a subclass calling original run().

Usage:
  extensions = ["startify_directives_all"]
"""

from __future__ import annotations
from docutils.nodes import Element
from typing import Iterator
import re
import copy
import importlib
import inspect
from typing import Callable, Dict, Iterable, List, Optional
from sphinx.transforms import SphinxTransform
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment

from sphinx.util import logging
logger = logging.getLogger(__name__)

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives as du_directives

SUFFIX_START = "-start"
SUFFIX_END = "-end"


# ---------------------------
# Helpers: identification
# ---------------------------

def _is_class_directive(obj) -> bool:
    return inspect.isclass(obj) and issubclass(obj, Directive)


# ---------------------------
# Helpers: registry access
# ---------------------------

def _get_unified_registry(app=None) -> Dict[str, object]:
    """
    Build a unified {name -> implementation} mapping of directives.

    Sources:
      1) docutils.parsers.rst.directives._directives  (loaded/added so far)
      2) docutils.parsers.rst.directives._directive_registry (lazy map of
         name -> (module, class) for builtins); import any missing ones.
      3) Sphinx app.registry (if provided) for extension-registered directives
    """
    # 1) Already-loaded directives (includes Sphinx & extensions registered via add_directive)
    unified: Dict[str, object] = dict(getattr(du_directives, "_directives", {}))

    # 2) Ensure Docutils built-ins are present by importing from _directive_registry
    reg = getattr(du_directives, "_directive_registry", {})
    for name, (modname, clsname) in reg.items():
        if name in unified:
            continue
        try:
            mod = importlib.import_module(f"docutils.parsers.rst.directives.{modname}")
            obj = getattr(mod, clsname, None)
            if obj is not None:
                unified[name] = obj
        except Exception:
            # Be defensive: if an import fails, just skip that name
            continue

    # 3) Add Sphinx's registry if app is provided
    if app is not None:
        # Sphinx stores directives in app.registry
        # Try different ways to access the directives mapping
        if hasattr(app.registry, 'directives'):
            # Newer Sphinx versions may have a directives attribute
            try:
                unified.update(app.registry.directives)
            except (AttributeError, TypeError):
                pass
        
        # Also check for domains which contain directives (e.g., prf:theorem from sphinx-proof)
        if hasattr(app.registry, 'domains'):
            for domain_name, domain_cls in app.registry.domains.items():
                try:
                    # Instantiate domain or use class attributes
                    if hasattr(domain_cls, 'directives'):
                        domain_directives = domain_cls.directives
                        for dir_name, dir_impl in domain_directives.items():
                            # Fully qualified name: domain:directive
                            full_name = f"{domain_name}:{dir_name}"
                            if full_name not in unified:
                                unified[full_name] = dir_impl
                except Exception:
                    continue

    return unified


# ---------------------------
# Helpers: class generation
# ---------------------------

def _copy_option_spec(option_spec):
    return copy.copy(option_spec) if isinstance(option_spec, dict) else option_spec

def make_startified_class(
    orig_name: str,
    base_cls: type[Directive],
) -> type[Directive]:
    """
    Subclass `base_cls` to call original run().
    """
    attrs = {}
    for attr in (
        "required_arguments",
        "optional_arguments",
        "final_argument_whitespace",
        "has_content",
        "option_spec",
    ):
        if hasattr(base_cls, attr):
            val = getattr(base_cls, attr)
            if attr == "option_spec":
                attrs[attr] = _copy_option_spec(val) or {}
            else:
                attrs[attr] = val

    def run(self: Directive):
        current_name = self.name
        self.name = orig_name  # temporarily set to original for base run()
        children = base_cls.run(self)
        self.name = current_name  # restore
        if not isinstance(children, list):
            if isinstance(children, Iterable):
                children = list(children)
            else:
                children = [children]
        # create a start_node and add all result nodes as its children
        start_node_instance = start_node()
        start_node_instance += children
        result = [start_node_instance]

        # Get environment from state.document.settings
        env = getattr(self.state.document.settings, "env", None)
        if env is not None:
            docname = env.docname
            # # 1) Check whether main registry is already created, if not, create it
            # if not hasattr(env, "sphinx_gated_directives_registry"):
            #     env.sphinx_gated_directives_registry = {}
            # # 2) Check whether a sub-registry for current directive type is already created, if not, create it
            # if orig_name not in env.sphinx_gated_directives_registry:
            #     env.sphinx_gated_directives_registry[orig_name] = {}
            # # 3) Register current usage in the registry for this doc and this type
            # gated_registry = env.sphinx_gated_directives_registry[orig_name]
            # if docname not in gated_registry:
            #     gated_registry[docname] = {
            #         "start": [],
            #         "end": [],
            #         "sequence": [],
            #         "msg": [],
            #     }
            # gated_registry[docname]["start"].append(self.lineno)
            # gated_registry[docname]["sequence"].append("S")
            # gated_registry[docname]["msg"].append(
            #     f"{self.name} at line: {self.lineno}"
            # )
            # 4) Check whether super registry has been created, if not, create it
            if not hasattr(env, "sphinx_gated_directives_super_registry"):
                env.sphinx_gated_directives_super_registry = {}
            # 5) Register current usage in the super registry
            super_registry = env.sphinx_gated_directives_super_registry
            if docname not in super_registry:
                super_registry[docname] = {
                    "start": [],
                    "end": [],
                    "sequence": [],
                    "msg": [],
                    "type": [],
                }
            super_registry[docname]["start"].append(self.lineno)
            super_registry[docname]["sequence"].append("S")
            super_registry[docname]["msg"].append(
                f"{self.name} at line: {self.lineno}"
            )
            super_registry[docname]["type"].append(orig_name)

        return result

    attrs["run"] = run
    new_cls_name = f"{base_cls.__name__}_Start_For_{orig_name.replace(':', '_')}"
    return type(new_cls_name, (base_cls,), attrs)

def make_endified_class(
    orig_name: str,
    base_cls: type[Directive],
) -> type[Directive]:
    """
    Just create a subclass to obtain an end node.
    """
    attrs = {}
    for attr in (
        "required_arguments",
        "optional_arguments",
        "final_argument_whitespace",
        "has_content",
        "option_spec",
    ):
        if hasattr(base_cls, attr):
            val = getattr(base_cls, attr)
            if attr == "option_spec":
                attrs[attr] = _copy_option_spec(val) or {}
            else:
                attrs[attr] = val

    def run(self: Directive):

        # Get environment from state.document.settings
        env = getattr(self.state.document.settings, "env", None)
        if env is not None:
            docname = env.docname
            # # 1) Check whether main registry is already created, if not, create it
            # if not hasattr(env, "sphinx_gated_directives_registry"):
            #     env.sphinx_gated_directives_registry = {}
            # # 2) Check whether a sub-registry for current directive type is already created, if not, create it
            # if orig_name not in env.sphinx_gated_directives_registry:
            #     env.sphinx_gated_directives_registry[orig_name] = {}
            # # 3) Register current usage in the registry for this doc and this type
            # gated_registry = env.sphinx_gated_directives_registry[orig_name]
            # if docname not in gated_registry:
            #     gated_registry[docname] = {
            #         "start": [],
            #         "end": [],
            #         "sequence": [],
            #         "msg": [],
            #     }
            # gated_registry[docname]["end"].append(self.lineno)
            # gated_registry[docname]["sequence"].append("E")
            # gated_registry[docname]["msg"].append(
            #     f"{self.name} at line: {self.lineno}"
            # )
            # 4) Check whether super registry has been created, if not, create it
            if not hasattr(env, "sphinx_gated_directives_super_registry"):
                env.sphinx_gated_directives_super_registry = {}
            # 5) Register current usage in the super registry
            super_registry = env.sphinx_gated_directives_super_registry
            if docname not in super_registry:
                super_registry[docname] = {
                    "start": [],
                    "end": [],
                    "sequence": [],
                    "msg": [],
                    "type": [],
                }
            super_registry[docname]["end"].append(self.lineno)
            super_registry[docname]["sequence"].append("E")
            super_registry[docname]["msg"].append(
                f"{self.name} at line: {self.lineno}"
            )
            super_registry[docname]["type"].append(orig_name)

        # return []
        # next line should be good enough, but raises an error as not all has been implemented
        # maybe we need end nodes per directive type?
        return [end_node()]

    attrs["run"] = run
    new_cls_name = f"{base_cls.__name__}_End_For_{orig_name.replace(':', '_')}"
    return type(new_cls_name, (base_cls,), attrs)

# ---------------------------
# Core logic
# ---------------------------

def _should_skip_name(orig_name: str) -> bool:
    return orig_name.endswith(SUFFIX_START) or orig_name.endswith(SUFFIX_END)

def _register_startified_directives(app, env, docnames):
    unified = _get_unified_registry(app)
    snapshot_names = set(unified.keys())
    added = 0

    for orig_name, obj in sorted(unified.items()):
        if _should_skip_name(orig_name):
            continue

        new_name = f"{orig_name}{SUFFIX_START}"
        if new_name in snapshot_names:
            continue

        try:
            if _is_class_directive(obj):
                start_cls = make_startified_class(orig_name, obj)
                app.add_directive(new_name, start_cls)
                end_cls = make_endified_class(orig_name, Directive) # because it does generate anything, most simple directive
                app.add_directive(f"{orig_name}{SUFFIX_END}", end_cls)
                added += 1
            else:
                logger.debug(f"[startify] '{orig_name}' is not a class directive; skipping.")
        except Exception as e:
            logger.warning(f"[startify] failed to register '{new_name}': {e}")

def setup(app):

    # register function to perge registries at start of build per document
    app.connect("env-purge-doc", purge_registries)
    
    # At the latest possible moment, register startified directives (also creates the endified ones)
    app.connect("env-before-read-docs", _register_startified_directives,priority=10000000000000000000000000000)

    # Register nodes, used as placeholder for end directives
    # will be resolved in the transforms to something meaningful
    # during merging of start-end blocks
    app.add_node(start_node)
    app.add_node(end_node)

    # Register a transform to check validity of start-end pairs
    app.add_transform(CheckGatedDirectivesTransform)

    # Register a transform to merge start-end pairs into gated content
    app.add_transform(MergeGatedDirectivesTransform)

    return {
        "version": "1.0",
        "parallel_read_safe": True,
    }

# Node classes for start and end directives

class start_node(nodes.Admonition, nodes.Element):
    pass

class end_node(nodes.Admonition, nodes.Element):
    pass

# purge_registry
def purge_registries(app: Sphinx, env: BuildEnvironment, docname: str) -> None:

    # only perge if needed
    # if hasattr(env, "sphinx_gated_directives_registry"):
    #     registry = env.sphinx_gated_directives_registry
    #     for directive_name in registry:
    #         if docname in registry[directive_name]:
    #             del registry[directive_name][docname]
    if hasattr(env, "sphinx_gated_directives_super_registry"):
        super_registry = env.sphinx_gated_directives_super_registry
        if docname in super_registry:
            del super_registry[docname]

# Transform to check validity of start-end pairs
class CheckGatedDirectivesTransform(SphinxTransform):
    default_priority = 1

    def apply(self, **kwargs):
        env = self.env
        # if not hasattr(env, "sphinx_gated_directives_registry"):
        #     return
        if not hasattr(env, "sphinx_gated_directives_super_registry"):
            return
        
        # First check the super registry for a correct structure
        # demands:
        # 1) equal number of start and end directives
        # 2) no nesting of start-end pairs (so SSEE is not allowed, only SESE)
        super_registry = env.sphinx_gated_directives_super_registry
        error = False
        docname = self.env.docname
        if docname in super_registry:
            start = super_registry[docname]["start"]
            end = super_registry[docname]["end"]
            structure = "\n  ".join(super_registry[docname]["msg"])
            sequence = "".join(super_registry[docname]["sequence"])
            groups = re.findall("(SE)", sequence)
            if len(start) > len(end):
                msg = f"The document {docname} contains more start directives than end directives:\n  {structure}\nPlease ensure each start directive has a corresponding end directive."
                logger.error(msg)
                error = True
            elif len(end) > len(start):
                msg = f"The document {docname} contains more end directives than start directives:\n  {structure}\nPlease ensure each end directive has a corresponding start directive."
                logger.error(msg)
                error = True
            # at this point, len(start) == len(end)
            elif len(groups) != len(start) or len(groups) != len(end):
                msg = f"The document {docname} contains nested start and end directives:\n  {structure}\nThis is not allowed. Please correct the nesting."
                logger.error(msg)
                error = True
            else:
                # At this point, every start is followed by an end.
                # Now check that types match in order.
                types = super_registry[docname]["type"]
                start_type = types[::2]
                end_type = types[1::2]
                for i in range(len(start_type)):
                    if start_type[i] != end_type[i]:
                        msg = f"The document {docname} contains mismatched start and end directives at lines {start[i]} and {end[i]}:\n  {structure}\nPlease ensure that start and end directives match in type."
                        logger.error(msg)
                        error = True

        if error:
            raise Exception(f"[sphinx-gated-directives] An error has occurred when parsing gated directives in {docname}.\nPlease check warning messages above.")
        
        # no check per directive type is needed if no error in super registry is raised,
        # as the super registry already ensures correctness for each type.
        # if nesting is allowed in the future, this part needs to be re-implemented.
        
        
class MergeGatedDirectivesTransform(SphinxTransform):
    default_priority = 10

    def apply(self, **kwargs):
        env = self.env
        # Something to do here
        # idea:
        # 1) Find all start_nodes
        # 2) for each start_node, find the corresponding end_node (i.e. next end_node)
        # 3) collect all nodes in between
        # 4) Take the first node after start_node, and add all other collected nodes as its children
        if not hasattr(env, "sphinx_gated_directives_super_registry"):
            return
        super_registry = env.sphinx_gated_directives_super_registry
        docname = self.env.docname
        if docname not in super_registry:
            return
        
        # Each start-end pair is valid (checked before), so we can proceed to merge
        # find all start nodes, as an iterator
        # for each start node, find the next end node within the parent of start node
        start_nodes = findall(self.document, start_node)
        for start_n in start_nodes:
            parent = start_n.parent
            # find the next end_node after start_n in parent
            found_start = False
            end_n = None
            for child in parent.children:
                if child is start_n:
                    found_start = True
                elif found_start and isinstance(child, end_node):
                    end_n = child
                    break
            if end_n is None:
                continue  # should not happen due to prior checks

            # collect all nodes between start_n and end_n
            start_index = parent.children.index(start_n)
            end_index = parent.children.index(end_n)
            between_nodes = parent.children[start_index + 1:end_index]

            # We have to merge, but how is the question.
            # we handle based on "experience" and "observation" of what kind of nodes are generated
            # step 1: create a new container node to hold the merged content
            # content of start_node
            new_nodes = start_n.children
            # add content in between, depending on content in start_n
            if between_nodes:
                has_section = False
                has_caption = False
                si = -1
                content = new_nodes[-1]  # we assume that the last child of start_n holds the main content
                for sn in content.children:
                    si += 1
                    if isinstance(sn, nodes.section):
                        has_section = True # So probably a topic or similar (from sphinx-proof)
                        section_index = si
                        section_node = sn
                        break
                    elif isinstance(sn, nodes.caption):
                        has_caption = True # So probably a figure or similar
                        caption_index = si
                        caption_node = sn
                        break
                if has_section:
                    # if there are sections, we add all between nodes to this section
                    content[section_index] += between_nodes
                elif has_caption:
                    # if there is a caption, we add all between nodes before the caption
                    n = len(content.children)
                    pos = n - 1
                    for i, bn in enumerate(between_nodes):
                            content.insert(pos + i, bn)  # insert sets parent/doc links
                else:
                    # otherwise, we add all between nodes to the main content directly\
                    for bn in between_nodes:
                        content += bn  # add sets parent/doc links
                    
            # finally, replace start_n with new_nodes, and remove end_n and between_nodes
            start_pos = parent.children.index(start_n)
            # remove end_n
            parent.remove(end_n)
            # remove start_n
            parent.remove(start_n)
            # remove between_nodes
            for bn in between_nodes:
                parent.remove(bn)
            # insert new_nodes at start_pos
            for i, nn in enumerate(new_nodes):
                parent.insert(start_pos + i, nn)  # insert new structure


def findall(node: Element, *args, **kwargs) -> Iterator[Element]:
    # findall replaces traverse in docutils v0.18
    # note a difference is that findall is an iterator
    impl = getattr(node, "findall", node.traverse)
    return iter(impl(*args, **kwargs))