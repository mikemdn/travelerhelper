################ Partie API ####################
import WayManager

class ApiRoute:
    def __init__(self, **array):
        self.array = array

    def get_route_api_front(self):
        return get_relevant_ways(self.array)

    def data_structure(self):
        way_dict = {}
        ways = get_route_api_front(self.array)
        for way in ways:
            if "t" in way.type:
                way_type = "Transit"
            if "a" in way.type:
                way_type = "Autolib"
            if "c" in way.type:
                way_type = "Velib"
            else:
                way_type = "Walking"

            elemway_dict = {}
            for elemWay in way.Elemways():
                elemway_dict[elemWay.type] = (elemWay.distance, elemWay.duration, elemWay.price, elemWay.steps)
            way_dict[way_type] = elemway_dict
        return way_dict

