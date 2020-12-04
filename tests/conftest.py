import pytest


@pytest.fixture()
def report_fixture():
    return [1, 2, 3, 4, 5, 2000, 6, 20, 7, 8, 9], 2000 * 20


@pytest.fixture()
def report_fixture_no_solution():
    return [1, 2, 3, 4, 5, 2000, 6, 21, 7, 8, 9]
