from itertools import combinations
from math import prod
from typing import Iterable


class SolutionNotFoundError(Exception):
    pass


def get_report(filename: str = "report.csv") -> Iterable[int]:
    with open(filename) as file:
        return (int(line) for line in file.readlines())


def solver(n: int) -> int:
    for nums in combinations(get_report(), n):
        if sum(nums) == 2020:
            return prod(nums)
    else:
        raise SolutionNotFoundError("Could not find a solution for the given data")
