"""The clear commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CLEAR {ALL}
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Clear(SCPICmdWrite):
    """The ``CLEAR`` command.

    Description:
        - This command clears acquisitions, measurements, and waveforms.

    Usage:
        - Using the ``.write(value)`` method will send the ``CLEAR value`` command.

    SCPI Syntax:
        ```
        - CLEAR {ALL}
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CLEAR") -> None:
        super().__init__(device, cmd_syntax)
