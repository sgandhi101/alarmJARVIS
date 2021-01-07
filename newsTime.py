import time
from datetime import datetime


def order(n):
    return str(n) + ("th" if 4 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))


def time_now():
    t = time.localtime()
    now = datetime.now()
    current_time = time.strftime("%H:%M", t)
    month = now.strftime('%B')
    day = now.day
    final = "It's " + current_time + " AM, " + month + " the " + order(day)
    return final
