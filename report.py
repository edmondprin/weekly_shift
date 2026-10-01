

def calculate_weekly_minutes(shifts):
    total = 0
    for shift in shifts:
        total += shift["total_minutes"]
    return total

my_shifts = [
    {"date": "2026-09-28", "total_minutes": 480},
    {"date": "2026-09-29", "total_minutes": 510},
    {"date": "2026-09-30", "total_minutes": 450},
]

# print(calculate_weekly_minutes(my_shifts))


def format_minutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours}h {minutes}m"

total_minutes = calculate_weekly_minutes(my_shifts)
print(format_minutes(total_minutes))