from newsTime import time_now
from weather import weather
from class_time import class_time
from tts import speak

time_text = time_now()
lecture = class_time()
weather = weather()

final = "Good morning. " + time_text + weather + lecture
print(final)
#speak(final)
