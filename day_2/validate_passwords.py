import re
from typing import Iterable, Tuple


def get_data(filename: str = "password_policy.csv") -> Iterable[str]:
    """
    read the file containing the exercise challenge data and return an iterable of the contents as strings
    :param filename: relative path
    :return: generator expression yielding strings
    """
    with open(filename) as file:
        return (line for line in file.readlines())


class UnexpectedLineFormat(Exception):
    pass


def parse_line(line: str) -> Tuple[int, int, str, str]:
    """
    parse the line into the distinct components of the policy and password value
    :param line: line of text containing password and policy
    :return: parsed components
    """
    pattern = re.compile(r"([0-9]+)-([0-9]+)\s([a-zA-Z]):\s([a-zA-Z]+)")
    match = pattern.match(line)
    if match:
        minimum = int(match.group(1))
        maximum = int(match.group(2))
        letter = match.group(3)
        pw_value = match.group(4)
        return minimum, maximum, letter, pw_value
    else:
        raise UnexpectedLineFormat


def is_valid_password(line) -> bool:
    """
    check if a particular line contains a valid password
    :param line: line of text containing password and policy
    :return: whether the password is valid according to its policy
    """
    minimum, maximum, letter, pw_value = parse_line(line)
    return minimum <= pw_value.count(letter) <= maximum


def solver():
    """
    count how many lines have valid passwords
    :return: final count
    """
    results = [line for line in get_data() if is_valid_password(line)]
    return len(results)


if __name__ == "__main__":
    print(solver())
