import os

import pytest

from conf import ROOT_DIR
from day_9.utils import get_numbers, get_window, is_sum

EXAMPLE_CYPHER_PATH = os.path.join(ROOT_DIR, "tests/day_9/example_cypher.csv")


def test_get_numbers():
    expected = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]
    assert get_numbers(EXAMPLE_CYPHER_PATH) == expected


@pytest.mark.parametrize(
    "test_inputs,expected",
    [
        ("get_window(get_numbers(EXAMPLE_CYPHER_PATH), 0, 1)", [35]),
        ("get_window(get_numbers(EXAMPLE_CYPHER_PATH), 0, 5)", [35, 20, 15, 25, 47]),
        ("get_window(get_numbers(EXAMPLE_CYPHER_PATH), 1, 1)", [20]),
        ("get_window(get_numbers(EXAMPLE_CYPHER_PATH), 1, 5)", [20, 15, 25, 47, 40]),
    ],
)
def test_get_window(test_inputs, expected):
    assert eval(test_inputs) == expected


@pytest.mark.parametrize(
    "test_inputs,expected",
    [
        ("is_sum((1, 2), 3)", True),
        ("is_sum((2, 3), 5)", True),
        ("is_sum((1, 2), 4)", False),
    ],
)
def test_is_sum(test_inputs, expected):
    assert eval(test_inputs) == expected
