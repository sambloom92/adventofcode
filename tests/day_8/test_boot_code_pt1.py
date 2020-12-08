import os

from conf import ROOT_DIR
from day_8.boot_code_pt1 import get_accumulator
from day_8.utils import get_boot_code

EXAMPLE_BOOT_CODE_PATH = os.path.join(ROOT_DIR, "tests/day_8/example_boot_code.txt")


def test_get_accumulator():
    example_boot_code = get_boot_code(EXAMPLE_BOOT_CODE_PATH)
    assert get_accumulator(example_boot_code) == 5
