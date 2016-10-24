################ Partie API ####################
from business.WayManager import WayManager
import constants

class ApiRoute:
    def __init__(self, array):
        self.array = array

    def get_route_api_front(self):
        """returns a WayManager object with information from the interface"""
        return WayManager(self.array)

    def data_structure(self):
        """Returns a dictionnary with all the ways and their Elem ways, with information about distance, duration and steps"""
        way_dict = {}
        ways = self.get_route_api_front().ways
        for way in ways:
            if "t" in way.type:
                way_type = "Transit"
            elif "d" in way.type:
                way_type = "Autolib"
            elif "c" in way.type:
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