import os

from conf import ROOT_DIR
from day_10.adapters_pt1 import count_step_sizes, get_step_sizes
from day_10.utils import get_adapters

SHORT_EXAMPLE_PATH = os.path.join(ROOT_DIR, "tests/day_10/short_example.csv")
SHORT_EXAMPLE_VALUES = get_adapters(SHORT_EXAMPLE_PATH)


def test_get_step_sizes():
    expected = [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]
    assert get_step_sizes(SHORT_EXAMPLE_VALUES) == expected


def test_count_step_sizes():
    expected = {1: 7, 3: 5}
    assert count_step_sizes(get_step_sizes(SHORT_EXAMPLE_VALUES)) == expected
