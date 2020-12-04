from unittest.mock import patch

import pytest

from day_1.utils import SolutionNotFoundError, get_report, solver


def test_get_report(tmpdir, report_fixture_pt1):
    mock_data, _ = report_fixture_pt1
    mock_file = tmpdir.join("mock_report.csv")
    for num in mock_data:
        mock_file.write(f"{num}\n", "a")
    assert [num for num in get_report(mock_file)] == mock_data


def test_solver_pt1(report_fixture_pt1):
    mock_data, answer = report_fixture_pt1
    with patch("day_1.utils.get_report", return_value=mock_data):
        assert solver(2) == answer


def test_solver_pt1_error(report_fixture_pt1_no_solution):
    mock_data = report_fixture_pt1_no_solution
    with patch("day_1.utils.get_report", return_value=mock_data):
        with pytest.raises(SolutionNotFoundError):
            solver(2)


def test_solver_pt2(report_fixture_pt2):
    mock_data, answer = report_fixture_pt2
    with patch("day_1.utils.get_report", return_value=mock_data):
        assert solver(3) == answer


def test_solver_pt2_error(report_fixture_pt2_no_solution):
    mock_data = report_fixture_pt2_no_solution
    with patch("day_1.utils.get_report", return_value=mock_data):
        with pytest.raises(SolutionNotFoundError):
            solver(3)
