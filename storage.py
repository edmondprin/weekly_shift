# save/load shift data

import json

# json.dump()    Python → JSON file
# json.load()    JSON file → Python 
# For real persistence, the existing JSON needs to be loaded before we append.
# Start program > LOAD shifts.json > data = existing shifts > append new_shift > WRITE updated data back



# JSON file → Python data
def load_shifts():
    try:
        with open("shifts.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
# An empty file is not valid JSON


# new_shift = {
#     "date": "2026-10-02",
#     "morning_in": "09:00",
#     "morning_out": "13:00",
#     "afternoon_in": "13:00",
#     "afternoon_out": "18:00",
#     "total_minutes": 540
# }

# Python shift → persisted JS
def save_shift(new_shift):
    data = load_shifts()
    
    for index, shift in enumerate(data):
        if shift["date"] == new_shift["date"]:
            data[index] = new_shift
            break
    else:
        data.append(new_shift)
    
    with open("shifts.json", "w") as file:
        json.dump(data, file)




