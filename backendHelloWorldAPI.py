import requests


def getcurrentWeather(openWeatherApiKey, lat, lon):
    '''
    :param openWeatherApiKey: Key for https://openweathermap.org API
    :param lat: horizontal lines that measure distance north or south of the equator
    :param lon: vertical lines that measure east or west of the meridian in Greenwich, England
    :return: current weather for given position(lat,lon) in a json file
    '''

    part  = ""

    jsonFileCurrentWeatherResponse = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={openWeatherApiKey}")
    print(jsonFileCurrentWeatherResponse.content)
    return jsonFileCurrentWeatherResponse


def backend():
    # lat, long = getLocationLatLong()

    # testData
    lat = 0
    lon= 0
    #data
    openWeatherApiKey = "570167a5f28aa6d8c40cb700faf0b0f5"
    getcurrentWeather(openWeatherApiKey, lat, lon)


backend()
