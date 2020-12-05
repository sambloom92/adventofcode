from itertools import product
from typing import Set

from day_5.utils import get_boarding_passes, get_row_id, parse_boarding_pass


def get_possible_row_ids(n_rows: int = 128, n_cols: int = 8) -> Set[int]:
    """
    get all possible pairings of row number and column number for given ranges
    :param n_rows: how many rows
    :param n_cols: how many columns
    :return: a set of all possible row_ids corresponding to the possible pairings
    """
    return set(
        get_row_id(row, col) for row, col in product(range(n_rows), range(n_cols))
    )


def get_missing_row_ids() -> Set[int]:
    """
    find which row_ids are not present in the sample
    :return: a set of all missing row_ids
    """
    passes = get_boarding_passes()
    existing_row_ids = {parse_boarding_pass(row_id) for row_id in passes}
    return get_possible_row_ids() - existing_row_ids


class SeatNotFoundError(Exception):
    pass


def get_my_seat() -> int:
    """
    find the seat which is missing from the sample but who's immediate neighbours are not
    :return: my seat
    """
    candidate_seats = get_missing_row_ids()
    for row_id in candidate_seats:
        if row_id + 1 not in candidate_seats and row_id - 1 not in candidate_seats:
            return row_id
    else:
        raise SeatNotFoundError


if __name__ == "__main__":
    print(get_my_seat())
