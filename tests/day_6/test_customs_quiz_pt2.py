import pytest

from day_6.customs_quiz_pt2 import get_response_intersection


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("get_response_intersection(['abc',])", {"a", "b", "c"}),
        ("get_response_intersection(['a', 'b', 'c'])", set()),
        ("get_response_intersection(['ab', 'ac'])", {"a"}),
        ("get_response_intersection(['a', 'a', 'a', 'a'])", {"a"}),
        ("get_response_intersection(['b'])", {"b"}),
    ],
)
def test_get_response_intersection(test_input, expected):
    assert eval(test_input) == expected
