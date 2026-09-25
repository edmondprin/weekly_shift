def convert_to_minutes(shift_entry):
    hours_str, minutes_str = shift_entry.split(":")
    
    hours = int(hours_str)
    minutes = int(minutes_str)

    if 0 <= hours < 24 and 0 <= minutes < 60:
        return hours * 60 + minutes
    else:
        raise ValueError("Invalid time")
# Python automatically raises ValueError when unpacking or integer conversion fails
# important not to return integer or string in one single function, but integer or error raised to be caught and handled in another function

def calculate_daily_hours(
        morning_in,
        morning_out,
        afternoon_in,
        afternoon_out
):
    morning_start = convert_to_minutes(morning_in)
    morning_end = convert_to_minutes(morning_out)
    afternoon_start = convert_to_minutes(afternoon_in)
    afternoon_end = convert_to_minutes(afternoon_out)
    if (
        morning_end > morning_start 
        and afternoon_start >= morning_end 
        and afternoon_end > afternoon_start
    ):
        return (morning_end - morning_start) + (afternoon_end - afternoon_start)
    else:
        raise ValueError("Time invalid")

def gather_user_shift():
    shift_moments = ["morning start", "morning end", "afternoon start", "afternoon end"]
    user_shift = []
    for i in range(4):
        while True:
            user_shift.append(input(f"Enter the time you {'clocked in' if i % 2 == 0 else 'clocked out'} for your {shift_moments[i]}" ))
            



'''
if "__name__" == "__main__":
    print(calculate_daily_hours("08:30", "12:12", "14:23", "18:34"))
    print(calculate_daily_hours("08:30", "12:00", "12:00", "20:00")) # shift without lunch break
    print(calculate_daily_hours("08:00", "12:00", "11:25", "17:00"))
    print(calculate_daily_hours("08:30", "12:12", "14:23", "00:56"))
'''



