import os
from unittest.mock import patch

from conf import ROOT_DIR
from day_7.bag_rules_pt1 import count_bags_that_can_contain_shiny_gold
from day_7.utils import get_bag_rules


def test_count_bags_that_can_contain_shiny_gold():
    example_path = os.path.join(ROOT_DIR, "tests/day_7/example_bag_rules_1.csv")
    example_rules = get_bag_rules(example_path)
    with patch("day_7.bag_rules_pt1.get_bag_rules", return_value=example_rules):
        assert count_bags_that_can_contain_shiny_gold() == 4
