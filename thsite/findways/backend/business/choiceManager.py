# -*- coding: utf-8 -*-

import math
import constants
from .wayManager import WayManager
from findways.backend.dao import position
from findways.backend.dao import weatherManager
from findways.models import Place


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

    def select_transport(self):
        """Set the list of available transports and the walking level accepted """

        """Price"""
        if self.main_criteria == 1:
            self.available_transports.append("rail")
            self.available_transports.append("autolib")
            self.available_transports.append("velib")
            self.available_transports.append("walk")
            self.available_transports.append("uber")
        if self.main_criteria == 2:
            self.available_transports.append("rail")
            self.available_transports.append("velib")
            self.available_transports.append("walk")
        """Load"""
        if self.main_criteria == 3:
            self.available_transports.append("autolib")
            self.available_transports.append("walk")
            self.available_transports.append("uber")
        """Tourisme"""
        if self.main_criteria == 4:
            self.available_transports.append("velib")
            self.available_transports.append("walk")

        """Conditions to define a rather bad weather which tends to limit cycling and walking"""
        condition_bad_weather = self.weather.get_type() == "Rain" or self.weather.get_type() == "Snow" or \
            self.weather.get_temperature() < 5 or self.weather.get_rain() > 1 or self.weather.get_wind() > 14
        if condition_bad_weather:
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
        way_manager = WayManager(requests, self.available_transports).get_ways()
        ways = way_manager["routes"]
        sorted_ways = sorted(ways, key=lambda way: way.duration)
        way_manager["routes"] = sorted_ways
        return way_manager

    def get_touristic_way(self, requests):
        """Return a Way object for main_criteria #4 on load"""
        ways = WayManager(requests, self.available_transports).get_ways()
        ways['places_to_visit'] = self.get_places_to_visit(requests)
        return ways

    def get_places_to_visit(self, requests):
        """Find in the database all the places that are in the rectangle defined by the departure and arrival positions"""
        arrival = position.Position(0, 0, requests["destination"])
        min_lat = min(requests["departure"]["lat"], arrival.get_latitude())
        max_lat = max(requests["departure"]["lat"], arrival.get_latitude())
        min_long = min(requests["departure"]["lng"], arrival.get_longitude())
        max_long = max(requests["departure"]["lng"], arrival.get_longitude())
        q1 = Place.objects.filter(long__gte=min_long)
        q2 = q1.filter(long__lte=max_long)
        q3 = q2.filter(lat__gte=min_lat)
        places_to_visit = q3.filter(lat__lte=max_lat)
        if len(places_to_visit) >= 3:
            return self.get_closest_places_to_visit(places_to_visit, arrival, requests)
        return places_to_visit

    def get_closest_places_to_visit(self, places_to_visit, arrival, requests):
        """Method to get the three places that are the closest to the line linking departure and arrival"""
        places_to_visit_filtered = {}
        steps_list = []
        for place in places_to_visit:
            dist = abs(self.get_distance_to_direct_line(arrival, requests, place))
            places_to_visit_filtered[place] = dist
        sorted_places_to_visit_filtered = sorted(places_to_visit_filtered.items(), key=lambda t: t[1])
        for i in range(0, constants.steps_number):
            try:
                steps_list.append(sorted_places_to_visit_filtered[i][0])
            except IndexError:
                print("Il n'y a pas plus d'éléments dans la liste")
        return steps_list

    def get_distance_to_direct_line(self, arrival, requests, place):
        """Method to calculate the distance between a place and the line linking departure and arrival"""
        delta_lat = arrival.get_latitude() - requests["departure"]["lat"]
        delta_long = arrival.get_longitude() - requests["departure"]["lng"]
        a = float(delta_lat / delta_long)
        b = -1
        c = arrival.get_longitude()
        return (a * place.long + b * place.lat + float(c)) / math.sqrt(pow(a, 2) + pow(b, 2))
