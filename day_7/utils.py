import os
from typing import Dict, Union

from conf import ROOT_DIR

RULES_PATH = os.path.join(ROOT_DIR, "day_7/bag_rules.csv")


def get_bag_rules(filepath: str = RULES_PATH) -> Dict[str, str]:
    """
    read the file containing the exercise challenge data and return an iterable of the contents
    :param filepath: path to file
    :return: generator expression yielding bag rules
    """
    with open(filepath) as file:
        return {" ".join(line.split()[:2]): line for line in file.readlines()}


class Bag:
    def __init__(self, colour: str, all_rules: Dict[str, str]):
        self.colour = colour
        self.all_rules = all_rules
        self._parse_contents()

    def __repr__(self) -> str:
        return f"{self.colour} bag"

    @staticmethod
    def _parse_quantity(content: str) -> int:
        """
        parse the quantity from a given rule string
        :param content: the part of the rule string describing the contents
        :return: how many of a particular colour is contained
        """
        if content.strip() == "no other bags.":
            return 0
        else:
            quantity_str = content.split()[0]
            return int(quantity_str)

    @staticmethod
    def _parse_colour(content: str) -> Union[str, None]:
        """
        parse the colour from a given rule string
        :param content: the part of the rule string describing the contents
        :return: the colour of the bag described
        """
        if content.strip() == "no other bags.":
            return None
        else:
            return " ".join(content.split()[1:3])

    def _parse_contents(self):
        """
        build a dictionary of items and quantities contained within this bag
        """
        rule = self.all_rules[self.colour]
        rule_list = rule.split("contain", 1)[1].split(",")
        contents = {
            self._parse_colour(content): self._parse_quantity(content)
            for content in rule_list
        }
        if None in contents.keys():
            self.contents = None
        else:
            self.contents = contents

    def can_contain_shiny_gold(self) -> bool:
        """
        check if this bag can ultimately contain at least one shiny gold bag
        """
        if self.contents:
            if "shiny gold" in self.contents.keys():
                return True
            else:
                return any(
                    [
                        Bag(other_bag_colour, self.all_rules).can_contain_shiny_gold()
                        for other_bag_colour in self.contents.keys()
                    ]
                )
        else:
            return False
