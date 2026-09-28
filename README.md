# Shift Email Automation

A Python command-line project for recording daily work shifts, calculating hours worked, and eventually generating and emailing a weekly hours report.

The project is also an exercise in building a small Python application with clear separation of concerns, input validation, exception handling, and automated testing with pytest.

## Current Features

- Accepts morning and afternoon clock-in/clock-out times
- Supports multiple time-entry formats:
  - `08:00`
  - `8:00`
  - `0800`
  - `800`
- Normalizes time entries to `HH:MM`
- Validates hours and minutes
- Detects invalid or overlapping shifts
- Retries when invalid input is entered
- Calculates daily working time in minutes
- Returns daily shift information as structured data
- Includes pytest coverage for validation, calculations, user input, and retry behavior

## Example

A user can enter:

```text
Enter the time you clocked in for your morning start: 800
Enter the time you clocked out for your morning end: 1200
Enter the time you clocked in for your afternoon start: 1300
Enter the time you clocked out for your afternoon end: 1700
```

The program normalizes and processes the shift as:

```python
{
    "morning_in": "08:00",
    "morning_out": "12:00",
    "afternoon_in": "13:00",
    "afternoon_out": "17:00",
    "total_minutes": 480
}
```

## Project Structure

The application currently separates several responsibilities:

- `format_time_entry()` — normalizes different time-entry formats
- `convert_to_minutes()` — validates a time and converts it to minutes
- `calculate_daily_hours()` — validates shift chronology and calculates total working time
- `gather_user_shift()` — handles user interaction and retries invalid entries

This separation makes the individual components easier to test and maintain.

## Testing

The project uses `pytest`.

Current tests cover:

- Valid and invalid time conversion
- Time-entry normalization
- Daily-hours calculations
- Invalid and overlapping shifts
- Simulated user input with `monkeypatch`
- Error-message output with `capsys`
- Recovery and retry behavior after invalid input

Run the tests with:

```bash
pytest -v
```

## Planned Features

The next stages of the project are:

- Associate each shift with a date
- Store daily shift data between program executions
- Calculate weekly hours
- Format minutes as hours and minutes
- Generate a weekly timesheet/report
- Add a dedicated email function
- Send the weekly report to a configured recipient

Sensitive information such as email addresses and credentials will not be stored directly in the source code.

## Technologies

- Python
- pytest
- Git / GitHub

## Status

Work in progress. The daily shift-entry, validation, calculation, and related testing functionality is currently implemented.
