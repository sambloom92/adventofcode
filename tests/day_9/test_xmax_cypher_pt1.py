import os

from conf import ROOT_DIR
from day_9.utils import get_numbers
from day_9.xmax_cypher_pt1 import solver

EXAMPLE_CYPHER_PATH = os.path.join(ROOT_DIR, "tests/day_9/example_cypher.csv")


def test_solver():
    example_numbers = get_numbers(EXAMPLE_CYPHER_PATH)
    assert solver(example_numbers, 5) == 127
