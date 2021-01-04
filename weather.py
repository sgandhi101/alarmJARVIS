import pyowm


def weather():
    owm = pyowm.OWM('1488aedbe2262fa7821c31932646460b')  # TODO: Replace <api_key> with your API key
    mgr = owm.weather_manager()
    obs = mgr.weather_at_place('Buffalo Grove,US')
    w = obs.weather
    vol_rain = w.rain
    wind_speed = w.wind()['speed']
    status = w.detailed_status

    high = int(w.temperature('fahrenheit')['temp_max'])
    low = int(w.temperature('fahrenheit')['temp_min'])
    temp = int(w.temperature('fahrenheit')['temp'])

    if not vol_rain:
        rain = "there is also expected to be rain today"
    else:
        rain = "there is also no rain expected today"

    final_weather = "As for the weather, today's status is " + str(status) + ". The current temperature is " + str(
        temp) + " degrees, with a high of " + str(high) + " and a low of " + str(
        low) + ". Currently, there is a wind speed of about " + str(
        wind_speed) + " miles per hour and " + rain + ". "
    return final_weather
