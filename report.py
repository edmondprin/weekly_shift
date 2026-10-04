# turn stored shift data into a report

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

# print(get_current_week_shifts(shifts, date(2026, 10, 2)))

def format_shift_line(shift):
    total_daily_time = format_minutes(shift["total_minutes"])
    return f"{shift['date']}: {shift['morning_in']}-{shift['morning_out']} | {shift['afternoon_in']}-{shift['afternoon_out']} - {total_daily_time}"

def build_weekly_report(shifts):
    weekly_shifts = []
    for shift in shifts:
        shift_line = format_shift_line(shift)
        weekly_shifts.append(shift_line)
    total_week_min = format_minutes(calculate_weekly_minutes(shifts))
    formatted_shifts =  "\n".join(weekly_shifts)if weekly_shifts else "No shifts recorded"
    # return formatted_shifts
    return f"Weekly Shift Report\n\n{formatted_shifts}\n\nWeekly total: {total_week_min}"
        

'''
my_new_shift = {
    "date": "2026-01-01", 
    "morning_in": "08:00",
    "morning_out": "09:00",
    "afternoon_in": "10:00",
    "afternoon_out": "11:00",
    "total_minutes": 120
}
'''

# print(format_shift_line(my_new_shift))

shifts = [
    {
        "date": "2026-10-01",
        "morning_in": "08:00",
        "morning_out": "12:00",
        "afternoon_in": "13:00",
        "afternoon_out": "17:30",
        "total_minutes": 510,
    },
    {
        "date": "2026-10-02",
        "morning_in": "08:00",
        "morning_out": "12:00",
        "afternoon_in": "13:00",
        "afternoon_out": "17:00",
        "total_minutes": 480,
    },
]

print(build_weekly_report(shifts))