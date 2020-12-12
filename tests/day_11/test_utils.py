import os

from conf import ROOT_DIR
from day_11.utils import count_occupied_seats, get_seats

EXAMPLE_SEATS_PATH = os.path.join(ROOT_DIR, "tests/day_11/example_seats.csv")


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
