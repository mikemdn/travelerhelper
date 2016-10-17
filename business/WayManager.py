from .Way import Way
from .ElemFunctions import *
from dao import position


class WayManager:
    def __init__(self, request):
        self.meteo = 10
        self.rich = True #request["rich"]
        self.bike = True #request["bike"]
        self.walk = True #request["walk"]
        self.charged = True #request["charged"]
        self.credit_card = True #request["credit card"]
        self.driving_license= True #request["driving licence"]
        # Ajouter en paramètre de la fonction ses coordonnées gps
        self.departure_position = position.Position(48.862725, 2.287592, "")
        self.arrival_position = position.Position(0, 0, request["destination"])

    def get_relevant_ways(self):
        #way is a list of Ways().
        ways = []
        """if self.charged:
            ways += WayManager.get_autolib_way(self, self.departure_position, self.arrival_position)
            ways += WayManager.get_driving_way()
        elif self.meteo > 5 :
            ways += WayManager.get_walking_way()
            ways += WayManager.get_cycling_way()
            ways += WayManager.get_transit_way()
        else:
            ways += WayManager.get_transit_way()"""
        ways.append(WayManager.get_autolib_way(self, self.departure_position, self.arrival_position))

        return ways

    #### METHODES GLOBALES

    """def get_walking_way(self):
        wway_elem=WayManager.get_walking_elem(geo_departure,geo_arrival)
        wway=Way()
        wway=Way+wway_elem
        return(wway)

    def get_cycling_way(self):
        departure_station,arrival_station=get_stations(departure,arrival)
        cway=Way()
        cway=cway+WayManager.get_walking_elem(self.geo_arrival,departure_station)
        cway=cway+WayManager.get_cycling_elem(departure_station,arrival_station)
        cway=cway+WayManager.get_walking_elem(arrival_station,self.arrival)
        return(cway)

    def get_driving_way(self):
        dway_elem=WayManager.get_driving_elem(geo_departure,geo_arrival)
        dway=Way()
        dway=Way+dway_elem
        return(dway)

    def get_transit_way(self):
        tway = Way()
        return(tway)"""

    def get_autolib_way(self, departure_position, arrival_position):
        departure_station = get_station(departure_position.get_latitude(), departure_position.get_longitude(), "c")
        departure_station_position = station_converter_into_position(departure_station)

        arrival_station = get_station(arrival_position.get_latitude(), arrival_position.get_longitude(), "c")
        arrival_station_position = station_converter_into_position(arrival_station)
        dway = Way()
        """dway = dway + get_walking_elem(departure_position, departure_station_position)
        dway = dway + get_driving_elem(departure_station_position, arrival_station_position)
        dway = dway + get_driving_elem(arrival_station_position, arrival_position)"""
        return(dway)

