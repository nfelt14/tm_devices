"""The alias commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO2, MSO5K,
MSO5KB, MSO70KC, MSO70KDX, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ALIas {ON|OFF|<NR1>}
    - ALIas:CATalog?
    - ALIas:DEFine <QString><,>{<QString>|<Block>}
    - ALIas:DEFine?
    - ALIas:DELEte <QString>
    - ALIas:DELEte:ALL
    - ALIas:DELEte:NAMe <QString>
    - ALIas:STATE {ON|OFF|<NR1>}
    - ALIas:STATE?
    - ALIas?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AliasState(SCPICmdWrite, SCPICmdRead):
    """The ``ALIas:STATE`` command.

    Description:
        - This command turns aliases on or off and is identical to the ALIAS command. The query form
          of this command returns the state of the aliases.

    Usage:
        - Using the ``.query()`` method will send the ``ALIas:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ALIas:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ALIas:STATE value`` command.

    SCPI Syntax:
        ```
        - ALIas:STATE {ON|OFF|<NR1>}
        - ALIas:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 turns off aliases; any other value turns on aliases.
        - ``OFF`` turns alias expansion off.
        - ``ON`` turns alias expansion on. When a defined alias is received, the specified command
          sequence is substituted for the alias and executed.
    """


class AliasDeleteName(SCPICmdWrite):
    """The ``ALIas:DELEte:NAMe`` command.

    Description:
        - This command removes a specified alias. An error message is generated if the named alias
          does not exist. This command is identical to ``ALIas:DELEte``.

    Usage:
        - Using the ``.write(value)`` method will send the ``ALIas:DELEte:NAMe value`` command.

    SCPI Syntax:
        ```
        - ALIas:DELEte:NAMe <QString>
        ```

    Info:
        - ``<QString>`` is the name of the alias to remove. Using <QString> must be a previously
          defined alias.
    """

    _WRAP_ARG_WITH_QUOTES = True


class AliasDeleteAll(SCPICmdWriteNoArguments):
    """The ``ALIas:DELEte:ALL`` command.

    Description:
        - This command deletes all existing aliases.

    Usage:
        - Using the ``.write()`` method will send the ``ALIas:DELEte:ALL`` command.

    SCPI Syntax:
        ```
        - ALIas:DELEte:ALL
        ```
    """


class AliasDelete(SCPICmdWrite, SCPICmdRead):
    """The ``ALIas:DELEte`` command.

    Description:
        - This command removes a specified alias and is identical to ``ALIas:DELEte:NAMe``. An error
          message is generated if the named alias does not exist.

    Usage:
        - Using the ``.write(value)`` method will send the ``ALIas:DELEte value`` command.

    SCPI Syntax:
        ```
        - ALIas:DELEte <QString>
        ```

    Info:
        - ``<QString>`` is the name of the alias to be removed. Using <QString> must be a previously
          defined value.

    Properties:
        - ``.all``: The ``ALIas:DELEte:ALL`` command.
        - ``.name``: The ``ALIas:DELEte:NAMe`` command.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._all = AliasDeleteAll(device, f"{self._cmd_syntax}:ALL")
        self._name = AliasDeleteName(device, f"{self._cmd_syntax}:NAMe")

    @property
    def all(self) -> AliasDeleteAll:
        """Return the ``ALIas:DELEte:ALL`` command.

        Description:
            - This command deletes all existing aliases.

        Usage:
            - Using the ``.write()`` method will send the ``ALIas:DELEte:ALL`` command.

        SCPI Syntax:
            ```
            - ALIas:DELEte:ALL
            ```
        """
        return self._all

    @property
    def name(self) -> AliasDeleteName:
        """Return the ``ALIas:DELEte:NAMe`` command.

        Description:
            - This command removes a specified alias. An error message is generated if the named
              alias does not exist. This command is identical to ``ALIas:DELEte``.

        Usage:
            - Using the ``.write(value)`` method will send the ``ALIas:DELEte:NAMe value`` command.

        SCPI Syntax:
            ```
            - ALIas:DELEte:NAMe <QString>
            ```

        Info:
            - ``<QString>`` is the name of the alias to remove. Using <QString> must be a previously
              defined alias.
        """
        return self._name


class AliasDefine(SCPICmdWrite, SCPICmdRead):
    """The ``ALIas:DEFine`` command.

    Description:
        - This command assigns a sequence of program messages to an alias label. These messages are
          then substituted for the alias whenever it is received as a command or query, provided
          that ``ALIas:STATE`` is turned on. The query form of this command returns the definitions
          of a selected alias.

    Usage:
        - Using the ``.query()`` method will send the ``ALIas:DEFine?`` query.
        - Using the ``.verify(value)`` method will send the ``ALIas:DEFine?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ALIas:DEFine value`` command.

    SCPI Syntax:
        ```
        - ALIas:DEFine <QString><,>{<QString>|<Block>}
        - ALIas:DEFine?
        ```

    Info:
        - ``<QString>`` is the alias label.
        - ``<QString>`` or <Block> is a complete sequence of program messages.
    """


class AliasCatalog(SCPICmdRead):
    """The ``ALIas:CATalog`` command.

    Description:
        - This query-only command returns a list of the currently defined alias labels, separated by
          commas. If no aliases are defined, the query returns the string ''.

    Usage:
        - Using the ``.query()`` method will send the ``ALIas:CATalog?`` query.
        - Using the ``.verify(value)`` method will send the ``ALIas:CATalog?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ALIas:CATalog?
        ```
    """


class Alias(SCPICmdWrite, SCPICmdRead):
    """The ``ALIas`` command.

    Description:
        - This command sets or queries the state of alias functionality, and it is identical to the
          ``ALIAS:STATE`` command.

    Usage:
        - Using the ``.query()`` method will send the ``ALIas?`` query.
        - Using the ``.verify(value)`` method will send the ``ALIas?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ALIas value`` command.

    SCPI Syntax:
        ```
        - ALIas {ON|OFF|<NR1>}
        - ALIas?
        ```

    Info:
        - ``OFF`` turns Alias expansion off.
        - ``ON`` turns Alias expansion on. When a defined alias is received, the specified command
          sequence is substituted for the alias and executed.
        - ``<NR1>`` = 0 disables Alias mode; any other value enables Alias mode.

    Properties:
        - ``.catalog``: The ``ALIas:CATalog`` command.
        - ``.define``: The ``ALIas:DEFine`` command.
        - ``.delete``: The ``ALIas:DELEte`` command.
        - ``.state``: The ``ALIas:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ALIas") -> None:
        super().__init__(device, cmd_syntax)
        self._catalog = AliasCatalog(device, f"{self._cmd_syntax}:CATalog")
        self._define = AliasDefine(device, f"{self._cmd_syntax}:DEFine")
        self._delete = AliasDelete(device, f"{self._cmd_syntax}:DELEte")
        self._state = AliasState(device, f"{self._cmd_syntax}:STATE")

    @property
    def catalog(self) -> AliasCatalog:
        """Return the ``ALIas:CATalog`` command.

        Description:
            - This query-only command returns a list of the currently defined alias labels,
              separated by commas. If no aliases are defined, the query returns the string ''.

        Usage:
            - Using the ``.query()`` method will send the ``ALIas:CATalog?`` query.
            - Using the ``.verify(value)`` method will send the ``ALIas:CATalog?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ALIas:CATalog?
            ```
        """
        return self._catalog

    @property
    def define(self) -> AliasDefine:
        """Return the ``ALIas:DEFine`` command.

        Description:
            - This command assigns a sequence of program messages to an alias label. These messages
              are then substituted for the alias whenever it is received as a command or query,
              provided that ``ALIas:STATE`` is turned on. The query form of this command returns the
              definitions of a selected alias.

        Usage:
            - Using the ``.query()`` method will send the ``ALIas:DEFine?`` query.
            - Using the ``.verify(value)`` method will send the ``ALIas:DEFine?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ALIas:DEFine value`` command.

        SCPI Syntax:
            ```
            - ALIas:DEFine <QString><,>{<QString>|<Block>}
            - ALIas:DEFine?
            ```

        Info:
            - ``<QString>`` is the alias label.
            - ``<QString>`` or <Block> is a complete sequence of program messages.
        """
        return self._define

    @property
    def delete(self) -> AliasDelete:
        """Return the ``ALIas:DELEte`` command.

        Description:
            - This command removes a specified alias and is identical to ``ALIas:DELEte:NAMe``. An
              error message is generated if the named alias does not exist.

        Usage:
            - Using the ``.write(value)`` method will send the ``ALIas:DELEte value`` command.

        SCPI Syntax:
            ```
            - ALIas:DELEte <QString>
            ```

        Info:
            - ``<QString>`` is the name of the alias to be removed. Using <QString> must be a
              previously defined value.

        Sub-properties:
            - ``.all``: The ``ALIas:DELEte:ALL`` command.
            - ``.name``: The ``ALIas:DELEte:NAMe`` command.
        """
        return self._delete

    @property
    def state(self) -> AliasState:
        """Return the ``ALIas:STATE`` command.

        Description:
            - This command turns aliases on or off and is identical to the ALIAS command. The query
              form of this command returns the state of the aliases.

        Usage:
            - Using the ``.query()`` method will send the ``ALIas:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ALIas:STATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ALIas:STATE value`` command.

        SCPI Syntax:
            ```
            - ALIas:STATE {ON|OFF|<NR1>}
            - ALIas:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 turns off aliases; any other value turns on aliases.
            - ``OFF`` turns alias expansion off.
            - ``ON`` turns alias expansion on. When a defined alias is received, the specified
              command sequence is substituted for the alias and executed.
        """
        return self._state
