from dao import weatherManager
from .wayManager import WayManager


class ChoiceManager:

    def __init__(self, main_criteria, requests, time=0):
        self.main_criteria = main_criteria
        self.requests = requests
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
            #self.available_transports.append("road")
            self.available_transports.append("autolib")
            self.available_transports.append("velib")
            self.available_transports.append("walk")
            self.available_transports.append("uber")
        if self.main_criteria == 2:
            self.available_transports.append("rail")
            #self.available_transports.append("road")
            self.available_transports.append("velib")
            self.available_transports.append("walk")
        """Load"""
        if self.main_criteria == 3:
            #self.available_transports.append("road")
            self.available_transports.append("autolib")
            self.available_transports.append("walk")
            self.available_transports.append("uber")
            self.walking_limitation = True
        """Tourisme"""
        if self.main_criteria == 4:
            #self.available_transports.append("road")
            self.available_transports.append("velib")
            self.available_transports.append("walk")

        """Conditions to define a rather bad weather which tends to limit cycling and walking"""
        condition_bad_weather = self.weather.get_type() == "Rain" or self.weather.get_type() == "Snow" or \
            self.weather.get_temperature() < 5 or self.weather.get_rain() > 1 or self.weather.get_wind() > 14
        if condition_bad_weather:
            self.walking_limitation = True
            try:
                self.available_transports.remove("velib")
            except:
                print("La possibilité d'utiliser un velib a déjà été supprimée.")

    def get_available_transport_list(self):
        print(self.available_transports)
        return self.available_transports

    def get_sorted_way_list_according_to_main_criteria(self):
        if self.main_criteria == 1:
            sorted_ways = self.get_fastest_way(self.requests)
        elif self.main_criteria == 2:
            sorted_ways = self.get_cheapest_way(self.requests)
        elif self.main_criteria == 3:
            sorted_ways = self.get_lightest_way(self.requests)
        elif self.main_criteria == 4:
            sorted_ways = self.get_touristic_way(self.requests)
        else:
            print("Une erreur s'est produite dans le choix du critère principal")
            sorted_ways = []
        return sorted_ways

    def get_fastest_way(self, requests):
        """Return a Way object for main_criteria #1 on speed"""
        way_manager = WayManager(requests, self.available_transports).get_ways()
        ways = way_manager["routes"]
        sorted_ways = sorted(ways, key=lambda way: way.duration)
        way_manager["routes"] = sorted_ways
        return way_manager

    def get_cheapest_way(self, requests):
        """Return a Way object for main_criteria #2 on price"""
        way_manager = WayManager(requests, self.available_transports).get_ways()
        ways = way_manager["routes"]
        sorted_ways = sorted(ways, key=lambda way: way.price)
        way_manager["routes"] = sorted_ways
        return way_manager

    def get_lightest_way(self, requests):
        """Return a Way object for main_criteria #3 on load"""
        WayManager(requests, self.available_transports).get_ways()

    def get_touristic_way(self, requests):
        """Return a Way object for main_criteria #4 on load"""
        WayManager(requests, self.available_transports).get_ways()
