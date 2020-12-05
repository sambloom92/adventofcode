from day_5.utils import get_boarding_passes, parse_boarding_pass


def get_max_id() -> int:
    """
    calculate the highest row_id from all of the boarding passes
    :return: the highest row_id
    """
    passes = get_boarding_passes()
    row_ids = [parse_boarding_pass(row_id) for row_id in passes]
    return max(row_ids)


if __name__ == "__main__":
    print(get_max_id())
