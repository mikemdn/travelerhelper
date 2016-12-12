# -*- coding: utf-8 -*-

import requests
import re
import constants


def convert_distance_into_meters(text):
    coeff = 1
    reg = r"(([0-9]*.?[0-9]+)\s([a-z]+))"
    letters = re.finditer(reg, text, re.MULTILINE)
    for matchNum, letter in enumerate(letters):
        if letter.groups()[2] == 'km':
            coeff = 1000
        return float(letter.groups()[1]) * coeff


def convert_duration_into_minutes(text):
    try:
        reg = r"(([0-9]+)\s([a-z]+))"
        groups = re.finditer(reg, text, re.MULTILINE)
        min = 0
        for matchNum, group in enumerate(groups):
            if group.groups()[2] == 'd' or group.groups()[2] == 'day' or group.groups()[2] == 'days':
                min += int(group.groups()[1]) * 60 * 24
            elif group.groups()[2] == 'hours' or group.groups()[2] == 'hour' or group.groups()[2] == 'h':
                min += int(group.groups()[1]) * 60
            elif group.groups()[2] == 'mins' or group.groups()[2] == 'min':
                min += int(group.groups()[1])
    except TypeError:
        min = text
    return min


def remove_tags(text):
    tags =re.compile('<.*?>')
    cleantext = re.sub(tags,'', text)
    return cleantext


def set_transport(code):
    if code == 'w':
        return 'walking'
    if code == 'c':
        return 'bicycling'
    if code == 'd':
        return 'driving'
    if code == 't':
        return 'transit'
    else:
        pass


class RouteManager:

    def __init__(self, departure, destination, mean_of_transport):
        # departure and destination are two objects Position
        # mean_of transport must be in the following list : driving, walking, bicycling, transit
        self.transport = set_transport(mean_of_transport)
        self.departure_latitude = departure.get_latitude()
        self.departure_longitude = departure.get_longitude()
        self.departure_address = departure.address
        self.destination_latitude = destination.get_latitude()
        self.destination_longitude = destination.get_longitude()
        self.destination_address = destination.address

        self.url = "https://maps.googleapis.com/maps/api/directions/json?origin={},{}&destination={},{}&mode={}&key={}".format(self.departure_latitude, self.departure_longitude, self.destination_latitude, self.destination_longitude, self.transport, constants.google_maps_api_key)

        self.reply = requests.get(self.url)
        self.dict_reply = self.reply.json()
        self.steps = self.get_steps()
        self.distance = convert_distance_into_meters(self.dict_reply['routes'][0]['legs'][0]['distance']['text'])
        self.duration = convert_duration_into_minutes(self.dict_reply['routes'][0]['legs'][0]['duration']['text'])

    def get_steps(self):
        steps = self.dict_reply['routes'][0]['legs'][0]['steps']
        steps_info = []
        for item in steps:
            step_distance = item['distance']['text']
            step_duration = item['duration']['text']
            step_instruction = remove_tags(item['html_instructions'])

            if self.transport == "transit":
                step_mode = item["travel_mode"]
                step_departure_location_latitude = ""
                step_departure_location_longitude = ""
                step_arrival_location_latitude = ""
                step_arrival_location_longitude = ""
                step_line = ""
                step_num_stations = ""
                step_departure_station = ""
                step_arrival_station = ""
                step_direction = ""
                step_arrival_time = ""
                step_departure_time = ""

                if step_mode =="TRANSIT":
                    step_line = item['transit_details']['line']['short_name']
                    step_num_stations = item['transit_details']['num_stops']
                    step_departure_station = item['transit_details']['departure_stop']['name']
                    step_arrival_station = item['transit_details']['arrival_stop']['name']
                    step_direction = item['transit_details']['headsign']
                    step_arrival_time = item['transit_details']['arrival_time']['text']
                    step_departure_time = item['transit_details']['departure_time']['text']
                    step_departure_location_latitude = item['transit_details']['departure_stop']['location']['lat']
                    step_departure_location_longitude = item['transit_details']['departure_stop']['location']['lng']
                    step_arrival_location_latitude = item['transit_details']['arrival_stop']['location']['lat']
                    step_arrival_location_longitude = item['transit_details']['arrival_stop']['location']['lng']
                    step_instruction = "Take Line {}, direction {} to {} from {} at {} ({} stations)".format(step_line.encode('utf-8'),
                        step_direction.encode('utf-8'), step_arrival_station.encode('utf-8'), step_departure_station.encode('utf-8'),
                        step_departure_time.encode('utf-8'), step_num_stations)

                if step_mode == "WALKING":
                    step_departure_location_latitude = item['start_location']['lat']
                    step_departure_location_longitude = item['start_location']['lng']
                    step_arrival_location_latitude = item['end_location']['lat']
                    step_arrival_location_longitude = item['end_location']['lng']

                steps_info.append(
                    {'distance': step_distance, 'duration': step_duration, 'instruction': step_instruction,
                     'type' : step_mode, 'line' : step_line, 'stops' : step_num_stations,
                     'departure_station' : step_departure_station, 'arrival_station' : step_arrival_station,
                     'direction' : step_direction, 'arrival_time' : step_arrival_time, 'departure_time' : step_departure_time,
                     'departure_location_lat' : step_departure_location_latitude, 'departure_location_lng' : step_departure_location_longitude,
                     'arrival_location_lat' : step_arrival_location_latitude, 'arrival_location_lng' : step_arrival_location_longitude})
            else:
                steps_info.append(
                    {'distance': step_distance, 'duration': step_duration, 'instruction': step_instruction})

        return steps_info

    def get_distance(self):
        return self.distance

    def get_duration(self):
        return self.duration

    def get_departure_address(self):
        return self.departure_address

    def get_destination_address(self):
        return self.destination_address
