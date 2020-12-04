import pytest


@pytest.fixture()
def report_fixture_pt1():
    return [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ], 514579


@pytest.fixture()
def report_fixture_pt1_no_solution():
    return [
        1722,
        979,
        366,
        299,
        675,
        1456,
    ]


@pytest.fixture()
def report_fixture_pt2():
    return [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ], 241861950


@pytest.fixture()
def report_fixture_pt2_no_solution():
    return [
        1722,
        979,
        366,
        299,
        676,
        1456,
    ]
