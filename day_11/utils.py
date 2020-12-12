import os
from typing import List

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
    return len([value for row in seats for value in row if value == "#"])
