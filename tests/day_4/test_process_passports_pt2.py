import pytest

from day_4.process_passports_pt2 import (
    is_valid_byr,
    is_valid_ecl,
    is_valid_entry,
    is_valid_eyr,
    is_valid_hcl,
    is_valid_hgt,
    is_valid_iyr,
    is_valid_pid,
)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("is_valid_byr('1900')", False),
        ("is_valid_byr('1920')", True),
        ("is_valid_byr('1970')", True),
        ("is_valid_byr('2002')", True),
        ("is_valid_byr('2020')", False),
        ("is_valid_byr('abdc')", False),
    ],
)
def test_is_valid_byr(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("is_valid_iyr('2000')", False),
        ("is_valid_iyr('2010')", True),
        ("is_valid_iyr('2015')", True),
        ("is_valid_iyr('2020')", True),
        ("is_valid_iyr('2030')", False),
        ("is_valid_iyr('abdc')", False),
    ],
)
def test_is_valid_iyr(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("is_valid_eyr('2010')", False),
        ("is_valid_eyr('2020')", True),
        ("is_valid_eyr('2025')", True),
        ("is_valid_eyr('2030')", True),
        ("is_valid_eyr('2040')", False),
        ("is_valid_eyr('abdc')", False),
    ],
)
def test_is_valid_eyr(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("is_valid_hgt('100cm')", False),
        ("is_valid_hgt('150cm')", True),
        ("is_valid_hgt('170cm')", True),
        ("is_valid_hgt('193cm')", True),
        ("is_valid_hgt('200cm')", False),
        ("is_valid_hgt('10in')", False),
        ("is_valid_hgt('59in')", True),
        ("is_valid_hgt('65in')", True),
        ("is_valid_hgt('76in')", True),
        ("is_valid_hgt('200in')", False),
        ("is_valid_hgt('200')", False),
    ],
)
def test_is_valid_hgt(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("is_valid_hcl('#abc123')", True),
        ("is_valid_hcl('abc123')", False),
        ("is_valid_hcl('#abc12345')", False),
        ("is_valid_hcl('#abc12')", False),
        ("is_valid_hcl('#abcdef')", True),
        ("is_valid_hcl('#123456')", True),
    ],
)
def test_is_valid_hcl(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("is_valid_ecl('amb')", True),
        ("is_valid_ecl('blu')", True),
        ("is_valid_ecl('brn')", True),
        ("is_valid_ecl('gry')", True),
        ("is_valid_ecl('grn')", True),
        ("is_valid_ecl('hzl')", True),
        ("is_valid_ecl('oth')", True),
        ("is_valid_ecl('abc')", False),
    ],
)
def test_is_valid_ecl(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("is_valid_pid('0123456789')", False),
        ("is_valid_pid('012345678')", True),
        ("is_valid_pid('01234567a')", False),
        ("is_valid_pid('123456789')", True),
    ],
)
def test_is_valid_pid(test_input, expected):
    assert eval(test_input) == expected
