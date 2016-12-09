# -*- coding: utf-8 -*-

from .elemFunctions import *


class WayManager:

    def __init__(self, request, available_transport_types):
        # Ajouter en paramètre de la fonction ses coordonnées gps
        self.departure_position = position.Position(float(request['departure']['lat']), float(request['departure']['lng']), "")
        self.arrival_position = position.Position(0, 0, request["destination"])
        self.ways = self.get_relevant_ways(available_transport_types)

    def get_relevant_ways(self, available_transport_types):
        #way is a list of Ways().
        way_manager = {}
        ways = []
        for transport_type in available_transport_types:
            if transport_type == "rail":
                ways.append(WayManager.get_transit_way(self)) #ajouter le paramètre ferré
            elif transport_type == "road":
                ways.append(WayManager.get_transit_way(self)) #ajouter le paramètre non ferré
            elif transport_type == "autolib":
                ways.append(WayManager.get_autolib_way(self))
            elif transport_type == "velib":
                ways.append(WayManager.get_cycling_way(self))
            elif transport_type == "walk":
                ways.append(WayManager.get_walking_way(self))
            elif transport_type == "uber":
                for uber_type in WayManager.get_uber_way(self):
                    ways.append(uber_type)
            else:
                print("Le type de transport ne fait pas partie des possibilités.")
        way_manager["start_address"] = self.arrival_position.address
        way_manager["end_address"] = self.arrival_position.address
        way_manager["start_address_coords"] = {'lat' : self.departure_position.get_latitude(),'lng' : self.departure_position.get_longitude()}
        way_manager["end_address_coords"] = {'lat' : self.arrival_position.get_latitude(),'lng' : self.arrival_position.get_longitude()}
        way_manager["routes"] = ways
        return way_manager

    def get_ways(self):
        return self.ways

    # The following functions return a Way object that contains all the corresponding elementary ways
    def get_walking_way(self):
        wway = Way()
        wway = wway + get_walking_elem(self.departure_position, self.arrival_position)
        return wway

    def get_cycling_way(self):
        cway = Way()
        cway = cway + get_cycling_elem(self.departure_position, self.arrival_position)
        return cway

    def get_transit_way(self):
        tway = get_transit_elem(self.departure_position, self.arrival_position)
        return tway

    def get_velib_way(self):
        departure_station = get_station(self.departure_position.get_latitude(), self.departure_position.get_longitude(), "b")
        departure_station_position = station_converter_into_position(departure_station)
        arrival_station = get_station(self.arrival_position.get_latitude(), self.arrival_position.get_longitude(), "b")
        arrival_station_position = station_converter_into_position(arrival_station)
        cway = Way()
        cway = cway + get_walking_elem(self.departure_position, departure_station_position)
        cway = cway + get_cycling_elem(departure_station_position, arrival_station_position)
        cway = cway + get_walking_elem(arrival_station_position, self.arrival_position)
        return cway

    def get_autolib_way(self):
        departure_station = get_station(self.departure_position.get_latitude(), self.departure_position.get_longitude(), "c")
        departure_station_position = station_converter_into_position(departure_station)
        arrival_station = get_station(self.arrival_position.get_latitude(), self.arrival_position.get_longitude(), "c")
        arrival_station_position = station_converter_into_position(arrival_station)
        dway = Way()
        dway = dway + get_walking_elem(self.departure_position, departure_station_position)
        dway = dway + get_driving_elem(departure_station_position, arrival_station_position)
        dway = dway + get_walking_elem(arrival_station_position, self.arrival_position)
        return dway

    def get_driving_way(self):
        dway = Way()
        dway = dway + get_driving_elem(self.departure_position, self.arrival_position)
        return dway

    def get_uber_way(self):
        dway = self.get_driving_way()
        uway_list = get_uber_elem(self.departure_position, self.arrival_position, dway)
        return uway_list
