from unittest.mock import patch

from day_2.validate_passwords import get_data, is_valid_password, parse_line, solver


def test_get_data(tmpdir, password_policy_fixture):
    mock_data, _, _, _ = password_policy_fixture
    mock_file = tmpdir.join("mock_passwords.csv")
    for line in mock_data:
        mock_file.write(f"{line}\n", "a")
    assert [line.strip() for line in get_data(mock_file)] == mock_data


def test_parse_line(password_policy_fixture):
    (
        mock_data,
        parsed,
        _,
        _,
    ) = password_policy_fixture
    assert [parse_line(line) for line in mock_data] == parsed


def test_is_valid_password(password_policy_fixture):
    mock_data, _, answers, _ = password_policy_fixture
    assert [is_valid_password(line) for line in mock_data] == answers


def test_solver(password_policy_fixture):
    mock_data, _, _, total = password_policy_fixture
    with patch("day_2.validate_passwords.get_data", return_value=mock_data):
        assert solver() == total
