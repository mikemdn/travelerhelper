from dao import weatherManager
from .WayManager import WayManager


class ChoiceManager:

    def __init__(self, main_criteria, time=0):
        self.main_criteria = main_criteria
        """Get weather"""
        if time == 0:
            type = "weather"
        else:
            type = "forecast"
        self.weather = weatherManager.WeatherManager().get_weather(type, time)
        """Set the list of available transports"""
        self.available_transports = []
        self.select_transport()
        self.walking_limitation = False

    def select_transport(self):
        """Set the list of available transports and the walking level accepted """

        """Price"""
        if self.main_criteria == 1:
            self.available_transports.append("rail")
            self.available_transports.append("road")
            self.available_transports.append("autolib")
            self.available_transports.append("velib")
            self.available_transports.append("walk")
            self.available_transports.append("uber")
        if self.main_criteria == 2:
            self.available_transports.append("rail")
            self.available_transports.append("road")
            self.available_transports.append("velib")
            self.available_transports.append("walk")
        """Load"""
        if self.main_criteria == 3:
            self.available_transports.append("road")
            self.available_transports.append("autolib")
            self.available_transports.append("walk")
            self.available_transports.append("uber")
            self.walking_limitation = True
        """Tourisme"""
        if self.main_criteria == 4:
            self.available_transports.append("road")
            self.available_transports.append("velib")
            self.available_transports.append("walk")

        """Conditions to define a rather bad weather which tends to limit cycling and walking"""
        condition_bad_weather = self.weather.get_type() == "Rain" or self.weather.get_type() == "Snow" or \
                    self.weather.get_temperature() < 10 or self.weather.get_humidity() > 75 or \
                    self.weather.get_rain() > 1 or self.weather.get_wind() > 14
        if condition_bad_weather:
            self.walking_limitation = True
            try:
                self.available_transports.remove("velib")
            except:
                print("La possibilité d'utiliser un velib a déjà été supprimée.")

    def get_fastest_way(self):
        """Return a Way object for main_criteria #1 on speed"""
        WayManager("5 avenue des Champs Elysees 75008 PARIS", self.available_transports).get_ways()

    def get_cheapest_way(self):
        """Return a Way object for main_criteria #2 on price"""
        WayManager("5 avenue des Champs Elysees 75008 PARIS", self.available_transports).get_ways()

    def get_lightest_way(self):
        """Return a Way object for main_criteria #3 on load"""
        WayManager("5 avenue des Champs Elysees 75008 PARIS", self.available_transports).get_ways()

    def get_touristic_way(self):
        """Return a Way object for main_criteria #4 on load"""
        WayManager("5 avenue des Champs Elysees 75008 PARIS", self.available_transports).get_ways()
