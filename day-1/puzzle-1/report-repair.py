from itertools import combinations
from math import prod


with open('report.csv') as file:
    REPORT = (int(line) for line in file.readlines())


def main():
    for pair in combinations(REPORT, 2):
        if sum(pair) == 2020:
            return prod(pair)


if __name__ == "__main__":
    print(main())
