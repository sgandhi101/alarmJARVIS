from tts import Polly
from newsTime import timeNow
from weather import getAllWeather
from get_news import getNews
import os
import time


tts = Polly('Brian')

# Get all relevant information
news = getNews()
time_text = timeNow()
weather = getAllWeather()
endingQuip = "That is all for now. Get out of bed now or Kelly won't like you. Have a great day sir."
surfingJoke = " . The surf conditions are fair, with waist to shoulder high lines. High tide will be at 10:52 am. "

# Join it all together and save it eZ money
final = "Good morning. " + time_text + surfingJoke + news + weather
final = final + endingQuip
print final
tts.saveToFile(final, 'final.mp3')

# Play with terminal AND vlc FINESSE should've never paid three bucks for LingOn
os.system('open music.mp3')
time.sleep(2)
os.system('mpg123 final.mp3')