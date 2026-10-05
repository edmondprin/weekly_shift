# orchestrate everything
from datetime import date
from shifts import gather_user_shift
from storage import load_shifts, save_shift
from report import get_current_week_shifts, build_weekly_report
from email_service import build_email, preview_email, confirm_send

def main():
    my_date = date.today()
    new_shift = gather_user_shift()
    save_shift(new_shift)
    my_shifts = load_shifts()
    current_week_shifts = get_current_week_shifts(my_shifts, my_date)
    report = build_weekly_report(current_week_shifts)
    email_data = build_email(report)
    preview_email(email_data)
    answer = confirm_send()
    if answer: 
        print("Email ready to send!")
    else:
        print("Email not sent!")

if __name__ == "__main__":
    main()