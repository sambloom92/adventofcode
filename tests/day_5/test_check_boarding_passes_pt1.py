import os
from unittest.mock import patch

from conf import ROOT_DIR
from day_5.check_boarding_passes_pt1 import get_max_id
from day_5.utils import get_boarding_passes


def test_get_max_id():
    example_filepath = os.path.join(ROOT_DIR, "tests/day_5/example_boarding_passes.csv")
    example_boarding_passes = get_boarding_passes(example_filepath)
    with patch(
        "day_5.check_boarding_passes_pt1.get_boarding_passes",
        return_value=example_boarding_passes,
    ):
        assert get_max_id() == 820
