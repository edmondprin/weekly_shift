# happy path → boundary → invalid value → invalid type

# 1 day   = 1,440 minutes
# 1 month = 30 days
# 1 year  = 365 days

# calculation / structured data
def decompose(my_time):
    if not isinstance(my_time, (int, float)):
        raise TypeError("Time must be a number")  
    if my_time <= 0:
        raise ValueError("Time must be a positive value")
    
    minutes_per_year = 1440 * 365
    minutes_per_month = 1440 * 30
    minutes_per_day = 24 * 60
    years = my_time // minutes_per_year 
    remaining_minutes = my_time % minutes_per_year 
    months = remaining_minutes // minutes_per_month
    remaining_minutes = remaining_minutes % minutes_per_month
    days = remaining_minutes // minutes_per_day
    remaining_minutes = remaining_minutes % minutes_per_day
    hours = remaining_minutes // 60
    minutes = remaining_minutes % 60 
    return {
            "years": years,
            "months": months,
            "days": days,
            "hours": hours,
            "minutes": minutes
        }

# 9 year(s), 1 month(s), 3 day(s)
# year_text = f"{years} year(s)" if years > 0 else ""
# f"{value_if_true if condition else value_if_false}"

# presentation / human-readable string
def format_duration(duration_dict):
    parts = []
    years = duration_dict["years"]
    if years > 0:
        parts.append(f"{years} year{'s' if years != 1 else ''}")
    months = duration_dict["months"]
    if months > 0:
        parts.append(f"{months} month{'s' if months != 1 else ''}")
    days = duration_dict["days"]
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    hours = duration_dict["hours"]
    parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    minutes = duration_dict["minutes"]
    parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    return ", ".join(parts) 
# join() puts ", " between existing elements only


if __name__ == "__main__":         
    my_time = decompose(2000)
    print(format_duration(my_time))



'''
years = time // minutes_per_year | 600,000 // 525,600 = 1
remaining_minutes = time % minutes_per_year | 600,000 % 525,600 = 74,400

months = remaining_minutes // minutes_per_month | 74,400 // 43,200 = 1
remaining_minutes = remaining_minutes % minutes_per_month | 74,400 % 43200 = 31200

days = remaining_minutes // minutes_per_day | 31,200 // 1,440 = 21
remaining_minutes = remaining_minutes % minutes_per_day | 31200 % 1,440 = 960

hours = remaining_minutes // 60 | 960 // 60 = 16
minutes = remaining_minutes % 60 | 960 % 60 = 0
'''

# other function that formats the length of time 
# 1 year(s), 2 month(s), 3 day(s), 4 hour(s), 5 minute(s)
