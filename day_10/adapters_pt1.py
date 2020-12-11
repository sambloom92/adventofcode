import os
from math import prod
from typing import Dict, Iterable, List, Set

from conf import ROOT_DIR
from day_10.utils import get_adapters


def get_step_sizes(input_values: Iterable[int]) -> List[int]:
    """
    list the differences between consecutive values
    :param input_values: ordered collection of values
    :return: sizes of the steps between values
    """
    values = [value for value in input_values]
    return [
        values[position + 1] - values[position] for position in range(len(values[1:]))
    ]


def count_step_sizes(step_sizes: List[int]) -> Dict[int, int]:
    """
    count the occurences of different step sizes
    :param step_sizes: collection of step_sizes
    :return: dictionary of step size counts
    """
    return {value: step_sizes.count(value) for value in set(step_sizes)}


if __name__ == "__main__":
    adapters = get_adapters(os.path.join(ROOT_DIR, "day_10/adapters.csv"))
    steps = get_step_sizes(adapters)
    counts = count_step_sizes(steps)
    print(prod(counts.values()))
