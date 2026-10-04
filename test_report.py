from datetime import date

from report import format_minutes, calculate_weekly_minutes, get_current_week_shifts, build_weekly_report

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

def test_build_weekly_report_empty():
    shifts = []
    result = build_weekly_report(shifts)
    expected = f"Weekly Shift Report\n\nNo shifts recorded\n\nWeekly total: 0h 0m"
    assert result == expected

def test_build_weekly_report_valid():
    shifts = [
        {
        "date": "2026-10-05",
        "morning_in": "08:00",
        "morning_out": "09:00",
        "afternoon_in": "10:00",
        "afternoon_out": "11:00",
        "total_minutes": 120
    },
    {
            "date": "2026-10-06",
            "morning_in": "10:00",
            "morning_out": "11:00",
            "afternoon_in": "12:00",
            "afternoon_out": "13:30",
            "total_minutes": 150
        },
    ]
    result = build_weekly_report(shifts)
    expected = f"Weekly Shift Report\n\n2026-10-05: 08:00-09:00 | 10:00-11:00 - 2h 0m\n2026-10-06: 10:00-11:00 | 12:00-13:30 - 2h 30m\n\nWeekly total: 4h 30m"

    # f"Weekly Shift Report\n\n\n\nWeekly total: 0h 0m"
    assert result == expected


