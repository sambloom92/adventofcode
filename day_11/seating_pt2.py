import copy
import os
from typing import List, Tuple

from conf import ROOT_DIR
from day_11.utils import count_occupied_seats, get_seats

SEATS_PATH = os.path.join(ROOT_DIR, "day_11/seats.csv")


def get_visible_seats(
    seats: List[List[str]], coordinates: Tuple[int, int]
) -> List[str]:
    row_num, column_num = coordinates
    max_row = len(seats) - 1
    max_column = len(seats[0]) - 1
    visible_seats = []
    directions = {
        "north": (-1, 0),
        "northeast": (-1, 1),
        "east": (0, 1),
        "southeast": (1, 1),
        "south": (1, 0),
        "southwest": (1, -1),
        "west": (0, -1),
        "northwest": (-1, -1),
    }
    for direction, vector in directions.items():
        is_seat = False
        is_valid_coordinate = True
        steps = 1
        while is_seat is False and is_valid_coordinate is True:
            row_step, column_step = [coordinate * steps for coordinate in vector]
            current_row = row_num + row_step
            current_column = column_num + column_step
            is_valid_row = 0 <= current_row <= max_row
            is_valid_column = 0 <= current_column <= max_column
            is_valid_coordinate = is_valid_row and is_valid_column
            if is_valid_coordinate:
                current_value = seats[current_row][current_column]
                is_seat = current_value != "."
                if is_valid_coordinate and is_seat:
                    visible_seats.append(current_value)
                steps += 1
    return visible_seats


def apply_rules(seats: List[List[str]]) -> List[List[str]]:
    new_seats = copy.deepcopy(seats)
    for row_num, row in enumerate(seats):
        for column_num, value in enumerate(row):
            visible_seats = get_visible_seats(seats, (row_num, column_num))
            if value == "L" and not any(
                [visible_seat == "#" for visible_seat in visible_seats]
            ):
                new_seats[row_num][column_num] = "#"
            elif (
                value == "#"
                and len(
                    [
                        visible_seat
                        for visible_seat in visible_seats
                        if visible_seat == "#"
                    ]
                )
                >= 5
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


if __name__ == "__main__":
    print(count_occupied_seats(get_stable_arrangement(get_seats(SEATS_PATH))))
