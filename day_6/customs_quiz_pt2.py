from typing import List, Set

from day_6.utils import get_total


def get_response_intersection(group: List[str]) -> Set:
    """
    return the intersection between all the individual responses within a group,
     i.e. all letters answered yes by everyone in the group
    :param group: list of responses for a group of passengers
    :return: the set representing the intersection of the responses
    """
    return set.intersection(*[set(response) for response in group])


if __name__ == "__main__":
    print(get_total(get_response_intersection))
