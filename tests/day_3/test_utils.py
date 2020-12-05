import os

import pytest

from conf import ROOT_DIR
from day_3.utils import TobogganMapRow, get_map, multiply_trees_hit, step_through_map

EXAMPLE_MAP_1_PATH = os.path.join(ROOT_DIR, "tests/day_3/example_map_1.csv")


def test_get_map():
    expected = [
        TobogganMapRow("..##..."),
        TobogganMapRow("#...#.."),
        TobogganMapRow(".#....#"),
        TobogganMapRow("..#.#.."),
    ]
    assert get_map(EXAMPLE_MAP_1_PATH) == expected


EXAMPLE_MAP_2_PATH = os.path.join(ROOT_DIR, "tests/day_3/example_map_2.csv")
MAP = get_map(EXAMPLE_MAP_2_PATH)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("step_through_map(1, 1, MAP)", 2),
        ("step_through_map(1, 3, MAP)", 7),
        ("step_through_map(1, 5, MAP)", 3),
        ("step_through_map(1, 7, MAP)", 4),
        ("step_through_map(2, 1, MAP)", 2),
    ],
)
def test_step_through_map(test_input, expected):
    assert eval(test_input) == expected


def test_multiply_trees_hit():
    assert multiply_trees_hit(MAP) == 336
