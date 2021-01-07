from datetime import timedelta
from datetime import datetime

# Python starts the week with Monday, not Sunday
classes = {
    "0": timedelta(hours=8, minutes=45, seconds=0),
    "1": timedelta(hours=9, minutes=25, seconds=0),
    "2": timedelta(hours=8, minutes=45, seconds=0),
    "3": timedelta(hours=9, minutes=25, seconds=0),
    "4": timedelta(hours=8, minutes=45, seconds=0)
}


def class_time():
    start = datetime.now().time()
    now = timedelta(hours=start.hour, minutes=start.minute, seconds=start.second)
    day = str(datetime.today().weekday())
    if day != 5 and day != 6:
        next_class = classes[day]
        delta = next_class - now
        delta = delta.seconds
        hours = delta // 3600
        if hours > 1:
            lexicon = " hours"
        else:
            lexicon = " hour"
        if delta > 3600:
            ending = "Your first class begins in " + str(hours) + lexicon + " and " + str(
                round(delta // 60) % 60) + " minutes"
        else:
            ending = "Your first class begins in " + str(round(delta // 60) % 60) + " minutes"
    else:
        ending = "You have no classes scheduled today."

    return ending
