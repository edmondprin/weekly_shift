from datetime import date, timedelta

def calculate_weekly_minutes(shifts):
    total = 0
    for shift in shifts:
        total += shift["total_minutes"]
    return total

shifts = [
    {"date": "2026-09-25", "total_minutes": 400},  # previous week
    {"date": "2026-09-28", "total_minutes": 480},  # Monday
    {"date": "2026-10-01", "total_minutes": 450},  # Thursday
    {"date": "2026-10-04", "total_minutes": 200},  # Sunday
    {"date": "2026-10-05", "total_minutes": 500},  # next Monday
]

# print(calculate_weekly_minutes(my_shifts))


def format_minutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours}h {minutes}m"

# total_minutes = calculate_weekly_minutes(my_shifts)
# print(format_minutes(total_minutes))

# Passing the date as an argument makes that dependency explicit
# Functions to be independent of system clock
def get_week_start(my_date):
    day_number = my_date.weekday()
    first_weekday = my_date - timedelta(days=day_number)
    return first_weekday # returns date object 

# date.isoformat() date object -> ISO string: 
# date.fromisoformat(): ISO string -> date object

# receive list → filter list → return list
def get_current_week_shifts(shifts, my_date):
    week_start = get_week_start(my_date)
    # print(f"Week start: {week_start}")
    week_end = week_start + timedelta (days = 6)
    # print(f"Week end: {week_end}")
    current_week = []
    for shift in shifts:
        date_obj = date.fromisoformat(shift["date"])
        if week_start <= date_obj <= week_end:
            current_week.append(shift)
    return current_week

print(get_current_week_shifts(shifts, date(2026, 10, 2)))