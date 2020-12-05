import re
from typing import Dict

from day_4.utils import solver


def is_valid_byr(value: str) -> bool:
    """check if byr is in range"""
    try:
        return 1920 <= int(value) <= 2002
    except ValueError:
        return False


def is_valid_iyr(value: str) -> bool:
    """check if iyr is in range"""
    try:
        return 2010 <= int(value) <= 2020
    except ValueError:
        return False


def is_valid_eyr(value: str) -> bool:
    """check if eyr is in range"""
    try:
        return 2020 <= int(value) <= 2030
    except ValueError:
        return False


def is_valid_hgt(value: str) -> bool:
    """check if hgt is formatted correctly and is in the correct range, given the unit"""
    match = re.fullmatch(r"([0-9]+)(cm|in)", value)
    if match:
        hgt = match.group(1)
        unit = match.group(2)
        if unit == "cm":
            return 150 <= int(hgt) <= 193
        else:
            return 59 <= int(hgt) <= 76
    else:
        return False


def is_valid_hcl(value: str) -> bool:
    """check if hcl has '#' followed by 6 alphanumeric characters"""
    if re.fullmatch(r"#[0-9a-f]{6}", value):
        return True
    else:
        return False


def is_valid_ecl(value: str) -> bool:
    """check if ecl is one of the valid values"""
    return value in (
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    )


def is_valid_pid(value: str) -> bool:
    """check if pid is a zero padded 9-digit number"""
    if re.fullmatch(r"[0-9]{9}", value):
        return True
    else:
        return False


def is_valid_entry(entry: Dict[str, str]) -> bool:
    """
    check if a password entry has all of the required fields
    and that the values are valid according to the data validation rules
    :param entry: dictionary of fields (keys) and values
    :return:
    """
    mandatory_fields = {
        "byr": is_valid_byr,
        "iyr": is_valid_iyr,
        "eyr": is_valid_eyr,
        "hgt": is_valid_hgt,
        "hcl": is_valid_hcl,
        "ecl": is_valid_ecl,
        "pid": is_valid_pid,
    }
    for field, rule in mandatory_fields.items():
        if field in entry.keys():
            if rule(entry[field]):
                pass
            else:
                return False
        else:
            return False
    return True


if __name__ == "__main__":
    print(solver(is_valid_entry))
