import os
from typing import Iterable, List

from conf import ROOT_DIR

CYPHER_PATH = os.path.join(ROOT_DIR, "day_9/xmas_cypher.csv")


class NoSolutionError(Exception):
    pass


def get_numbers(filepath: str = CYPHER_PATH) -> List[int]:
    """
    read the file containing the exercise challenge data and return an iterable of the contents
    :param filepath: path to file
    :return: generator expression yielding lines of the cypher file
    """
    with open(filepath) as file:
        return [int(line.strip()) for line in file.readlines()]


def get_window(cypher: List[int], index: int, length: int) -> List[int]:
    """
    get a slice of the list of a specified length, starting from index
    :param cypher: ordered list of numbers
    :param index: index to start from
    :param length: size of window
    :return: ordered list of numbers in window
    """
    return cypher[index : index + length]


def is_sum(numbers: Iterable[int], value: int) -> bool:
    """
    check if the sum of a collection of numbers produces the specified sum
    :param numbers: iterable of numbers to sum over
    :param value: target sum to check against
    :return: whether the sum is equal to the target value
    """
    return sum(numbers) == value
