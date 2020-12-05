import os

from conf import ROOT_DIR
from day_4.process_passports_pt1 import is_valid_entry
from day_4.utils import get_passports


def test_is_valid_entry():
    example_path = os.path.join(ROOT_DIR, "tests/day_4/example_passports_1.txt")
    examples = get_passports(example_path)
    results = [is_valid_entry(example) for example in examples]
    assert results == [True, False, True, False]
