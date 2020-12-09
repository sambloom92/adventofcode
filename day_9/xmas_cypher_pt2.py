import os
from typing import Iterable, List

from conf import ROOT_DIR
from day_9.utils import NoSolutionError, get_numbers, get_window, is_sum
from day_9.xmax_cypher_pt1 import solver as solver_pt1

CYPHER_PATH = os.path.join(ROOT_DIR, "day_9/xmas_cypher.csv")


def sum_min_max(numbers: Iterable[int]) -> int:
    """
    calculated the sum of the largest value and smallest value in a given list of numbers
    :param numbers: list of numbers
    :return: value of min + max
    """
    return min(numbers) + max(numbers)


def solver_pt2(cypher: List[int]) -> int:
    """
    find the contiguous range of numbers which sum to the value found in part 1, and return min + max
    :param cypher: ordered list of numbers
    :return: min + max for the contiguous range of numbers summing to the target value
    """
    target_sum = solver_pt1(cypher)
    n_numbers = len(cypher)
    for index in range(n_numbers):
        max_window = n_numbers - index
        for window_length in range(max_window):
            window = get_window(cypher, index, window_length)
            if is_sum(window, target_sum):
                return sum_min_max(window)
    raise NoSolutionError


if __name__ == "__main__":
    print(solver_pt2(get_numbers()))
