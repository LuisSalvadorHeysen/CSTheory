import pytest
from main import aggregate_logs


# ✅ Valid inputs
@pytest.mark.parametrize("logs, expected", [
    (
        ["100 alice LOGIN", "101 bob QUERY", "102 alice QUERY", "103 alice LOGOUT", "104 bob LOGIN"],
        {"alice": {"LOGIN": 1, "LOGOUT": 1, "QUERY": 1},
         "bob": {"LOGIN": 1, "LOGOUT": 0, "QUERY": 1}}
    ),
    (
        ["200 alice LOGIN", "201 alice LOGIN"],
        {"alice": {"LOGIN": 2, "LOGOUT": 0, "QUERY": 0}}
    ),
    (
        ["300 bob QUERY", "301 bob QUERY", "302 bob QUERY"],
        {"bob": {"LOGIN": 0, "LOGOUT": 0, "QUERY": 3}}
    ),
])
def test_valid_inputs(logs, expected):
    assert aggregate_logs(logs) == expected


def test_empty_input():
    assert aggregate_logs([]) == {}


# ✅ Invalid inputs
def test_missing_action():
    # Missing the action field
    logs = ["100 john"]
    with pytest.raises(ValueError, match="missing action"):
        aggregate_logs(logs)


def test_invalid_action():
    # Action not in {LOGIN, LOGOUT, QUERY}
    logs = ["100 alice HACK"]
    with pytest.raises(ValueError):
        aggregate_logs(logs)
