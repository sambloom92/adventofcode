import os
from itertools import combinations
from math import prod
from typing import Iterable, List

from conf import ROOT_DIR
from day_10.adapters_pt1 import get_step_sizes
from day_10.utils import get_adapters


def split_into_sublists(input_values: List[int]) -> List[List[int]]:
    """
    split an ordered list of values into sublists, splitting anywhere where two values are separated by 3
    :param input_values: ordered list of values
    :return: a list of sublists where the values in each list are all separated by 1
    """
    steps = get_step_sizes(input_values)
    sublist_cuts = [index for index, value in enumerate(steps) if value == 3]
    sublists = []
    for index, cut in enumerate(sublist_cuts):
        cut_end = cut + 1
        if index > 0:
            cut_start = sublist_cuts[index - 1] + 1
        else:
            cut_start = 0
        sublists.append(input_values[cut_start:cut_end])
    sublists[-1].append(input_values[-1])
    return sublists


def is_valid_arrangement(arrangement: Iterable[int]) -> bool:
    """
    check if an ordered collection of values is a valid arrangement, i.e. there are no steps of more than 3
    :param arrangement: ordered collection of values
    :return: whether the arrangement is valid
    """
    return not any([step_size > 3 for step_size in get_step_sizes(arrangement)])


def count_arrangements(input_values: List[int]):
    """
    count how many valid arrangements can be made for a given list of values.
    the arrangement must start and end the same as the original list and must not contain steps of more than 3
    the original list also counts as a valid arrangement.
    lists of 2 or less can only have 1 valid arrangement.
    :param input_values: ordered list of values
    :return: how many valid arrangements are possible for the given input
    """
    if len(input_values) > 2:
        start = [input_values[0]]
        end = [input_values[-1]]
        middle = input_values[1:-1]
        arrangement_count = 0
        for length in range(len(middle) + 1):
            for middle_arrangement in combinations(middle, length):
                arrangement = start + [num for num in middle_arrangement] + end
                if is_valid_arrangement(arrangement):
                    arrangement_count += 1
    else:
        arrangement_count = 1
    return arrangement_count


def calculate_total_arrangements(input_values: List[int]) -> int:
    """
    calculate the total arrangements as the product of the number of arrangements for each sublist
    :param input_values: ordered list of values
    :return: the total number of arrangements
    """
    sublists = split_into_sublists(input_values)
    return prod([count_arrangements(sublist) for sublist in sublists])


if __name__ == "__main__":
    joltages = get_adapters(os.path.join(ROOT_DIR, "day_10/adapters.csv"))
    print(calculate_total_arrangements(joltages))
