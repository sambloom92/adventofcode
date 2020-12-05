import os
from typing import Callable, Dict, List

from conf import ROOT_DIR

PASSPORT_PATH = os.path.join(ROOT_DIR, "day_4/passports.txt")


def get_passports(filepath: str = PASSPORT_PATH) -> List[Dict[str, str]]:
    """
    read the file containing the exercise challenge data and return an iterable of the contents
    :param filepath: path to file
    :return: generator expression yielding passport entries
    """
    with open(filepath) as file:
        return [
            {field.split(":")[0]: field.split(":")[1] for field in passport.split()}
            for passport in file.read().split("\n\n")
        ]


def solver(validating_function: Callable[[Dict[str, str]], bool]) -> int:
    """
    count how many passports are valid
    :param validating_function: callable which checks whether a passport is valid
    :return: final count
    """
    results = [line for line in get_passports() if validating_function(line)]
    return len(results)
