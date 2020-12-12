import copy
import os
from typing import Callable, List

from conf import ROOT_DIR

SEATS_PATH = os.path.join(ROOT_DIR, "day_11/seats.csv")


def get_seats(filepath: str = SEATS_PATH) -> List[List[str]]:
    """
    read the file containing the exercise challenge data and return an iterable of the contents
    :param filepath: path to file
    :return: list of rows as strings
    """
    with open(filepath) as file:
        return [[value for value in line.strip()] for line in file.readlines()]


def count_occupied_seats(seats: List[List[str]]) -> int:
    """
    count how many seats are occupied for a given arrangement
    :param seats: list of lists of values
    :return: how many '#'s are present
    """
    return len([value for row in seats for value in row if value == "#"])


def get_stable_arrangement(
    seats: List[List[str]], rule_func: Callable
) -> List[List[str]]:
    """
    apply the rules repeatedly until a stable arrangement arises
    :param seats: the seating arrangement
    :return: a seating arrangement which does not change if rules are applied again
    """
    current_arrangement = copy.deepcopy(seats)
    new_arrangement = rule_func(current_arrangement)
    if current_arrangement == new_arrangement:
        return new_arrangement
    else:
        return get_stable_arrangement(new_arrangement, rule_func)
