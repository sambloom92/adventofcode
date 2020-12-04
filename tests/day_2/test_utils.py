from unittest.mock import patch

from day_2.utils import get_data, parse_line, solver
from day_2.validate_password_pt1 import is_valid_password as is_valid_password_pt1


def test_get_data(tmpdir, password_policy_fixture_pt1):
    mock_data, _, _, _ = password_policy_fixture_pt1
    mock_file = tmpdir.join("mock_passwords.csv")
    for line in mock_data:
        mock_file.write(f"{line}\n", "a")
    assert [line.strip() for line in get_data(mock_file)] == mock_data


def test_parse_line(password_policy_fixture_pt1):
    (
        mock_data,
        parsed,
        _,
        _,
    ) = password_policy_fixture_pt1
    assert [parse_line(line) for line in mock_data] == parsed


def test_solver(password_policy_fixture_pt1):
    mock_data, _, _, total = password_policy_fixture_pt1
    with patch("day_2.utils.get_data", return_value=mock_data):
        assert solver(is_valid_password_pt1) == total
