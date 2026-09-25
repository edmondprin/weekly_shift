# validate + convert
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

# calculate
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

# interact with user
def gather_user_shift():
    shift_moments = ["morning start", "morning end", "afternoon start", "afternoon end"]
    user_shift = []
    for i in range(4):
        while True:
            user_input = input(f"Enter the time you {'clocked in' if i % 2 == 0 else 'clocked out'} for your {shift_moments[i]}: " )
            try:
                convert_to_minutes(user_input)
                user_shift.append(user_input)
                break
            except ValueError:
                print("Time invalid. Try again")
    return user_shift

# normalize
def format_time_entry(time_entry):
    if (
        len(time_entry) == 5
        and time_entry[2] == ":"
    ):
        return time_entry
    
    elif (
    time_entry.isdigit() 
    and len(time_entry) == 4
    ):
        new_time_entry = time_entry[:2] + ":" + time_entry[2:]
        return new_time_entry
    
    elif (
        len(time_entry) == 4
        and time_entry[0] != "0"
        and time_entry[1] == ":"
    ):
        new_time_entry = "0" + time_entry
        return new_time_entry
    else:
        return time_entry


print(format_time_entry("8:00"))
print(format_time_entry("08:00"))
print(format_time_entry("0800"))
print(format_time_entry(""))
print(format_time_entry("8"))

'''
if "__name__" == "__main__":
    print(calculate_daily_hours("08:30", "12:12", "14:23", "18:34"))
    print(calculate_daily_hours("08:30", "12:00", "12:00", "20:00")) # shift without lunch break
    print(calculate_daily_hours("08:00", "12:00", "11:25", "17:00"))
    print(calculate_daily_hours("08:30", "12:12", "14:23", "00:56"))
'''



