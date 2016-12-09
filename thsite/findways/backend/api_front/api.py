# -*- coding: utf-8 -*-

import requests
import constants
from findways.backend.business.choiceManager import ChoiceManager


def convert_meters_into_km(number):
    if number >= 1000:
        return "{} km".format(number // 1000)
    else:
        return "{} m".format(number)


class ApiRoute:
    def __init__(self, array):
        self.array = array

    def get_geolocation(self):
        """Returns the coordinates of the user's current location"""
        url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + constants.google_maps_api_key
        r = requests.post(url).json()
        self.array['departure'] = (r['location'])

    def get_route_api_front(self):
        """Returns a WayManager object with information from the interface"""
        self.get_geolocation()
        main_criteria = self.array['criteria']
        choice_manager = ChoiceManager(main_criteria, self.array)
        ways = choice_manager.get_sorted_way_list_according_to_main_criteria()
        return ways

    def data_structure(self):
        """Returns a dictionnary with all the ways and their Elem ways, with information about distance, duration and steps"""
        json = {}
        i = 1
        ways_list = []
        ways = self.get_route_api_front()
        for way in ways["routes"]:
            if "t" in way.type:
                way_type = "Transit"
            elif "d" in way.type:
                if len(way.type) == 1:
                    way_type = "Driving"
                else:
                    way_type = "Autolib (9€/30min)"
            elif "c" in way.type:
                if len(way.type) == 1:
                    way_type = "Bicycling"
                else:
                    way_type = "Velib (1,70€/day)"
            elif "u" in way.type:
                way_type = way.display_name
            else:
                way_type = "Walking"

            elemways_list = []
            for elemWay in way.elemWaysTable:
                if elemWay.type == 'c':
                    elemWay.type = "Bicycle"
                if elemWay.type == 't':
                    elemWay.type = "Transit"
                if elemWay.type == 'w':
                    elemWay.type = "Walking"
                if elemWay.type == 'd':
                    elemWay.type = "Driving"

                elemway_info = {}
                elemway_info["ElemWay_Distance"] = convert_meters_into_km(float(elemWay.distance))
                elemway_info["ElemWay_Duration"] = elemWay.duration
                elemway_info["ElemWay_Steps"] = elemWay.steps
                elemway_info["Type"] = elemWay.type
                elemways_list.append(elemway_info)
            way_dict = {}
            way_dict["Total_Duration"] = way.duration
            way_dict["Total_Distance"] = convert_meters_into_km(way.distance)
            way_dict["Price"] = way.price
            way_dict["Route_Details"] = elemways_list
            way_dict["Type"] = way_type
            way_dict["id"] = i
            ways_list.append(way_dict)
            i += 1
        json["Start_Address"] = ways["start_address"]
        json["End_Address"] = ways["end_address"]
        json["Routes"] = ways_list
        try:
            json["Places_to_visit"] = ways["places_to_visit"]
        except KeyError:
            print("Vous n'êtes pas dans le mode visite")
        return json