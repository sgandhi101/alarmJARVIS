from newsTime import time_now
from weather import weather
from get_news import get_news
from tts import speak

news = get_news()
time_text = time_now()
weather = weather()
ending = "Have a great day sir."

final = "Good morning. " + time_text + news + weather + ending
print(final)
speak(final)
