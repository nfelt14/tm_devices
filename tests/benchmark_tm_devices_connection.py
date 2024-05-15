"""A simple script called from a benchmarking test function in test_benchmarks.py."""

from unittest import mock

from conftest import SIMULATED_VISA_LIB
from tm_devices import DeviceManager

INSTRUMENT_RESOURCE_EXPRESSION = "TCPIP0::MSO58B-HOSTNAME::inst0::INSTR"
CUSTOM_MOCK = mock.MagicMock(return_value=0)

# NOTE: Adding mock patches to enable code to work on simulated instruments,
# the other benchmark script has the mocks included for parity with this benchmark script
with mock.patch(
    "pyvisa.resources.messagebased.MessageBasedResource.read_stb",
    CUSTOM_MOCK,
), mock.patch(
    "pyvisa.resources.messagebased.MessageBasedResource.clear",
    CUSTOM_MOCK,
), DeviceManager(verbose=False) as dm:
    dm.visa_library = SIMULATED_VISA_LIB

    instrument = dm.add_scope(INSTRUMENT_RESOURCE_EXPRESSION)
    instrument.query("*IDN?")
