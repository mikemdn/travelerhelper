from .Way import Way
from .ElemFunctions import *
from dao import position


class WayManager:
    def __init__(self, request):
        self.meteo = 10
        self.rich = request["rich"]
        self.car = request["car"]
        self.bike = request["bike"]
        self.walk = request["walk"]
        self.charged = request["charged"]
        self.credit_card = request["credit card"]
        self.driving_license= request["driving licence"]
        # Ajouter en paramètre de la fonction ses coordonnées gps
        self.departure_position = position.Position(float(request['departure']['lat']), float(request['departure']['lng']), "")
        self.arrival_position = position.Position(0, 0, request["destination"])
        self.ways = self.get_relevant_ways()

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
        if self.walk and not self.charged:
            ways.append(self.get_walking_way())
        if self.driving_license and self.credit_card:
            ways.append(self.get_autolib_way())
            ways.append(self.get_driving_way())
        if not self.charged and self.bike:
            ways.append(self.get_velib_way())
            ways.append(self.get_cycling_way())
        for way in ways:
            print(str(way.distance) + " " + str(way.type)+ " " + str(way.price))
        return ways

    #### METHODES GLOBALES

    def get_walking_way(self):
        wway = Way()
        wway = wway + get_walking_elem(self.departure_position, self.arrival_position)
        return(wway)


    def get_cycling_way(self):
        cway = Way()
        cway = cway + get_cycling_elem(self.departure_position, self.arrival_position)
        return(cway)

    def get_transit_way(self):
        tway = get_transit_elem(self.departure_position, self.arrival_position)
        return (tway)

    def get_velib_way(self):
        departure_station = get_station(self.departure_position.get_latitude(), self.departure_position.get_longitude(), "b")
        departure_station_position = station_converter_into_position(departure_station)
        print('velib_depart : {}, {}'.format(departure_station_position.get_latitude(), departure_station_position.get_longitude()))
        arrival_station = get_station(self.arrival_position.get_latitude(), self.arrival_position.get_longitude(), "b")
        arrival_station_position = station_converter_into_position(arrival_station)
        print('velib_arrivee : {}, {}'.format(arrival_station_position.get_latitude(), arrival_station_position.get_longitude()))
        cway = Way()
        cway = cway + get_walking_elem(self.departure_position, departure_station_position)
        cway = cway + get_cycling_elem(departure_station_position, arrival_station_position)
        cway = cway + get_walking_elem(arrival_station_position, self.arrival_position)
        return(cway)


    def get_autolib_way(self):
        print(self.departure_position.get_latitude(), self.departure_position.get_longitude())
        departure_station = get_station(self.departure_position.get_latitude(), self.departure_position.get_longitude(), "c")
        departure_station_position = station_converter_into_position(departure_station)
        print('autolib_depart : {}, {}'.format(departure_station_position.get_latitude(), departure_station_position.get_longitude()))
        arrival_station = get_station(self.arrival_position.get_latitude(), self.arrival_position.get_longitude(), "c")
        arrival_station_position = station_converter_into_position(arrival_station)
        print('autolib_arrivee : {}, {}'.format(arrival_station_position.get_latitude(), arrival_station_position.get_longitude()))
        dway = Way()
        dway = dway + get_walking_elem(self.departure_position, departure_station_position)
        dway = dway + get_driving_elem(departure_station_position, arrival_station_position)
        dway = dway + get_walking_elem(arrival_station_position, self.arrival_position)
        return(dway)


    def get_driving_way(self):
        dway = Way()
        dway = dway + get_driving_elem(self.departure_position, self.arrival_position)
        return(dway)

    def get_uber_way(self):
        uway = Way()
        uway = uway + get_uber_elem(self.departure_position, self.arrival_position)
        return uway
