import os

import pytest

from conf import ROOT_DIR
from day_5.utils import (
    get_boarding_passes,
    get_row_id,
    parse_boarding_pass,
    parse_to_decimal,
)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("get_row_id(44, 5)", 357),
        ("get_row_id(70, 7)", 567),
        ("get_row_id(14, 7)", 119),
        ("get_row_id(102, 4)", 820),
    ],
)
def test_get_row_id(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("parse_to_decimal('FBFBBFF')", 44),
        ("parse_to_decimal('BFFFBBF')", 70),
        ("parse_to_decimal('FFFBBBF')", 14),
        ("parse_to_decimal('BBFFBBF')", 102),
        ("parse_to_decimal('RLR')", 5),
        ("parse_to_decimal('RRR')", 7),
        ("parse_to_decimal('RLL')", 4),
    ],
)
def test_parse_to_decimal(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("parse_boarding_pass('FBFBBFFRLR')", 357),
        ("parse_boarding_pass('BFFFBBFRRR')", 567),
        ("parse_boarding_pass('FFFBBBFRRR')", 119),
        ("parse_boarding_pass('BBFFBBFRLL')", 820),
    ],
)
def test_parse_boarding_pass(test_input, expected):
    assert eval(test_input) == expected


def test_get_boarding_passes():
    example_filepath = os.path.join(ROOT_DIR, "tests/day_5/example_boarding_passes.csv")
    expected = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    actual = [boarding_pass for boarding_pass in get_boarding_passes(example_filepath)]
    assert actual == expected
