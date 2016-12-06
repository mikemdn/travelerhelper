import requests
import constants
from findways.backend.business.choiceManager import ChoiceManager


class ApiRoute:
    def __init__(self, array):
        self.array = array

    def get_geolocation(self):
        """Returns the coordinates of the user's current location"""
        url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + constants.google_maps_api_key
        r = requests.post(url).json()
        self.array['departure'] = (r['location'])
        print("geolocation : {}".format(r))

    def get_route_api_front(self):
        """Returns a WayManager object with information from the interface"""
        self.get_geolocation()
        # Attention, coder ceci de manière dynamique
        main_criteria = 4
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
            elif "u" in way.type:
                way_type = way.display_name
            else:
                way_type = "Walking"

            elemway_tuple = []
            for elemWay in way.elemWaysTable:
                elemway_tuple.append([elemWay.type, (elemWay.distance, elemWay.duration, elemWay.steps)])
            way_dict[way_type] = (way.duration, way.distance, way.price, elemway_tuple)
        return way_dict

if __name__ == "__main__":
    apiroute = ApiRoute({})
    apiroute.get_geolocation()
