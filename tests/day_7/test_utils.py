import os

import pytest

from conf import ROOT_DIR
from day_7.utils import Bag, get_bag_rules


def test_get_bag_rules():
    example_path = os.path.join(ROOT_DIR, "tests/day_7/example_bag_rules_1.csv")
    actual = get_bag_rules(example_path)
    expected = {
        "light red": "light red bags contain 1 bright white bag, 2 muted yellow bags.\n",
        "dark orange": "dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n",
        "bright white": "bright white bags contain 1 shiny gold bag.\n",
        "muted yellow": "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n",
        "shiny gold": "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n",
        "dark olive": "dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n",
        "vibrant plum": "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n",
        "faded blue": "faded blue bags contain no other bags.\n",
        "dotted black": "dotted black bags contain no other bags.",
    }
    assert actual == expected


EXAMPLE_PATH = os.path.join(ROOT_DIR, "tests/day_7/example_bag_rules_1.csv")
EXAMPLE_RULES = get_bag_rules(EXAMPLE_PATH)
BAG = Bag("shiny gold", EXAMPLE_RULES)


def test_bag_all_rules():
    assert BAG.all_rules == EXAMPLE_RULES


def test_bag_colour():
    assert BAG.colour == "shiny gold"


def test_bag_contents():
    assert BAG.contents == {"dark olive": 1, "vibrant plum": 2}


def test_bag_parse_colour():
    assert BAG._parse_colour("1 dark olive bag") == "dark olive"


def test_bag_parse_colour_none():
    assert BAG._parse_colour("no other bags.") is None


def test_bag_parse_quantity():
    assert BAG._parse_quantity("1 dark olive bag") == 1


def test_bag_parse_quantity_none():
    assert BAG._parse_quantity("no other bags.") == 0


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Bag('shiny gold', EXAMPLE_RULES).can_contain_shiny_gold()", False),
        ("Bag('light red', EXAMPLE_RULES).can_contain_shiny_gold()", True),
        ("Bag('dark orange', EXAMPLE_RULES).can_contain_shiny_gold()", True),
        ("Bag('bright white', EXAMPLE_RULES).can_contain_shiny_gold()", True),
        ("Bag('muted yellow', EXAMPLE_RULES).can_contain_shiny_gold()", True),
    ],
)
def test_bag_can_contain_shiny_gold(test_input, expected):
    assert eval(test_input) == expected
