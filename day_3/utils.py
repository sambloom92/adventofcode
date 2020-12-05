from itertools import cycle, islice
from math import prod
from typing import List


class TobogganMapRow:
    def __init__(self, row_pattern: str):
        self.row_pattern = row_pattern.strip()

    def _get_row_cycle(self) -> cycle:
        return cycle(self.row_pattern)

    def __getitem__(self, index) -> str:
        return next(islice(self._get_row_cycle(), index, index + 1))

    def __eq__(self, other):
        return self.row_pattern == other.row_pattern

    def __repr__(self):
        return f"{self.row_pattern}--->"


def get_map(filename: str = "map.csv") -> List[TobogganMapRow]:
    """
    read the file containing the exercise challenge data and return an iterable of the contents as integers
    :param filename: relative path
    :return: generator expression yielding integers
    """
    with open(filename) as file:
        return [TobogganMapRow(row) for row in file.readlines()]


def step_through_map(
    down_steps: int, right_steps: int, tree_map: List[TobogganMapRow]
) -> int:
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
