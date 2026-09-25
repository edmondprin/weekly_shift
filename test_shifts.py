import pytest
from shifts import convert_to_minutes, calculate_daily_hours

def test_convert_to_minutes_valid():
    assert convert_to_minutes("08:45") == 525
    assert convert_to_minutes("00:00") == 0
    assert convert_to_minutes("02:00") == 120

def test_convert_to_minutes_invalid():
    with pytest.raises(ValueError):
        convert_to_minutes("24:00")
    with pytest.raises(ValueError):
        convert_to_minutes("12:60")
    with pytest.raises(ValueError):
        convert_to_minutes("Hello")

def test_calculate_daily_hours_valid():
    assert calculate_daily_hours("08:00", "12:00", "13:00", "17:00") == 480
    assert calculate_daily_hours("09:00", "15:00", "15:00", "20:00") == 660 # edge case

def test_calculate_daily_hours_invalid():
    with pytest.raises(ValueError):
        calculate_daily_hours("08:00", "12:00", "11:45", "18:00")
    with pytest.raises(ValueError):
        calculate_daily_hours("hello", "12:00", "13:00", "20:00")
    with pytest.raises(ValueError):
        calculate_daily_hours("12:00", "08:00", "13:00", "17:00") # edge case