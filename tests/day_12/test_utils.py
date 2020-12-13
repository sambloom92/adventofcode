import os

from conf import ROOT_DIR
from day_12.ship_pt1 import ShipPart1
from day_12.utils import Ship, get_instructions

EXAMPLE_INSTRUCTIONS_PATH = os.path.join(
    ROOT_DIR, "tests/day_12/example_instructions.csv"
)


def test_get_instructions():
    expected = [
        {"F": 10},
        {"N": 3},
        {"F": 7},
        {"R": 90},
        {"F": 11},
    ]
    assert get_instructions(EXAMPLE_INSTRUCTIONS_PATH) == expected


def test_ship_init():
    test_ship = ShipPart1()
    assert test_ship.coordinates == [0, 0]


def test_ship_translate():
    test_ship = ShipPart1()
    vector = (1, 1)
    test_ship.translate(vector, 3)
    expected = [3, 3]
    assert test_ship.coordinates == expected


def test_ship_get_manhattan_distance():
    test_ship = ShipPart1()
    vector = (1, 1)
    test_ship.translate(vector, 3)
    assert test_ship.get_manhattan_distance() == 6


def test_ship_execute_all_instructions():
    test_ship = ShipPart1()
    instructions = get_instructions(EXAMPLE_INSTRUCTIONS_PATH)
    test_ship.execute_all_instructions(instructions)
    assert test_ship.coordinates == [8, 17] and test_ship.heading == 180
