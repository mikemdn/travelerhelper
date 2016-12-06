from findways.backend.business.elemWay import ElemWay
from findways.backend.dao import position
from findways.backend.dao import stationManager
from findways.backend.dao.position import Position
from findways.backend.dao.routeManager import RouteManager
from findways.backend.dao.routeManager import convert_distance_into_meters
from findways.backend.dao.routeManager import convert_duration_into_minutes

from findways.backend.business.way import Way
from findways.backend.dao.uberManager import UberManager

""" Methods to get information about elementary ways """


def get_walking_elem(elem_departure_position, elem_arrival_position):
    """Elementary walking ways"""
    elemway = ElemWay(elem_departure_position, elem_arrival_position, 'w')
    route_manager = RouteManager(elemway.departure, elemway.arrival, elemway.type)
    elemway.steps = route_manager.steps
    elemway.duration = route_manager.duration
    elemway.distance = route_manager.distance
    elemway.price = 0
    return elemway


def get_cycling_elem(elem_departure_position, elem_arrival_position):
    """Elementary cycling ways"""
    elemway = ElemWay(elem_departure_position, elem_arrival_position, 'c')
    route_manager = RouteManager(elemway.departure, elemway.arrival, elemway.type)
    elemway.steps = route_manager.steps
    elemway.duration = route_manager.duration
    elemway.distance = route_manager.distance
    elemway.price = 0
    return elemway


def get_driving_elem(elem_departure_position, elem_arrival_position):
    """Elementary driving ways"""
    elemway = ElemWay(elem_departure_position, elem_arrival_position, 'd')
    route_manager = RouteManager(elemway.departure, elemway.arrival, elemway.type)
    elemway.steps = route_manager.steps
    elemway.duration = route_manager.duration
    elemway.distance = route_manager.distance
    elemway.price = 0
    return elemway


def get_transit_elem(elem_departure_position, elem_arrival_position):
    """Elementary transit ways"""
    transit_way = Way()
    route_manager = RouteManager(elem_departure_position, elem_arrival_position, 't')
    route_manager.steps = route_manager.get_steps()

    for step in route_manager.steps:
        e = ElemWay(Position(step['departure_location_lat'], step['departure_location_lng'], ""),
                    Position(step['arrival_location_lat'], step['arrival_location_lng'], ""))

        e.distance = convert_distance_into_meters(step['distance'])
        e.duration = convert_duration_into_minutes(step['duration'])

        if step['type'] == 'WALKING':
            e.type = 'w'
            e.steps = [{'instruction': step['instruction']}]

        if step['type'] == 'TRANSIT':
            e.type = 't'
            e.steps = [{'instruction': "Take Line {}, direction {} to {} from {} at {}".format(step['line'],
                        step['direction'], step['arrival_station'], step['departure_station'], step['departure_time'])}]
        transit_way = transit_way + e

    #transit_way.distance = route_manager.distance
    transit_way.price = 2.25
    transit_way.duration = route_manager.duration #convert_duration_into_minutes(route_manager.duration)

    return transit_way


def get_uber_elem(departure_position, arrival_position, dway):
    """Elementary Uber ways"""
    uber_list = UberManager(departure_position.latitude,departure_position.longitude, arrival_position.latitude, arrival_position.longitude, dway).get_uber()
    return uber_list


def get_station(latitude, longitude, transport_type):
    """Returns the nearest station from a certain point"""
    distance = 10000
    is_velib = True
    if transport_type == "b":
        is_velib = True
    elif transport_type == "c":
        is_velib = False
    is_autolib = not is_velib
    result = stationManager.StationManager().find_stations_in_radius(latitude, longitude, is_velib, is_autolib, distance)
    if len(result) > 0:
        return result[0]
    # Traiter le cas ou la liste des resultats est vide (augmenter le rayon de recherche)
    # Optimiser le choix de la premiere station


def station_converter_into_position(station):
    return position.Position(station.get_position().get_latitude(), station.get_position().get_longitude(), "")
