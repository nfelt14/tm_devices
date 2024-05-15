"""Benchmarking tests."""

import subprocess
import sys

from pathlib import Path

import pytest

from pytest_benchmark.fixture import BenchmarkFixture  # pyright: ignore[reportMissingTypeStubs]


@pytest.mark.slow
@pytest.mark.benchmark
def test_pyvisa_benchmark(benchmark: BenchmarkFixture) -> None:
    """Benchmark speed with pyvisa."""
    args = [sys.executable, str(Path(__file__).parent / "benchmark_pyvisa_connection.py")]
    benchmark(subprocess.check_call, args)


@pytest.mark.slow
@pytest.mark.benchmark
def test_tm_devices_benchmark(benchmark: BenchmarkFixture) -> None:
    """Benchmark speed with tm_devices."""
    args = [sys.executable, str(Path(__file__).parent / "benchmark_tm_devices_connection.py")]
    benchmark(subprocess.check_call, args)
