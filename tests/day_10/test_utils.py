import os

from conf import ROOT_DIR
from day_10.utils import get_adapters


def test_get_adapters():
    short_example_path = os.path.join(ROOT_DIR, "tests/day_10/short_example.csv")
    expected = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
    assert get_adapters(short_example_path) == expected
