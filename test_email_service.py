from email_service import build_email, preview_email, choose_email_action, copy_to_clipboard
import pytest

# monkeypatch → temporarily replace something external to the function.
# capsys → capture what was printed.
# pytest.raises() → verify an exception is raised.

# control the environment the function reads / Control the external state that the function depends on.
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
    assert captured.out.startswith("\n") 
    assert captured.out.endswith("---\n") 
    # print() automatically adds a newline at the end
    assert captured.out.strip().endswith("---")
    # added that one above for practice purposes
    assert "mynewemail@gmail.com" in captured.out
    assert "Total hours: 40 hours" in captured.out
    assert "weekly shift recap" in captured.out

# input() — control what a dependency returns
def test_choose_email_send(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _:"1")
    response = choose_email_action()
    assert response == "send"

def test_choose_email_copy(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _:"2")
    response = choose_email_action()
    assert response == "copy"

def test_choose_email_cancel(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _:"3")
    result = choose_email_action()
    assert result == "cancel"

def test_choose_email_iteration(monkeypatch, capsys):
    responses = iter(["copy", "3"])
    monkeypatch.setattr("builtins.input", lambda prompt:next(responses))
    result = choose_email_action()
    captured = capsys.readouterr()
    assert "pick 1, 2, or 3" in captured.out
    assert result == "cancel"

# intercepting an external function call and inspecting its arguments. control/observe what the function calls / Control how external dependency is called
def test_copy_clipboard(monkeypatch):
# ARRANGE
    calls = {}
    
    def fake_run(command, input, text, check):
        calls["command"] = command
        calls["input"] = input
        calls["text"] = text
        calls["check"] = check

    monkeypatch.setattr("email_service.subprocess.run", fake_run)

# ACT
    copy_to_clipboard("This is my text for today")

# ASSERT
    assert calls["command"] == ["pbcopy"]
    assert calls["input"] == "This is my text for today"
    assert calls["text"] is True
    assert calls["check"] is True

# Previous code where the function was binary (send or not send)
'''
def test_confirm_send_positive(monkeypatch):
    # ARRANGE
    monkeypatch.setattr("builtins.input", lambda _:"Yes")
    # ACT
    response = confirm_send()

    # ASSERT
    assert response is True

def test_confirm_send_negative(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    response = confirm_send()
    assert response is False


def test_confirm_iteration(monkeypatch, capsys):
    responses = iter(["hello", "yes"])
    monkeypatch.setattr("builtins.input", lambda prompt:next(responses))
    response = confirm_send()
    captured = capsys.readouterr()
    assert "Try again" in captured.out
    assert response is True
'''