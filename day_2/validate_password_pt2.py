from day_2.utils import parse_line, solver


def is_valid_password(line: str) -> bool:
    """
    check if a particular line contains a valid password
    :param line: line of text containing password and policy
    :return: whether the password is valid according to its policy
    """
    first_pos, second_pos, letter, pw_value = parse_line(line)
    length = len(pw_value)
    if first_pos <= length >= second_pos:
        return (pw_value[first_pos - 1] == letter) ^ (
            pw_value[second_pos - 1] == letter
        )
    else:
        return False


if __name__ == "__main__":
    print(solver(is_valid_password))
