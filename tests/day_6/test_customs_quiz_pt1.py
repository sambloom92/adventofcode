import pytest

from day_6.customs_quiz_pt1 import get_response_union


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("get_response_union(['abc', ])", {"a", "b", "c"}),
        ("get_response_union(['a', 'b', 'c'])", {"a", "b", "c"}),
        ("get_response_union(['ab', 'ac'])", {"a", "b", "c"}),
        ("get_response_union(['a', 'a', 'a', 'a'])", {"a"}),
        ("get_response_union(['b'])", {"b"}),
    ],
)
def test_get_response_union(test_input, expected):
    assert eval(test_input) == expected
