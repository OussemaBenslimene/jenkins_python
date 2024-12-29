import calendar
from datetime import datetime

def show_calendar():
    now = datetime.now()
    year = now.year
    month = now.month
    print(calendar.month(year, month))

if __name__ == "__main__":
    show_calendar()
