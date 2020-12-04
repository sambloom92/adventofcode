import pytest


@pytest.fixture()
def password_policy_fixture_pt1():
    lines = [
        "1-1 a: onea",
        "1-2 a: twoa",
        "2-2 a: atwice",
        "3-4 o: toomanyooooooooos",
        "1-2 a: missingrequiredletter",
    ]
    parsed = [
        (1, 1, "a", "onea"),
        (1, 2, "a", "twoa"),
        (2, 2, "a", "atwice"),
        (3, 4, "o", "toomanyooooooooos"),
        (1, 2, "a", "missingrequiredletter"),
    ]
    answers = [True, True, False, False, False]
    total = 2
    return lines, parsed, answers, total


@pytest.fixture()
def password_policy_fixture_pt2():
    lines = [
        "1-2 a: aabbb",
        "1-2 a: abbbb",
        "1-2 a: babbb",
        "1-2 a: bbbbb",
        "2-4 a: babab",
        "2-4 a: babba",
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
        "1-3 a: toolong",
        "1-11 h: rightlength",
    ]

    parsed = [
        (1, 2, "a", "aabbb"),
        (1, 2, "a", "abbbb"),
        (1, 2, "a", "babbb"),
        (1, 2, "a", "bbbbb"),
        (2, 4, "a", "babab"),
        (2, 4, "a", "babba"),
        (1, 3, "a", "abcde"),
        (1, 3, "b", "cdefg"),
        (2, 9, "c", "ccccccccc"),
        (1, 9, "a", "tooshort"),
        (
            1,
            11,
            "h",
            "rightlength",
        ),
    ]
    answers = [False, True, True, False, False, True, True, False, False, False, True]
    total = 3
    return lines, parsed, answers, total
