from itertools import combinations
from math import prod
from typing import Iterable


def get_report(filename: str = "report.csv") -> Iterable[int]:
    with open(filename) as file:
        return (int(line) for line in file.readlines())


def main():
    for pair in combinations(get_report(), 2):
        if sum(pair) == 2020:
            return prod(pair)


if __name__ == "__main__":
    print(main())
