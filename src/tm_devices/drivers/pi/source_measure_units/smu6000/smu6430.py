"""SMU6430 device driver module."""

import pyvisa as visa

from tm_devices.drivers.pi.source_measure_units.smu6000.smu6000 import SMU6000
from tm_devices.helpers import DeviceConfigEntry


class SMU6430(SMU6000):
    """SMU6430 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(  # pylint: disable=useless-parent-delegation
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a SMU6430 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
