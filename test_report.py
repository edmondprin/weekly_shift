from datetime import date

from report import format_minutes, calculate_weekly_minutes, get_current_week_shifts

def test_format_minutes():
    assert format_minutes(60) == "1h 0m"
    assert format_minutes(0) == "0h 0m"
    assert format_minutes(65) == "1h 5m"

def test_calculate_weekly_minutes():
    assert calculate_weekly_minutes([{"total_minutes": 20}, {"total_minutes": 40}]) == 60
    assert calculate_weekly_minutes([]) == 0

def test_get_current_week_shifts_valid():
    shifts = [
    {"date": "2026-09-25", "total_minutes": 400},  # previous week
    {"date": "2026-09-28", "total_minutes": 480},  # Monday
    {"date": "2026-10-01", "total_minutes": 450},  # Thursday
    {"date": "2026-10-04", "total_minutes": 200},  # Sunday
    {"date": "2026-10-05", "total_minutes": 500},  # next Monday
    ]
    expected =  [
        {'date': '2026-09-28', 'total_minutes': 480}, 
        {'date': '2026-10-01', 'total_minutes': 450}, 
        {'date': '2026-10-04', 'total_minutes': 200}
        ]
    result = get_current_week_shifts(shifts, date(2026, 10, 2)) 
    assert result == expected


def test_get_current_week_shifts_empty():
    # ARRANGE
    shifts = []
    expected = []

    # ACT
    result = get_current_week_shifts(shifts, date(2026, 10, 2))

    # ASSERT
    assert result == expected 
