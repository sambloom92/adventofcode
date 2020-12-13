import os

from conf import ROOT_DIR
from day_12.ship_pt2 import ShipPart2

EXAMPLE_INSTRUCTIONS_PATH = os.path.join(
    ROOT_DIR, "tests/day_12/example_instructions.csv"
)


def test_ship_init():
    test_ship = ShipPart2()
    assert test_ship.coordinates == [0, 0] and test_ship.waypoint_vector == [-1, 10]


def test_ship_translate_waypoint():
    test_ship = ShipPart2()
    test_ship.translate_waypoint([1, 1], 3)
    assert test_ship.coordinates == [0, 0] and test_ship.waypoint_vector == [2, 13]


def test_ship_rotate_waypoint():
    test_ship = ShipPart2()
    test_ship.rotate_waypoint("R", 90)
    assert test_ship.waypoint_vector == [10, 1]
    test_ship.rotate_waypoint("L", 90)
    assert test_ship.waypoint_vector == [-1, 10]
    test_ship.rotate_waypoint("R", 270)
    assert test_ship.waypoint_vector == [-10, -1]


def test_execute_instruction():
    test_ship = ShipPart2()
    test_ship.execute_instruction("F", 10)
    assert test_ship.coordinates == [-10, 100] and test_ship.waypoint_vector == [-1, 10]
    test_ship.execute_instruction("N", 3)
    assert test_ship.coordinates == [-10, 100] and test_ship.waypoint_vector == [-4, 10]
    test_ship.execute_instruction("N", 7)
    assert test_ship.coordinates == [-10, 100] and test_ship.waypoint_vector == [
        -11,
        10,
    ]
    test_ship.execute_instruction("R", 90)
    assert test_ship.coordinates == [-10, 100] and test_ship.waypoint_vector == [10, 11]
    test_ship.execute_instruction("F", 11)
    assert test_ship.coordinates == [100, 221] and test_ship.waypoint_vector == [10, 11]
