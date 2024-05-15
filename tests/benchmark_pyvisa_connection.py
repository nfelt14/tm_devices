"""A simple script called from a benchmarking test function in test_benchmarks.py."""

from unittest import mock

import pyvisa

from conftest import SIMULATED_VISA_LIB

INSTRUMENT_RESOURCE_EXPRESSION = "TCPIP0::MSO58B-HOSTNAME::inst0::INSTR"
CUSTOM_MOCK = mock.MagicMock(return_value=0)

# NOTE: Adding mock patches for parity with other benchmark
with mock.patch(
    "pyvisa.resources.messagebased.MessageBasedResource.read_stb",
    CUSTOM_MOCK,
), mock.patch(
    "pyvisa.resources.messagebased.MessageBasedResource.clear",
    CUSTOM_MOCK,
):
    rm = pyvisa.ResourceManager(SIMULATED_VISA_LIB)
    print("Opened ResourceManager")
    instrument = rm.open_resource(INSTRUMENT_RESOURCE_EXPRESSION)
    print(f'Connected to "{INSTRUMENT_RESOURCE_EXPRESSION}"')
    instrument.read_termination = "\n"  # pyright: ignore[reportAttributeAccessIssue]
    instrument.write_termination = "\n"  # pyright: ignore[reportAttributeAccessIssue]
    # noinspection PyUnresolvedReferences
    print(f"*IDN? response: {instrument.query('*IDN?')}")  # pyright: ignore[reportUnknownMemberType,reportAttributeAccessIssue]
    instrument.close()
    print(f'Closed connection with "{INSTRUMENT_RESOURCE_EXPRESSION}"')
    rm.close()
    print("Closed ResourceManager")
