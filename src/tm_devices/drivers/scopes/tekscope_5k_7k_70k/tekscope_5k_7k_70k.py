"""Base TekScope5k7k70k scope device driver module."""

from abc import ABC

import pyvisa as visa

from tm_devices.driver_mixins.device_control import PIControl
from tm_devices.driver_mixins.shared_implementations._tektronix_pi_scope_mixin import (
    _TektronixPIScopeMixin,  # pyright: ignore[reportPrivateUsage]
)
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.scopes.scope import Scope
from tm_devices.helpers import DeviceConfigEntry
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


@family_base_class
class TekScope5k7k70k(_TektronixPIScopeMixin, PIControl, Scope, ABC):
    """Base TekScope5k7k70k scope device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
        default_visa_timeout: int,
    ) -> None:
        """Create a TekScope5k7k70k device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed. If True,
                communication printouts will be logged with a level of INFO. If False,
                communication printouts will be logged with a level of DEBUG.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        super().__init__(config_entry, verbose, visa_resource, default_visa_timeout)
        self.write("HEADER OFF", verbose=False)
        # Extract the numeric part as string from the model number
        digits = "".join(char for char in self.model if char.isdigit())
        # Last digit represents the channel number.
        self._total_channels: int = int(digits[-1])
        # Check for models starting with MSO, as these models only offer digital channels.
        if self.model.startswith("MSO"):
            self._num_dig_bits_in_ch: int = 16
        else:
            self._num_dig_bits_in_ch = 0

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def num_dig_bits_in_ch(self) -> int:
        """Return the number of digital bits expected in a digital channel."""
        # TODO: should be part of self.channel
        #  https://github.com/tektronix/tm_devices/issues/329
        return self._num_dig_bits_in_ch

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return self._total_channels

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
