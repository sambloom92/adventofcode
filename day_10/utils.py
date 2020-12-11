import os
from typing import List

from conf import ROOT_DIR

ADAPTERS_PATH = os.path.join(ROOT_DIR, "day_10/adapters.csv")


def get_adapters(filepath: str = ADAPTERS_PATH) -> List[int]:
    """
    read the file containing the exercise challenge data and return an iterable of the contents
    :param filepath: path to file
    :return: list of joltage values
    """
    with open(filepath) as file:
        adapters = sorted([int(line.strip()) for line in file.readlines()])
        adapters.append(max(adapters) + 3)
        adapters.insert(0, 0)
        return adapters
