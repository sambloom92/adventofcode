import os

import pytest

from conf import ROOT_DIR
from day_11.seating_pt1 import apply_rules, get_immediate_neighbours
from day_11.utils import get_seats

EXAMPLE_SEATS_PATH = os.path.join(ROOT_DIR, "tests/day_11/example_seats.csv")
EXAMPLE_SEATS = get_seats(EXAMPLE_SEATS_PATH)
EXAMPLE_SEATS_SOLUTION_PATH = os.path.join(
    ROOT_DIR, "tests/day_11/example_seats_solution_pt1.csv"
)
EXAMPLE_SEATS_SOLUTION = get_seats(EXAMPLE_SEATS_SOLUTION_PATH)
EXAMPLE_SEATS_PENULTIMATE_PATH = os.path.join(
    ROOT_DIR, "tests/day_11/example_seats_penultimate_pt1.csv"
)
EXAMPLE_SEATS_PENULTIMATE = get_seats(EXAMPLE_SEATS_PENULTIMATE_PATH)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("get_immediate_neighbours(EXAMPLE_SEATS, (0, 0))", ["L", "L"]),
        (
            "get_immediate_neighbours(EXAMPLE_SEATS, (1, 1))",
            ["L", "L", "L", "L", "L", "L"],
        ),
        ("get_immediate_neighbours(EXAMPLE_SEATS, (6, 2))", ["L", "L", "L", "L", "L"]),
        ("get_immediate_neighbours(EXAMPLE_SEATS_SOLUTION, (0, 0))", ["L", "#"]),
        (
            "get_immediate_neighbours(EXAMPLE_SEATS_SOLUTION, (1, 1))",
            ["#", "L", "#", "L", "#", "#"],
        ),
        (
            "get_immediate_neighbours(EXAMPLE_SEATS_SOLUTION, (6, 2))",
            ["#", "L", "L", "#", "L"],
        ),
    ],
)
def test_get_immediate_neighbours(test_input, expected):
    assert eval(test_input) == expected


def test_apply_rules():
    assert apply_rules(EXAMPLE_SEATS_PENULTIMATE) == EXAMPLE_SEATS_SOLUTION
