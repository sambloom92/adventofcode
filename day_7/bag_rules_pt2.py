from typing import Union

from day_7.utils import Bag, get_bag_rules


def count_bags_contained_in_bag(colour: str) -> int:
    """
    count how many bags must be contained within a given colour of bag.
    recursively checks the colours contained within
    :param colour: colour of the bag to check
    :return: total bags contained within
    """
    bag = Bag(colour, get_bag_rules())
    counter = 0
    if bag.contents:
        for other_bag_colour, quantity in bag.contents.items():
            counter += quantity * (1 + count_bags_contained_in_bag(other_bag_colour))
    else:
        pass
    return counter


if __name__ == "__main__":
    print(count_bags_contained_in_bag("shiny gold"))
