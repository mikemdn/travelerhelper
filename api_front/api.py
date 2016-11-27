from business.choiceManager import ChoiceManager
import constants
import requests


class ApiRoute:
    def __init__(self, array):
        self.array = array

    def get_geolocation(self):
        r = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=" + constants.google_maps_api_key).json()
        print(r)
        self.array['departure'] = (r['location'])
        print(self.array)

    def get_route_api_front(self):
        """Returns a WayManager object with information from the interface"""
        self.get_geolocation()

        ## Attention, coder ceci de manière dynamique
        main_criteria = 1
        choice_manager = ChoiceManager(main_criteria, self.array)
        ways = choice_manager.get_sorted_way_list_according_to_main_criteria()
        return ways

    def data_structure(self):
        """Returns a dictionnary with all the ways and their Elem ways, with information about distance, duration and steps"""
        way_dict = {}
        ways = self.get_route_api_front()
        print(ways)
        for way in ways:
            if "t" in way.type:
                way_type = "Transit"
            elif "d" in way.type:
                if len(way.type) == 1:
                    way_type = "Driving"
                else:
                    way_type = "Autolib"
            elif "c" in way.type:
                if len(way.type) == 1:
                    way_type = "Bicycling"
                else:
                    way_type = "Velib"
            else:
                way_type = "Walking"

            elemway_tuple = []
            for elemWay in way.elemWaysTable:
                elemway_tuple.append([elemWay.type, (elemWay.distance, elemWay.duration, elemWay.price, elemWay.steps)])
            way_dict[way_type] = elemway_tuple
        return way_dict

"""
    def get_geolocation(self):
        "https://www.googleapis.com/geolocation/v1/geolocate?key={}".format(constants.google_maps_api_key)
"""

if __name__ == "__main__":
    apiroute = ApiRoute({})
    apiroute.get_geolocation()
