from bs4 import BeautifulSoup as soup
from urllib2 import urlopen
import time
from datetime import date

def timeNow():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)

    today = date.today()
    todaysDate = today.strftime("%B %d, %Y")
    finalText = "The time is  " + current_time + " AM, and it is " + todaysDate
    return finalText


