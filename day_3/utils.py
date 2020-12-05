import os
from itertools import cycle, islice
from math import prod
from typing import List

from conf import ROOT_DIR

MAP_PATH = os.path.join(ROOT_DIR, "day_3/map.csv")


class TobogganMapRow:
    def __init__(self, row_pattern: str):
        """
        the rows of a toboggan map repeat a pattern infinitely, so instances are characterised by a repeating pattern
        :param row_pattern: a finite string of '.' and '#', to be repeated
        """
        self.row_pattern = row_pattern.strip()

    def _get_row_cycle(self) -> cycle:
        """
        return a new cycle for each call as cycles are mutable
        :return: a generator which repeats row_pattern infinitely
        """
        return cycle(self.row_pattern)

    def __getitem__(self, index) -> str:
        """
        allow fetching of the value at any index, with no limitation on index range
        :param index: number of steps across the row to fetch the value from
        :return: value of the row at the given index - either '.' or '#'
        """
        return next(islice(self._get_row_cycle(), index, index + 1))

    def __eq__(self, other) -> bool:
        """
        allow comparison for unit testing
        """
        return self.row_pattern == other.row_pattern

    def __repr__(self) -> str:
        """
        representation for easy debugging
        """
        return f"{self.row_pattern}--->"


def get_map(filepath: str = MAP_PATH) -> List[TobogganMapRow]:
    """
    read the file containing the exercise challenge data and return an iterable of the contents as integers
    :param filepath: path to file
    :return: generator expression yielding integers
    """
    with open(filepath) as file:
        return [TobogganMapRow(row) for row in file.readlines()]


def step_through_map(
    down_steps: int, right_steps: int, tree_map: List[TobogganMapRow]
) -> int:
    """
    step through the map using the specified trajectory, until the bottom is reached, returning how many trees were
    encountered
    :param down_steps: how many downward steps to take each time
    :param right_steps: how many steps to the right to take each time
    :param tree_map: the map to step through
    :return: how many trees were encountered
    """
    row, col = 0, 0
    tree_counter = 0
    while row < len(tree_map):
        value = tree_map[row][col]
        if value == "#":
            tree_counter += 1
        row += down_steps
        col += right_steps
    return tree_counter


def multiply_trees_hit(tree_map: List[TobogganMapRow]) -> int:
    """
    count trees hit for each of the five trajectories and return their product
    :param tree_map: the map to be used
    :return: the product of the trees hit for each trajectory
    """
    trajectories = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1),
    ]
    trees_hit_list = [
        step_through_map(down, right, tree_map) for down, right in trajectories
    ]
    return prod(trees_hit_list)
