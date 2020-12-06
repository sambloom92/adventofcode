from typing import List, Set

from day_6.utils import get_total


def get_response_union(group: List[str]) -> Set:
    """
    return the union between all the individual responses within a group,
     i.e. all letters answered yes by anyone in the group
    :param group: list of responses for a group of passengers
    :return: the set representing the union of the responses
    """
    return {letter for response in group for letter in response}


if __name__ == "__main__":
    print(get_total(get_response_union))
