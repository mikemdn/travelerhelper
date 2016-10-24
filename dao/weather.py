class Weather:

    def __init__(self, type, temperature, humidity, rain, clouds):
        self.type = type
        self.temperature = temperature
        self.humidity = humidity
        self.rain = rain
        self.clouds = clouds

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

    def weather_to_string(self):
        print("Type: " + str(self.type) + "\nHumidity: " + str(self.humidity) + "\nTemperature: " + str(self.temperature)
              + "\nRain: " + str(self.rain) + "\nClouds: " + str(self.clouds))
