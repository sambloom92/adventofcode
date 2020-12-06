import os
from unittest.mock import patch

from conf import ROOT_DIR
from day_6.customs_quiz_pt1 import get_response_union
from day_6.utils import get_customs_responses, get_total


def test_get_customs_responses():
    example_responses_path = os.path.join(
        ROOT_DIR, "tests/day_6/example_customs_quiz.csv"
    )
    actual = get_customs_responses(example_responses_path)
    expected = [
        [
            "abc",
        ],
        ["a", "b", "c"],
        ["ab", "ac"],
        ["a", "a", "a", "a"],
        [
            "b",
        ],
    ]
    assert actual == expected


def test_get_total():
    example_responses_path = os.path.join(
        ROOT_DIR, "tests/day_6/example_customs_quiz.csv"
    )
    example_responses = get_customs_responses(example_responses_path)
    with patch("day_6.utils.get_customs_responses", return_value=example_responses):
        assert get_total(get_response_union) == 11
