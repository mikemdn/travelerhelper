class Weather:

    def __init__(self, type, temperature, humidity, rain, clouds, wind):
        self.type = type
        self.temperature = temperature
        self.humidity = humidity
        self.rain = rain
        self.clouds = clouds
        self.wind = wind

    def get_type(self):
        return self.type

    def get_humidity(self):
        return self.humidity

    def get_temperature(self):
        return self.temperature

    def get_rain(self):
        return self.rain

    def get_clouds(self):
        return self.clouds

    def get_wind(self):
        return self.wind

    def weather_to_string(self):
        print("Type: " + str(self.type) + "\nHumidity: " + str(self.humidity) + "\nTemperature: " + str(self.temperature)
              + "\nRain: " + str(self.rain) + "\nClouds: " + str(self.clouds) + "\nWind: " + str(self.wind))
