import os
from itertools import combinations
from typing import List

from conf import ROOT_DIR
from day_9.utils import NoSolutionError, get_numbers, get_window, is_sum

CYPHER_PATH = os.path.join(ROOT_DIR, "day_9/xmas_cypher.csv")


def solver(cypher: List[int], preamble_length: int = 25) -> int:
    """
    find the first number for which no pair of numbers in the preamble sum to its value
    :param cypher: ordered list of numbers
    :param preamble_length: length of the preceeding list of numbers
    :return: value of the first number which breaks the rule
    """
    for index in range(len(cypher)):
        window = get_window(cypher, index, preamble_length + 1)
        current_number = window[-1]
        preamble = set(window[:-1])
        if any([is_sum(pair, current_number) for pair in combinations(preamble, 2)]):
            pass
        else:
            return current_number
    raise NoSolutionError()


if __name__ == "__main__":
    print(solver(get_numbers()))
