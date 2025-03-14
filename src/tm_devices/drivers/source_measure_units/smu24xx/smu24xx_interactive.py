"""SMU24xxInteractive device driver module."""

from abc import ABC
from typing import Tuple

from tm_devices.driver_mixins.device_control import TSPControl
from tm_devices.driver_mixins.shared_implementations.common_tsp_error_check_mixin import (
    CommonTSPErrorCheckMixin,
)
from tm_devices.driver_mixins.shared_implementations.ieee488_2_commands import (
    LegacyTSPIEEE4882Commands,
)
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.source_measure_units.source_measure_unit import SourceMeasureUnit
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


@family_base_class
class SMU24xxInteractive(CommonTSPErrorCheckMixin, TSPControl, SourceMeasureUnit, ABC):
    """Base SMU24xxInteractive device driver."""

    _IEEE_COMMANDS_CLASS = LegacyTSPIEEE4882Commands

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""
        return tuple(f"OUTPUT{x + 1}" for x in range(self.total_channels))

    @property
    def ieee_cmds(self) -> LegacyTSPIEEE4882Commands:
        """Return an internal class containing methods for the standard IEEE 488.2 command set."""
        return self._ieee_cmds  # pyright: ignore[reportReturnType]

    @cached_property
    def total_channels(self) -> int:  # pylint: disable=no-self-use
        """Return the total number of channels (all types)."""
        return 1

    ################################################################################################
    # Public Methods
    ################################################################################################
    def _get_errors(self) -> Tuple[int, Tuple[str, ...]]:
        """Get the current errors from the device.

        !!! note
            This method will clear out the error queue after reading the current errors.

        Returns:
            A tuple containing the current error code alongside a tuple of the current error
                messages.
        """
        # instrument returns exponential numbers so converting to float before int
        error_code = int(float(self.query("print(status.standard.event)")))
        err_count = int(self.query("print(eventlog.getcount(eventlog.SEV_ERROR))"))
        error_message_list = []
        if err_count:
            error_message_list = [self.query("print(eventlog.next())") for _ in range(err_count)]
        return error_code, tuple(filter(None, error_message_list))

    ################################################################################################
    # Private Methods
    ################################################################################################
