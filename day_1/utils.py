from itertools import combinations
from math import prod
from typing import Iterable


class SolutionNotFoundError(Exception):
    pass


def get_report(filename: str = "report.csv") -> Iterable[int]:
    """
    read the file containing the exercise challenge data and return an iterable of the contents as integers
    :param filename: relative path
    :return: generator expression yielding integers
    """
    with open(filename) as file:
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
