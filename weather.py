import pyowm
owm = pyowm.OWM('1488aedbe2262fa7821c31932646460b') # TODO: Replace <api_key> with your API key

def getAllWeather():
    obs = owm.weather_at_place('Buffalo Grove,US')
    w = obs.get_weather()
    volumeRain = w.get_rain()
    windSpeed = w.get_wind()['speed']
    status = w.get_detailed_status()

    tempHigh = w.get_temperature('fahrenheit')['temp_max']
    tempLow = w.get_temperature('fahrenheit')['temp_min']
    temp = w.get_temperature('fahrenheit')['temp']
    tempHigh = int(tempHigh)
    tempLow = int(tempLow)
    temp = int(temp)

    print volumeRain
    if (volumeRain > 0):
        isRain = "there is also expected to be rain today"
    else:
        isRain = "there is also no rain expected today"

    print windSpeed
    print tempLow
    print tempHigh
    print temp
    print status

    finalWeather = "As for the weather, today's status is " + str(status) + ". The current temperature is " + str(temp) + " degrees, with a high of " + str(tempHigh) + " and a low of " + str(tempLow) + ". Currently, there is a windspeed of about " + str(windSpeed) + " miles per hour and " + isRain + ". "
    return finalWeather

print getAllWeather()