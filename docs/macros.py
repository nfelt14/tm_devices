"""Macros for the documentation."""

from mkdocs_macros.plugin import MacrosPlugin  # pyright: ignore[reportMissingTypeStubs]

PAGE_REPLACEMENTS = {
    "tm_devices: Test & Measurement Device Management": (
        # TODO: update plural device types to include the "s" when
        #  https://github.com/realtimeprojects/mkdocs-ezglossary/issues/9 is fixed
        (" AFGs ", " <AFG:> "),
        (" AWGs ", " <AWG:> "),
        (" Scopes ", " <Scope:> "),
        (" PSUs ", " <PSU:> "),
        (" SMUs ", " <SMU:> "),
        (" MTs ", " <MT:> "),
        (" DMMs ", " <DMM:> "),
        (" DAQs ", " <DAQ:> "),
        (" SSs ", " <SS:> "),
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
    if env.page.title in PAGE_REPLACEMENTS:  # pyright: ignore[reportUnknownMemberType]
        for search, replace in PAGE_REPLACEMENTS[env.page.title]:  # pyright: ignore[reportUnknownMemberType]
            env.markdown = env.markdown.replace(search, replace)  # pyright: ignore[reportUnknownMemberType]
