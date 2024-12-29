from app.main import show_calendar
import calendar

def test_show_calendar():
    # Ensure calendar.month produces output for current year and month
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    expected_calendar = calendar.month(year, month)
    
    # Mocking print output
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    show_calendar()
    sys.stdout = sys.__stdout__
    
    assert captured_output.getvalue().strip() == expected_calendar.strip()
