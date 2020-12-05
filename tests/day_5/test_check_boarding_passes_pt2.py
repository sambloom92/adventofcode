from unittest.mock import DEFAULT, patch

import pytest

from day_5.check_boarding_passes_pt2 import (
    SeatNotFoundError,
    get_missing_row_ids,
    get_my_seat,
    get_possible_row_ids,
)


def test_get_possible_row_ids():
    actual = get_possible_row_ids(2, 4)
    expected = {0, 1, 2, 3, 8, 9, 10, 11}
    assert actual == expected


def test_get_missing_row_ids():
    possible = {0, 1, 2, 3, 8, 9, 10, 11}
    present = [
        "FFFFFFFLLL",
        "FFFFFFFLLR",
        "FFFFFFFLRL",
        "FFFFFFFLRR",
        "FFFFFFBLLL",
        "FFFFFFBLLR",
    ]
    with patch.multiple(
        "day_5.check_boarding_passes_pt2",
        get_possible_row_ids=DEFAULT,
        get_boarding_passes=DEFAULT,
    ) as mocks:
        mocks["get_possible_row_ids"].return_value = possible
        mocks["get_boarding_passes"].return_value = present
        assert get_missing_row_ids() == {10, 11}


def test_get_my_seat():
    possible = {0, 1, 2, 3, 8, 9, 10, 11}
    present = [
        "FFFFFFFLLL",
        "FFFFFFFLLR",
        "FFFFFFFLRL",
        "FFFFFFFLRR",
        "FFFFFFBLLL",
        "FFFFFFBLLR",
        "FFFFFFBLRL",
    ]
    with patch.multiple(
        "day_5.check_boarding_passes_pt2",
        get_possible_row_ids=DEFAULT,
        get_boarding_passes=DEFAULT,
    ) as mocks:
        mocks["get_possible_row_ids"].return_value = possible
        mocks["get_boarding_passes"].return_value = present
        assert get_my_seat() == 11


def test_get_my_seat_not_found():
    possible = {0, 1, 2, 3, 8, 9, 10, 11}
    present = [
        "FFFFFFFLLL",
        "FFFFFFFLLR",
        "FFFFFFFLRL",
        "FFFFFFFLRR",
        "FFFFFFBLLL",
        "FFFFFFBLLR",
        "FFFFFFBLRL",
        "FFFFFFBLRR",
    ]
    with patch.multiple(
        "day_5.check_boarding_passes_pt2",
        get_possible_row_ids=DEFAULT,
        get_boarding_passes=DEFAULT,
    ) as mocks:
        mocks["get_possible_row_ids"].return_value = possible
        mocks["get_boarding_passes"].return_value = present
        with pytest.raises(SeatNotFoundError):
            get_my_seat()
