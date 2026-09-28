import pytest
from shifts import convert_to_minutes, calculate_daily_hours, format_time_entry, calculate_daily_hours, gather_user_shift

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

def test_format_time_entry():
    assert format_time_entry("900") == "09:00"
    assert format_time_entry("0730") == "07:30"
    assert format_time_entry("12:00") == "12:00"
    assert format_time_entry("6:00") == "06:00"
    assert format_time_entry("hello") == "hello"

def test_gather_user_input_valid(monkeypatch): # happy path
    responses = iter(["800", "1200", "13:00", "2000"])
    monkeypatch.setattr("builtins.input", lambda prompt:next(responses))
    response = gather_user_shift()

    assert response == {
        "morning_in": "08:00", 
        "morning_out": "12:00", 
        "afternoon_in": "13:00", 
        "afternoon_out": "20:00",
        "total_minutes": 660
    }

def test_gather_user_input_invalid(monkeypatch, capsys): # invalid individual input + recovery
    responses = iter(["hello", "0800", "1300", "15:00", "2000"])
    monkeypatch.setattr("builtins.input", lambda prompt:next(responses))
    response = gather_user_shift()
    captured = capsys.readouterr()
    assert "Time invalid. Try again." in captured.out
    assert response == {
        "morning_in": "08:00",
        "morning_out": "13:00",
        "afternoon_in": "15:00",
        "afternoon_out": "20:00",
        "total_minutes": 600 
    }

    def test_gather_user_input_invalid2(monkeypatch, capsys): # valid individual inputs but invalid overall shift + full-day recovery
        responses = iter(["08:00", "1200", "1100", "20:00", "08:00", "10:00", "11:00", "13:00"])
        monkeypatch.setattr("builtins.input", lambda prompt:next(responses))
        response = gather_user_shift()
        captured = capsys.readouterr()
        assert "Time invalid" in captured.out
        assert response == {
            "morning_in": "08:00",
            "morning_out": "10:00",
            "afternoon_in": "11:00",
            "afternoon_out": "13:00",
            "total_minutes": 240
        }