# Basic Usage

A collection of examples showing the basics of how to use `tm_devices` in a
project.

## List available VISA devices

This will print the available VISA devices to the console when run from a shell terminal.

```console
$ list-visa-resources
[
  "TCPIP0::192.168.0.100::inst0::INSTR",
  "ASRL4::INSTR"
]
```

## Adding devices

Configure device connections as needed using the
[config file](configuration.md#config-file), an
[environment variable](configuration.md#environment-variable), or
via [Python code](configuration.md#python-code) (shown here). See the
[Configuration guide](configuration.md) for more information on how to
configure devices to connect with.

<!--codeinclude-->
[](../examples/miscellaneous/adding_devices.py)
<!--/codeinclude-->

## VISA backend selection

The `DeviceManager` can be configured to use VISA backends from different VISA implementations.

<!--codeinclude-->
[](../examples/miscellaneous/visa_connection_selectivity.py)
<!--/codeinclude-->

## Alias usage

Devices can be given custom alias names and can be referenced by that alias.

<!--codeinclude-->
[](../examples/miscellaneous/alias_usage.py)
<!--/codeinclude-->

## Adding devices with environment variables

Device configuration information can be defined in an
[environment variable](configuration.md#environment-variable), usually done
outside the Python code for ease of automation
(shown inside the Python code here for demonstration purposes).

<!--codeinclude-->
[](../examples/miscellaneous/adding_devices_with_env_var.py)
<!--/codeinclude-->

## Disable command checking

This removes an extra query that verifies the property was set to the expected
value. This can be disabled at the device level or disabled for all devices by
disabling verification via the device manager.

<!--codeinclude-->
[](../examples/miscellaneous/disable_command_verification.py)
<!--/codeinclude-->

## Generate a signal using the Internal AFG

Use the Internal AFG to generate a 1 V, 10 MHz square wave with a 200 mV offset
on CH1 of the SCOPE.

- Requires a SCOPE with a license for the Internal AFG.
- Requires the Internal AFG output to be connected to CH1 on the SCOPE

<!--codeinclude-->
[](../examples/scopes/tekscope/generate_internal_afg_signal.py)
<!--/codeinclude-->

## Curve query saved to csv

Perform a curve query and save the results to a csv file.

- Requires an AFG connected to channel 1 on a SCOPE.

<!--codeinclude-->
[](../examples/scopes/tekscope/basic_curve_query.py)
<!--/codeinclude-->

## Saving / recalling a waveform and session

We can save a waveform on our scope to an external file. This is useful for
recalling previously saved waveforms if we ever need to use that waveform again.

The same can be done for scope sessions, sessions are essentially a snapshot of
the current state of our scope.

<!--codeinclude-->
[](../examples/scopes/tekscope/basic_save_recall.py)
<!--/codeinclude-->

## Configuring a measurement on a single sequence

A scope can be configured for a measurement on a single acquisition by setting the appropriate acquisition parameters
and adding the desired measurement on the selected channel.

<!--codeinclude-->
[](../examples/scopes/tekscope/get_acquisition_data.py)
<!--/codeinclude-->

## Adding DPOJET measurements and plots

DPOJET measurements and plots can be added on a DPO70KSX/C/7KC/DPO5KB scope.
Measurements report can be saved in a `.pdf` format.

<!--codeinclude-->
[](../examples/scopes/tekscope_70k/dpojet/adding_dpojet_measurements.py)
<!--/codeinclude-->

## Directly accessing the PyVISA resource object

The [PyVISA](https://pyvisa.readthedocs.io/en/latest/) resource object can be directly
accessed if there is a specific action that is not yet available directly through
the drivers in the `tm_devices` package.

<!--codeinclude-->
[](../examples/miscellaneous/pyvisa_resource_access.py)
<!--/codeinclude-->

## Dynamic reading buffers (SMUs)

Create and read from a dynamic buffer.

<!--codeinclude-->
[](../examples/source_measure_units/2600/reading_dynamic_buffers.py)
<!--/codeinclude-->

## Registering the Device Manager to be closed at program termination

Sometimes using the `DeviceManager` class as a context manager is not feasible.
In those instances there is an alternative way to enforce the device manager to
close when the Python script execution is finished without needing to explicitly
call the `.close()` method.

<!--codeinclude-->
[](../examples/miscellaneous/register_dm_atexit.py)
<!--/codeinclude-->

## Add custom device support

Sometimes there is a need to use a device that is not currently supported by
`tm_devices`. When this is the case, custom device driver classes can be created
and passed to the [DeviceManager][tm_devices.DeviceManager] when it is
first instantiated.

In order to do this a few things will need to be created:

1. A custom device class inheriting from one of the
    [main device types](advanced/architecture.md#main-device-types).
2. A mapping of the parsed model series string to the Python class.

<!--codeinclude-->
[](../examples/miscellaneous/custom_device_driver_support.py)
<!--/codeinclude-->
