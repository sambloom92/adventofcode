import os
from unittest.mock import patch

import pytest

from conf import ROOT_DIR
from day_9.utils import get_numbers
from day_9.xmas_cypher_pt2 import solver_pt2, sum_min_max

EXAMPLE_CYPHER_PATH = os.path.join(ROOT_DIR, "tests/day_9/example_cypher.csv")


def test_solver():
    example_numbers = get_numbers(EXAMPLE_CYPHER_PATH)
    with patch("day_9.xmas_cypher_pt2.solver_pt1", return_value=127):
        assert solver_pt2(example_numbers) == 62


@pytest.mark.parametrize(
    "test_inputs,expected",
    [
        ("sum_min_max([1, 2, 3, 4])", 5),
        ("sum_min_max([4, 3, 2, 1])", 5),
    ],
)
def test_sum_min_max(test_inputs, expected):
    assert eval(test_inputs) == expected
