from report import format_minutes, calculate_weekly_minutes

def test_format_minutes():
    assert format_minutes(60) == "1h 0m"
    assert format_minutes(0) == "0h 0m"
    assert format_minutes(65) == "1h 5m"

def test_calculate_weekly_minutes():
    assert calculate_weekly_minutes([{"total_minutes": 20}, {"total_minutes": 40}]) == 60
    assert calculate_weekly_minutes([]) == 0