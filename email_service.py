import os
import subprocess
import smtplib
from email.message import EmailMessage

# export MANAGER_EMAIL="fake@email.com" 
# echo $MANAGER_EMAIL

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
    print(f"\n---- EMAIL PREVIEW---\n\nTo: {email_data['recipient']}\nSubject: {email_data['subject']}\n\n{email_data['body']}\n\n---------------")


def copy_to_clipboard(text):
    subprocess.run(['pbcopy'], input=text, text=True, check=True)

# copy_to_clipboard("Hello")


def send_email(email_data):
    sender = os.getenv("GMAIL_ADDRESS")
    password = os.getenv("GMAIL_APP_PASSWORD") # retrieves your Gmail credentials from environment variables.

    if not sender or not password:
        raise ValueError("Gmail credentials are not configured")

    message = EmailMessage() # constructs the email, including its headers and body.
    message["From"] = sender
    message["To"] = email_data["recipient"]
    message["Subject"] = email_data["subject"]
    message.set_content(email_data["body"])

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server: # establishes an encrypted connection to Gmail.
        server.login(sender, password) # authenticates using your Gmail address and App Password.
        server.send_message(message) # sends the email.


def choose_email_action():
    while True:
        user_answer = input("What would you like to do?\n1. Send email\n2. Copy email body\n3. Cancel\n").strip()
        if user_answer == "1":
            return "send"
        elif user_answer == "2":
            return "copy"
        elif user_answer == "3":
            return "cancel"
        else:
            print("Please make sure to pick 1, 2, or 3")

# print(choose_email_action())        

# send, copy body or cancel



def confirm_send():
    while True:
        answer = input("Are you sure you want to send this email? (y/n): ").strip().lower()

        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("Please enter y or n.")


# email_data = build_email('2026-10-04: 05:00-10:00 | 14:00-17:00 - 8h 0m\n\nWeekly total: 8h 0m')
# preview_email(email_data)
# print(build_email("This is the body of my weekly report"))