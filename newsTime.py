import time


def time_now():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    final = "It's  " + current_time + " AM,"
    return final
