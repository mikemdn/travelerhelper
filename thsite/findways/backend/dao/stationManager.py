from .velibStation import VelibStation
from .autolibStation import AutolibStation
import requests


class StationManager:

    distance = 200

    def __init__(self):
        self.dataset_id_autolib = "stations_et_espaces_autolib_de_la_metropole_parisienne"
        self.dataset_id_velib = "stations-velib-disponibilites-en-temps-reel"

    def filter_velib(self, result):
        output_list = []
        stations_list = result["records"]
        for station in stations_list:
            latitude = station["fields"]["position"][0]
            longitude = station["fields"]["position"][1]
            capacity = station["fields"]["bike_stands"]
            availability = station["fields"]["available_bikes"]
            if station["fields"]["status"] == "OPEN":
                status = True
            else:
                status = False
            station = VelibStation(latitude, longitude, capacity, availability, status)
            output_list.append(station)
            station.object_to_string()
        return output_list

    def filter_autolib(self, result):
        output_list = []
        stations_list = result["records"]
        for station in stations_list:
            latitude = station["fields"]["xy"][0]
            longitude = station["fields"]["xy"][1]
            capacity = station["fields"]["prises_autolib"]
            station = AutolibStation(latitude, longitude, capacity)
            output_list.append(station)
        return output_list

    def find_stations_in_radius(self, latitude, longitude, is_velib, is_autolib, distance):
        # Checker is_velib != is_autolib and raise an exception if condition not verified
        if is_velib and not is_autolib:
            dataset_id = self.dataset_id_velib
        elif not is_velib and is_autolib:
            dataset_id = self.dataset_id_autolib

        url = "http://opendata.paris.fr/api/records/1.0/search/?dataset=" + dataset_id + "&geofilter.distance=" + str(latitude) + "%2C+" + str(longitude) + "%2C" + str(distance)
        result = requests.get(url).json()

        if is_velib and not is_autolib:
            return self.filter_velib(result)
        elif not is_velib and is_autolib:
            return self.filter_autolib(result)
