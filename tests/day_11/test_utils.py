import os

from conf import ROOT_DIR
from day_11.seating_pt1 import apply_rules
from day_11.utils import count_occupied_seats, get_seats, get_stable_arrangement

EXAMPLE_SEATS_PATH = os.path.join(ROOT_DIR, "tests/day_11/example_seats.csv")
EXAMPLE_SEATS = get_seats(EXAMPLE_SEATS_PATH)
EXAMPLE_SEATS_SOLUTION_PATH = os.path.join(
    ROOT_DIR, "tests/day_11/example_seats_solution_pt1.csv"
)
EXAMPLE_SEATS_SOLUTION = get_seats(EXAMPLE_SEATS_SOLUTION_PATH)


def test_get_seats():
    expected = [
        ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
        ["L", "L", "L", "L", "L", "L", "L", ".", "L", "L"],
        ["L", ".", "L", ".", "L", ".", ".", "L", ".", "."],
        ["L", "L", "L", "L", ".", "L", "L", ".", "L", "L"],
        ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
        ["L", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
        [".", ".", "L", ".", "L", ".", ".", ".", ".", "."],
        ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
        ["L", ".", "L", "L", "L", "L", "L", "L", ".", "L"],
        ["L", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
    ]
    assert get_seats(EXAMPLE_SEATS_PATH) == expected


def test_count_occupied_seats_empty():
    example_seats = get_seats(EXAMPLE_SEATS_PATH)
    assert count_occupied_seats(example_seats) == 0


def test_count_occupied_seats_final():
    example_seats_solution_path = os.path.join(
        ROOT_DIR, "tests/day_11/example_seats_solution_pt1.csv"
    )
    example_seats_solution = get_seats(example_seats_solution_path)
    assert count_occupied_seats(example_seats_solution) == 37


def test_get_stable_arrangement():
    expected_path = os.path.join(
        ROOT_DIR, "tests/day_11/example_seats_solution_pt1.csv"
    )
    expected = get_seats(expected_path)
    actual = get_stable_arrangement(EXAMPLE_SEATS, apply_rules)
    assert actual == expected
