import os

def build_email(report):
    recipient = os.getenv("MANAGER_EMAIL")
    if not recipient:
        raise ValueError("MANAGER_EMAIL environment variable is not set")
    email_data = {
        "recipient": recipient,
        "subject": "Weekly Shifts Report",
        "body": report
    }
    return email_data

def preview_email(email_data):
    print(f"---- EMAIL PREVIEW---\n\nTo: {email_data['recipient']}\nSubject: {email_data['subject']}\n\n{email_data['body']}\n\n---------------")


def confirm_send():
    while True:
        user_answer = input("OK to send email? ")
        if user_answer.strip().lower() in ("yes", "y"):
            return True
        elif user_answer.strip().lower() in ("no", "n"):
            return False
        else:
            print("Make sure to enter 'Y' for Yes or 'N' for no. Try again")

def send_email():
    pass


# email_data = build_email('2026-10-04: 05:00-10:00 | 14:00-17:00 - 8h 0m\n\nWeekly total: 8h 0m')
# preview_email(email_data)
# print(build_email("This is the body of my weekly report"))