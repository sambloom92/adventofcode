import copy
import os
from typing import List, Tuple

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


def get_neighbours(seats: List[List[str]], coordinates: Tuple[int, int]) -> List[str]:
    row_num, column_num = coordinates
    max_row = len(seats) - 1
    max_columns = len(seats[0]) - 1
    neighbours = []
    if row_num > 0:
        north = seats[row_num - 1][column_num]
        neighbours.append(north)
    if row_num > 0 and column_num < max_columns:
        north_east = seats[row_num - 1][column_num + 1]
        neighbours.append(north_east)
    if column_num < max_columns:
        east = seats[row_num][column_num + 1]
        neighbours.append(east)
    if row_num < max_row and column_num < max_columns:
        south_east = seats[row_num + 1][column_num + 1]
        neighbours.append(south_east)
    if row_num < max_row:
        south = seats[row_num + 1][column_num]
        neighbours.append(south)
    if row_num < max_row and column_num > 0:
        south_west = seats[row_num + 1][column_num - 1]
        neighbours.append(south_west)
    if column_num > 0:
        west = seats[row_num][column_num - 1]
        neighbours.append(west)
    if row_num > 0 and column_num > 0:
        north_west = seats[row_num - 1][column_num - 1]
        neighbours.append(north_west)
    return neighbours


def apply_rules(seats: List[List[str]]) -> List[List[str]]:
    new_seats = copy.deepcopy(seats)
    for row_num, row in enumerate(seats):
        for column_num, value in enumerate(row):
            neighbours = get_neighbours(seats, (row_num, column_num))
            if value == "L" and not any([neighbour == "#" for neighbour in neighbours]):
                new_seats[row_num][column_num] = "#"
            elif (
                value == "#"
                and len([neighbour for neighbour in neighbours if neighbour == "#"])
                >= 4
            ):
                new_seats[row_num][column_num] = "L"
    return new_seats


def get_stable_arrangement(seats: List[List[str]]) -> List[List[str]]:
    current_arrangement = copy.deepcopy(seats)
    new_arrangement = apply_rules(current_arrangement)
    if current_arrangement == new_arrangement:
        return new_arrangement
    else:
        return get_stable_arrangement(new_arrangement)


def count_occupied_seats(seats: List[List[str]]) -> int:
    return len([value for row in seats for value in row if value == "#"])


print(count_occupied_seats(get_stable_arrangement(get_seats(SEATS_PATH))))
