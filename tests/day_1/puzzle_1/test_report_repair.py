from unittest.mock import patch

import pytest

from day_1.puzzle_1.report_repair import SolutionNotFoundError, get_report, main


def test_get_report(tmpdir, report_fixture):
    mock_data, _ = report_fixture
    mock_file = tmpdir.join("mock_report.csv")
    for num in mock_data:
        mock_file.write(f"{num}\n", "a")
    assert [num for num in get_report(mock_file)] == mock_data


def test_main(report_fixture):
    mock_data, answer = report_fixture
    with patch("day_1.puzzle_1.report_repair.get_report", return_value=mock_data):
        assert main() == answer


def test_main_error(report_fixture_no_solution):
    mock_data = report_fixture_no_solution
    with patch("day_1.puzzle_1.report_repair.get_report", return_value=mock_data):
        with pytest.raises(SolutionNotFoundError):
            main()
