"""Macros for the documentation."""

import pathlib
import re

import tomli

from mkdocs_macros.plugin import MacrosPlugin  # pyright: ignore[reportMissingTypeStubs]

HEADER_ONE_REGEX = re.compile(r"^#\s(.+)$", re.MULTILINE)
PAGE_REPLACEMENTS = {
    "index.md": (
        (" AFGs ", r" [AFGs](default:AFG) "),
        (" AWGs ", r" [AWGs](default:AFG) "),
        (" Scopes ", r" [Scopes](default:Scope) "),
        (" PSUs ", r" [PSUs](default:PSU) "),
        (" SMUs ", r" [SMUs](default:SMU) "),
        (" MTs ", r" [MTs](default:MT) "),
        (" DMMs ", r" [DMMs](default:DMM) "),
        (" DAQs ", r" [DAQs](default:DAQ) "),
        (" SSs ", r" [SSs](default:SS) "),
        (" PI ", " <PI:>"),
        (" TSP ", " <TSP:>"),
        (" API ", " <API:>"),
        (" DPOJET ", " <DPOJET:>"),
        (" ✅ ", " [](default:✅) "),
        (" 🚧 ", " [](default:🚧) "),
        (" ❌ ", " [](default:❌) "),
        (r"> \[!TIP\]", "!!! tip"),
        (
            "> Visit the [Glossary",
            "    Hover over a link or icon to see its definition, or visit the [Glossary",
        ),
        ("(https://tinyurl.com/tek-tm-devices/docs/glossary.md)", "(./glossary.md)"),
        ("(https://tinyurl.com/tek-tm-devices/CODE_OF_CONDUCT.md)", "(./CODE_OF_CONDUCT.md)"),
        ("(https://tinyurl.com/tek-tm-devices/CONTRIBUTING.md)", "(./CONTRIBUTING.md)"),
        ("(https://tinyurl.com/tek-tm-devices/LICENSE.md)", "(./LICENSE.md)"),
    ),
}


def define_env(env: MacrosPlugin) -> None:
    """Define variables, macros and filters.

    Notes:
        - variables: the dictionary that contains the environment variables
        - macro: a decorator function, to declare a macro.
        - filter: a function with one of more arguments,
            used to perform a transformation
    """
    # Read in the current package version number to use in templates and files
    with open(
        pathlib.Path(f"{pathlib.Path(__file__).parents[1]}") / "pyproject.toml", "rb"
    ) as file_handle:
        pyproject_data = tomli.load(file_handle)
        env.variables["package_version"] = "v" + pyproject_data["tool"]["poetry"]["version"]


def on_post_page_macros(env: MacrosPlugin) -> None:
    """Post-process pages."""
    if env.page.file.src_path in PAGE_REPLACEMENTS:  # pyright: ignore[reportUnknownMemberType]
        for search, replace in PAGE_REPLACEMENTS[env.page.file.src_path]:  # pyright: ignore[reportUnknownMemberType]
            env.markdown = env.markdown.replace(search, replace)  # pyright: ignore[reportUnknownMemberType]
    # Check if the title is correct
    if actual_title_match := HEADER_ONE_REGEX.search(env.markdown):  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
        actual_title = actual_title_match.group(1)
        if env.page.title != actual_title:  # pyright: ignore[reportUnknownMemberType]
            env.page.title = actual_title  # pyright: ignore[reportUnknownMemberType]
