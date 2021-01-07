import weathercom
from json import loads

def weather():
    detailed = weathercom.getCityWeatherDetails("bloomington, indiana", queryType="hourly-data")
    w = loads(detailed)
    feels = round((w["vt1hourlyForecast"]["feelsLike"][0] * float(9/5)) + 32)
    rain = max(w["vt1hourlyForecast"]["precipPct"])
    status = (w["vt1hourlyForecast"]["phrase"][0]).lower()
    if rain > 5:
        rain = ". There is a high chance of precipitation today, at " + str(rain) + " percent. "
    else:
        rain = ". There is no rain expected today. "

    final_weather = ". The weather in Bloomington is " + str(feels) + " degrees with today's status being, " + str(
        status) + rain
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
