# Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""Implement the DataParser for network latency performance tests."""

import statistics
from collections.abc import Iterator
from typing import List
from providers.types import DataParser

# We add a small extra percentage margin, to account for small variations
# that were not caught while gathering baselines. This provides
# slightly better reliability, while not affecting regression
# detection.
DELTA_EXTRA_MARGIN = 0.01


# pylint: disable=R0903
class LatencyDataParser(DataParser):
    """Parse the data provided by the network latency performance tests."""

    # pylint: disable=W0102
    def __init__(self, data_provider: Iterator):
        """Initialize the data parser."""
        super().__init__(
            data_provider,
            ["latency/Avg"],
        )

    def calculate_baseline(self, data: List[float]) -> dict:
        """Return the target and delta values, given a list of data points."""
        avg = statistics.mean(data)
        stddev = statistics.stdev(data)
        return {
            "target": round(avg, 3),
            "delta_percentage": round(stddev + DELTA_EXTRA_MARGIN, 2),
        }
