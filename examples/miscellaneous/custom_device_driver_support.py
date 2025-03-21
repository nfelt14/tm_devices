"""An example of external device support via a custom driver."""

from typing import Tuple

from tm_devices import DeviceManager, register_additional_usbtmc_mapping
from tm_devices.driver_mixins.device_control import PIControl
from tm_devices.drivers import MSO5
from tm_devices.drivers.device import Device
from tm_devices.drivers.scopes.scope import Scope
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


# Custom devices that inherit from a supported device type can be defined by inheriting from the
# specific device type class. This custom class must implement all abstract methods defined by the
# abstract parent classes.
class CustomScope(PIControl, Scope):
    """Custom scope class."""

    # This is an abstract method that must be implemented by the custom device driver
    @cached_property
    def total_channels(self) -> int:
        return 4

    # This is an abstract method that must be implemented by the custom device driver.
    def _get_errors(self) -> Tuple[int, Tuple[str, ...]]:
        """Get the current errors from the device."""
        # The contents of this method would need to be properly implemented,
        # this is just example code. :)
        return 0, ()

    def custom_method(self, value: str) -> None:
        """Add a custom method to the custom driver."""
        print(f"{self.name}, {value=}")


# Custom devices that do not inherit from a supported device type can be defined by inheriting from
# a parent class further up the inheritance tree as well as a control mixin class to provide the
# necessary methods for controlling the device. This custom class must also implement all abstract
# methods defined by the abstract parent classes.
class CustomDevice(PIControl, Device):
    """A custom device that is not one of the officially supported devices."""

    # Custom device types not officially supported need to define what type of device they are.
    @cached_property
    def device_type(self) -> str:
        """Return the device type."""
        return "CustomDevice"

    # This is an abstract method that must be implemented by the custom device driver.
    def _get_errors(self) -> Tuple[int, Tuple[str, ...]]:
        """Get the current errors from the device."""
        # The contents of this method would need to be properly implemented,
        # this is just example code. :)
        return 0, ()

    def custom_device_method(self, value: int) -> None:
        """Add a custom method to the custom device driver."""
        print(f"{self.name}, {value=}")


# For VISA devices, the model series is based on the model that is returned from
# the ``*IDN?`` query. (See the ``tm_devices.helpers.get_model_series()`` function for details)
# For REST API devices, the model series is provided via the ``device_driver`` parameter in
# the configuration file, environment variable, or python code.
CUSTOM_DEVICE_DRIVERS = {  # A mapping of custom model series strings to Python driver classes
    "CustomModelSeries": CustomScope,
    "CustomDeviceModelSeries": CustomDevice,
}


# To enable USBTMC connection support for a device without native USBTMC support in tm_devices,
# simply register the USBTMC connection information for the device's model series.
register_additional_usbtmc_mapping("CustomModelSeries", model_id="0x0000", vendor_id="0x0000")


with DeviceManager(external_device_drivers=CUSTOM_DEVICE_DRIVERS) as device_manager:
    # Add a scope that is currently supported by the package
    mso5: MSO5 = device_manager.add_scope("192.168.0.1")
    # Add the custom scope with a USB connection after registering the USBTMC mapping above
    custom_scope: CustomScope = device_manager.add_scope("MODEL-SERIAL", connection_type="USB")
    # Add the custom device that is a device type not officially supported
    # NOTE: If using a config file or environment variable to define a device that is unsupported,
    #       the `device_type` key must be set to "UNSUPPORTED".
    custom_device: CustomDevice = device_manager.add_unsupported_device("192.168.0.3")

    # Custom drivers inherit all methods and attributes
    print(custom_scope.all_channel_names_list)  # print the channel names
    custom_scope.cleanup()  # cleanup the custom scope
    # Custom drivers can also use added methods
    custom_scope.custom_method("value")

    # Custom device types still inherit methods from their parent classes, though device type
    # specific functionality is not defined by default
    assert not custom_device.has_errors()  # check for no errors
    # Custom devices can also use any custom methods added to the custom class
    custom_device.custom_device_method(10)
