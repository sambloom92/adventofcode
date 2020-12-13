import os

from conf import ROOT_DIR
from day_12.ship_pt1 import ShipPart1

EXAMPLE_INSTRUCTIONS_PATH = os.path.join(
    ROOT_DIR, "tests/day_12/example_instructions.csv"
)


def test_ship_init():
    test_ship = ShipPart1()
    assert test_ship.coordinates == [0, 0] and test_ship.heading == 90


def test_ship_change_heading():
    test_ship = ShipPart1()
    test_ship.change_heading("R", 90)
    assert test_ship.heading == 180
    test_ship.change_heading("L", 90)
    assert test_ship.heading == 90
    test_ship.change_heading("R", 270)
    assert test_ship.heading == 0


def test_execute_instruction():
    test_ship = ShipPart1()
    test_ship.execute_instruction("F", 10)
    assert test_ship.coordinates == [0, 10] and test_ship.heading == 90
    test_ship.execute_instruction("N", 3)
    assert test_ship.coordinates == [-3, 10] and test_ship.heading == 90
    test_ship.execute_instruction("N", 7)
    assert test_ship.coordinates == [-10, 10] and test_ship.heading == 90
    test_ship.execute_instruction("R", 90)
    assert test_ship.coordinates == [-10, 10] and test_ship.heading == 180
    test_ship.execute_instruction("F", 11)
    assert test_ship.coordinates == [1, 10] and test_ship.heading == 180
