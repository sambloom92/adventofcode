from typing import Dict

from day_4.utils import solver


def is_valid_entry(entry: Dict[str, str]) -> bool:
    """
    check if a password entry has all of the required fields
    :param entry: dictionary of fields (keys) and values
    :return:
    """
    mandatory_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]
    for field in mandatory_fields:
        if field not in entry.keys():
            return False
    return True


if __name__ == "__main__":
    print(solver(is_valid_entry))
