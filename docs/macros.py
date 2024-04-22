"""Macros for the documentation."""

import re

from mkdocs_macros.plugin import MacrosPlugin  # pyright: ignore[reportMissingTypeStubs]

HEADER_ONE_REGEX = re.compile(r"^#\s(.+)$", re.MULTILINE)
PAGE_REPLACEMENTS = {
    "index.md": (
        (" AFGs ", r" <AFG:\|AFGs> "),
        (" AWGs ", r" <AWG:\|AWGs> "),
        (" Scopes ", r" <Scope:\|Scopes> "),
        (" PSUs ", r" <PSU:\|PSUs> "),
        (" SMUs ", r" <SMU:\|SMUs> "),
        (" MTs ", r" <MT:\|MTs> "),
        (" DMMs ", r" <DMM:\|DMMs> "),
        (" DAQs ", r" <DAQ:\|DAQs> "),
        (" SSs ", r" <SS:\|SSs> "),
        (" PI ", " <PI:>"),
        (" TSP ", " <TSP:>"),
        (" API ", " <API:>"),
        (" DPOJET ", " <DPOJET:>"),
        # FUTURE # (" ✅ ", " <✅:>"),
        # FUTURE # (" 🚧 ", " <🚧:>"),
        # FUTURE # (" ❌ ", " <❌:>"),
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


def define_env(env: MacrosPlugin) -> None:  # noqa: ARG001
    """Define variables, macros and filters.

    Notes:
        - variables: the dictionary that contains the environment variables
        - macro: a decorator function, to declare a macro.
        - filter: a function with one of more arguments,
            used to perform a transformation
    """


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
