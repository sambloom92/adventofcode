import os
from unittest.mock import patch

from conf import ROOT_DIR
from day_4.process_passports_pt1 import is_valid_entry as is_valid_entry_pt1
from day_4.utils import get_passports, solver


def test_get_passports():
    example_path = os.path.join(ROOT_DIR, "tests/day_4/example_passports_1.txt")
    expected = [
        {
            "ecl": "gry",
            "pid": "860033327",
            "eyr": "2020",
            "hcl": "#fffffd",
            "byr": "1937",
            "iyr": "2017",
            "cid": "147",
            "hgt": "183cm",
        },
        {
            "iyr": "2013",
            "ecl": "amb",
            "cid": "350",
            "eyr": "2023",
            "pid": "028048884",
            "hcl": "#cfa07d",
            "byr": "1929",
        },
        {
            "hcl": "#ae17e1",
            "iyr": "2013",
            "eyr": "2024",
            "ecl": "brn",
            "pid": "760753108",
            "byr": "1931",
            "hgt": "179cm",
        },
        {
            "hcl": "#cfa07d",
            "eyr": "2025",
            "pid": "166559648",
            "iyr": "2011",
            "ecl": "brn",
            "hgt": "59in",
        },
    ]
    assert get_passports(example_path) == expected


def test_solver_pt1():
    example_path = os.path.join(ROOT_DIR, "tests/day_4/example_passports_1.txt")
    examples = get_passports(example_path)
    with patch("day_4.utils.get_passports", return_value=examples):
        assert solver(is_valid_entry_pt1) == 2
