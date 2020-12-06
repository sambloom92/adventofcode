import os
from typing import Callable, List

from conf import ROOT_DIR

CUSTOMS_PATH = os.path.join(ROOT_DIR, "day_6/customs_responses.csv")


def get_customs_responses(filepath: str = CUSTOMS_PATH) -> List[List[str]]:
    """
    read the file containing the exercise challenge data and return an iterable of the contents
    :param filepath: path to file
    :return: generator expression yielding customs responses
    """
    with open(filepath) as file:
        return [passport.split() for passport in file.read().split("\n\n")]


def get_total(set_function: Callable) -> int:
    """
    sum the lengths of the set for each group
    :param set_function: callable used to determine how to create the set
    :return: total sum of the set lengths
    """
    return sum([len(set_function(group)) for group in get_customs_responses()])
