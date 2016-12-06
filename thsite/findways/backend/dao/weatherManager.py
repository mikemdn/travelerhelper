import requests
import constants
import math
from .weather import Weather


class WeatherManager:

    def __init__(self):
        self.weather = "weather"
        self.forecast = "forecast"

    def get_weather(self, type, time=0):
        url = "http://api.openweathermap.org/data/2.5/" + type + "?q=" + constants.city + "&appid=" + str(constants.open_weather_map_api_key)
        if type == self.weather:
            response = requests.get(url).json()
            try:
                rain = response["rain"]["3h"]
            except:
                rain = 0
        elif type == self.forecast:
            if time != 0:
                raw_response = requests.get(url).json()["list"]
                first_dt = raw_response[0]["dt"]
                index = WeatherManager.find_correct_forecast_index(self, first_dt, time)
                response = raw_response[index]
            else:
                # lever une exception
                print("Vous n'avez pas indiqué de date de départ")
            rain = -1
        else:
            # lever une exception
            print("Une erreur s'est produite")

        type = response["weather"][0]["main"]
        temperature = response["main"]["temp"] - 272.15
        humidity = response["main"]["humidity"]
        clouds = response["clouds"]["all"]
        wind = response["wind"]["speed"]

        weather = Weather(type, temperature, humidity, rain, clouds, wind)
        return weather

    def find_correct_forecast_index(self, first_date_time_in_the_list, wanted_date_time):
        return math.floor((wanted_date_time - first_date_time_in_the_list)/(3 * 3600))
