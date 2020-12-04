import pytest


@pytest.fixture()
def password_policy_fixture():
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
