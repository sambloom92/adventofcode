import re
from typing import Callable, Iterable, Tuple


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
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        letter = match.group(3)
        pw_value = match.group(4)
        return num1, num2, letter, pw_value
    else:
        raise UnexpectedLineFormat


def solver(validating_function: Callable[[str], bool]):
    """
    count how many lines have valid passwords
    :param validating_function: callable which checks whether a row is valid
    :return: final count
    """
    results = [line for line in get_data() if validating_function(line)]
    return len(results)
