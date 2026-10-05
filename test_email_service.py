from email_service import build_email, preview_email
import pytest

def test_build_email(monkeypatch):
    # ARRANGE
    report = "This is my week's summary of shifts"
    monkeypatch.setenv("MANAGER_EMAIL", "fake2@example.com")
# monkeypatch to fake an environment variable

    # ACT
    my_new_email = build_email(report)

    # ASSERT
    assert my_new_email["body"] == "This is my week's summary of shifts"
    assert my_new_email["subject"] == "Weekly Shifts Report"
    assert my_new_email["recipient"] == "fake2@example.com"

def test_build_email_missing_recipient(monkeypatch):
    # ARRANGE
    monkeypatch.delenv("MANAGER_EMAIL", raising=False)
    with pytest.raises(ValueError):
        build_email("Hello")

def test_preview_email(capsys):
    # ARRANGE
    fake_email_data = {
        "recipient": "mynewemail@gmail.com",
        "subject": "weekly shift recap",
        "body": "Total hours: 40 hours"
    }
    # ACT
    preview_email(fake_email_data)
    captured = capsys.readouterr()

    # ASSERT
    assert captured.out.startswith("--") 
    assert captured.out.endswith("---\n") 
    # print() automatically adds a newline at the end
    assert captured.out.strip().endswith("---")
    # added that one above for practice purposes
    assert "mynewemail@gmail.com" in captured.out
    assert "Total hours: 40 hours" in captured.out
    assert "weekly shift recap" in captured.out






