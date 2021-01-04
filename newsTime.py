import time
from datetime import date


def time_now():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)

    today = date.today()
    todaysDate = today.strftime("%B %d, %Y")
    finalText = "The time is  " + current_time + " AM, and it is " + todaysDate
    return finalText
