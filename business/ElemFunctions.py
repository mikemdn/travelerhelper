from business.ElemWay import ElemWay
from dao import position
from dao import stationManager
from dao.routeManager import RouteManager

#### METHODES ELEMENTAIRES

def get_walking_elem(elem_departure_position, elem_arrival_position):
    elemway = ElemWay(elem_departure_position, elem_arrival_position, 'w')
    route_manager = RouteManager(elemway.departure, elemway.arrival, elemway.type)
    elemway.steps = route_manager.steps
    elemway.duration = route_manager.duration
    elemway.distance = route_manager.distance
    elemway.price = 0
    return(elemway)

"""
def get_cycling_elem(elem_departure_position, elem_arrival_position):
    elemway = ElemWay(elem_departure_position, elem_arrival_position, 'c')
    route_manager = RouteManager(elemway.departure, elemway.arrival, elemway.type)
    elemway.steps = route_manager.steps
    elemway.duration = route_manager.duration
    elemway.distance = route_manager.distance
    elemway.price = 0
    return(elemway)
"""

def get_driving_elem(elem_departure_position, elem_arrival_position):
    elemway = ElemWay(elem_departure_position, elem_arrival_position, 'd')
    route_manager = RouteManager(elemway.departure, elemway.arrival, elemway.type)
    elemway.steps = route_manager.steps
    elemway.duration = route_manager.duration
    elemway.distance = route_manager.distance
    elemway.price = 0
    return(elemway)

"""
def get_transit_elem(elem_departure_position, elem_arrival_position):
    return (ElemWay())"""


def get_station(latitude, longitude, type):
    distance = 10000
    if type == "b":
        is_velib = True
    elif type == "c":
        is_velib = False
    is_autolib = not is_velib
    result = stationManager.StationManager().find_stations_in_radius(latitude, longitude, is_velib, is_autolib, distance)
    if len(result) > 0:
        return result[0]
    # Traiter le cas ou la liste des resultats est vide (augmenter le rayon de recherche)
    # Optimiser le choix de la premiere station


def station_converter_into_position(station):
    return position.Position(station.get_position().get_latitude(), station.get_position().get_longitude(), "")

