from day_2.utils import parse_line, solver


def is_valid_password(line: str) -> bool:
    """
    check if a particular line contains a valid password
    :param line: line of text containing password and policy
    :return: whether the password is valid according to its policy
    """
    minimum, maximum, letter, pw_value = parse_line(line)
    return minimum <= pw_value.count(letter) <= maximum


if __name__ == "__main__":
    print(solver(is_valid_password))
