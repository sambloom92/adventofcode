import os
from itertools import combinations
from math import prod
from typing import Iterable

from conf import ROOT_DIR


class SolutionNotFoundError(Exception):
    pass


REPORT_PATH = os.path.join(ROOT_DIR, "day_1/report.csv")


def get_report(filepath: str = REPORT_PATH) -> Iterable[int]:
    """
    read the file containing the exercise challenge data and return an iterable of the contents as integers
    :param filepath: path to file
    :return: generator expression yielding integers
    """
    with open(filepath) as file:
        return (int(line) for line in file.readlines())


def solver(n: int) -> int:
    """
    finds n numbers in the report where the sum is equal to 2020, and returns their product
    :param n: how many numbers to sum and multiply
    :return: the solution as an integer
    """
    for nums in combinations(get_report(), n):
        if sum(nums) == 2020:
            return prod(nums)
    else:
        raise SolutionNotFoundError("Could not find a solution for the given data")
