import os

import pytest

from conf import ROOT_DIR
from day_10.adapters_pt2 import (
    calculate_total_arrangements,
    count_arrangements,
    is_valid_arrangement,
    split_into_sublists,
)
from day_10.utils import get_adapters

SHORT_EXAMPLE_PATH = os.path.join(ROOT_DIR, "tests/day_10/short_example.csv")
SHORT_EXAMPLE_VALUES = get_adapters(SHORT_EXAMPLE_PATH)
LONG_EXAMPLE_PATH = os.path.join(ROOT_DIR, "tests/day_10/long_example.csv")
LONG_EXAMPLE_VALUES = get_adapters(LONG_EXAMPLE_PATH)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("is_valid_arrangement([1, 2, 3, 4, 5])", True),
        ("is_valid_arrangement([1, 2, 4, 5])", True),
        ("is_valid_arrangement([1, 5])", False),
        ("is_valid_arrangement([1])", True),
    ],
)
def test_is_valid_arrangement(test_input, expected):
    assert eval(test_input) == expected


def test_split_into_sublists():
    expected = [[0, 1], [4, 5, 6, 7], [10, 11, 12], [15, 16], [19, 22]]
    assert split_into_sublists(SHORT_EXAMPLE_VALUES) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("count_arrangements([1, 2, 3, 4, 5])", 7),
        ("count_arrangements([1, 2, 3, 4])", 4),
        ("count_arrangements([1, 2])", 1),
        ("count_arrangements([1])", 1),
    ],
)
def test_count_arrangements(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("calculate_total_arrangements(SHORT_EXAMPLE_VALUES)", 8),
        ("calculate_total_arrangements(LONG_EXAMPLE_VALUES)", 19208),
    ],
)
def test_calculate_total_arrangements(test_input, expected):
    assert eval(test_input) == expected
