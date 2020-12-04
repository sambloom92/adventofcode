from day_2.validate_password_pt2 import is_valid_password


def test_is_valid_password(password_policy_fixture_pt2):
    mock_data, _, answers, _ = password_policy_fixture_pt2
    assert [is_valid_password(line) for line in mock_data] == answers
