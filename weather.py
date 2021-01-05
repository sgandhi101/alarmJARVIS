import pyowm


# TODO: Need to use a different library for weather this one sucks

def weather():
    owm = pyowm.OWM('1488aedbe2262fa7821c31932646460b')  # TODO: Replace <api_key> with your API key
    mgr = owm.weather_manager()
    obs = mgr.weather_at_coords(lat=39.166592, lon=-86.534889)
    w = obs.weather
    vol_rain = w.rain
    wind_speed = w.wind()['speed']
    status = w.detailed_status

    high = int(w.temperature('fahrenheit')['temp_max'])
    low = int(w.temperature('fahrenheit')['temp_min'])
    temp = int(w.temperature('fahrenheit')['temp'])

    if not vol_rain:
        rain = "there is expected to be rain later"
    else:
        rain = "there is no rain expected"

    final_weather = " the weather in Bloomington is " + str(temp) + " with today's status being " + str(
        status) + ". There is a high of " + str(high) + " degrees, reaching to a low of " + str(
        low) + ". Currently, there is a wind speed of about " + str(
        wind_speed) + " miles per hour and " + rain + ". "
    return final_weather


"""
**************** CLOUDY AND RAIN ****************
It appears to be overcast and cloudy today. Might I suggest you bring an umbrella, as not to tempt fate?
Weather patterns indicate, a cloudy day.
There is a high chance of precipitation today.

**************** COLD TEMPERATURE ****************
Scans indicate low temperatures today.
Scans indicate a cold front today.
May I suggest you dress warmly. It looks cold today.
Scans indicate frigid temperatures outside. May I recommend staying in with a nice, hot cocoa?

**************** HOT WEATHER ****************
Scans indicate it should be quite hot today.
It looks like it will be extremely warm. I suggest we adjust the air conditioning to high.
Temperature readings look quite high.

**************** RAINY WEATHER ****************
It appears to be raining today. An umbrella might be in order.
Large concentrations of water vapor have been forming in the region.
Expect rain today.
Scans indicate thunder and lightning today.
Today's temperatures will be cold and rainy. I daresay, a good day to stay in and catch a movie.

**************** SNOWY WEATHER ****************
Scans indicate concentrated masses of ice particles are saturating the air for several miles. That is to say, it's snowing.
Scans indicate snow today.
Weather patterns indicate snow today.
The forecast suggests snowy weather today. Layering is both an excellent and fashionable way to keep warm.

**************** CLEAR SKIES ****************
My scans indicate clear and sunny skies today. Have a wonderful day.
Today's weather readings indicate clear skies.
Scans indicate clear and sunny skies today.

**************** WINDY WEATHER ****************
Conditions are expected to be windy. Please plan accordingly.
Scans indicate high winds. 
"""
