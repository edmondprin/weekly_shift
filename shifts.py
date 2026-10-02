# gather/validate individual shift data

from datetime import date

def get_current_date():
    today = date.today().isoformat()
    return today

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



# normalize (does not raise error)
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
        time_entry.isdigit()
        and len(time_entry) == 3
    ):
        new_time_entry = "0" + time_entry[0] + ":" + time_entry[1:]
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
    
# interact with user (relies on convert_to_minutes which raises error)
def gather_user_shift():
    today = get_current_date()
    shift_moments = ["morning start", "morning end", "afternoon start", "afternoon end"]
    
    while True:
        raw_inputs = []
        for i in range(4):
            while True:
                action = 'clocked in' if i % 2 == 0 else 'clocked out'
                user_input = input(f"Enter the time you {action} for your {shift_moments[i]}: ")        
                formatted = format_time_entry(user_input)

                try:
                    convert_to_minutes(formatted)
                    raw_inputs.append(formatted)
                    break
                except ValueError:
                    print("Time invalid. Try again.")
        try:
            total_minutes_daily = calculate_daily_hours(*raw_inputs)
            break
        except ValueError:
            print("Time invalid. Try again")
    return {
        "date": today,
        "morning_in": raw_inputs[0],
        "morning_out": raw_inputs[1],
        "afternoon_in": raw_inputs[2],
        "afternoon_out": raw_inputs[3],
        "total_minutes": total_minutes_daily
    }

# if __name__ == "__main__":
#     print(gather_user_shift())




# new_list = gather_user_shift()

def format_daily_hours(daily_log):
    hours = daily_log // 60
    minutes = daily_log % 60
    return hours, minutes

# print(format_daily_hours(calculate_daily_hours(*new_list)))










