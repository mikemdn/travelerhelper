import requests
import re
from dao.position import Position
#from elemWay import ElemWay

def convert_distance_into_meters(text):
    coeff = 1
    reg = r"([a-z]+)"
    letters = re.finditer(reg, text, re.MULTILINE)
    for matchNum, letter in enumerate(letters):
        if letter.group() == 'km':
            coeff = 1000
        break
    regex = r"([0-9]+.?[0-9]+)"
    numbers = re.finditer(regex, text, re.MULTILINE)
    for matchNum, number in enumerate(numbers):
        return (float(number.group()) * coeff)

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

class RouteManager():

    def __init__(self, departure, destination, mean_of_transport):
        #departure and destination are two objects Position
        #mean_of transport must be in the following list : driving, walking, bicycling, transit
        self.transport = set_transport(mean_of_transport)
        self.departure_latitude = departure.get_latitude()
        self.departure_longitude = departure.get_longitude()
        self.departure_address = departure.address
        self.destination_latitude = destination.get_latitude()
        self.destination_longitude = destination.get_longitude()
        self.destination_address = destination.address
        #self.mean_of_transport = elemway.type
        self.url = "https://maps.googleapis.com/maps/api/directions/json?origin={},{}&destination={},{}&mode={}&key=AIzaSyADxwwZWNKCrpZ2RXfO5U_a7rwCBW54-j0".format(self.departure_latitude, self.departure_longitude, self.destination_latitude, self.destination_longitude, self.transport)
        print(self.url)
        self.reply = requests.get(self.url)
        self.dict_reply = self.reply.json()
        self.steps = []
        self.distance = convert_distance_into_meters(self.dict_reply['routes'][0]['legs'][0]['distance']['text'])
        self.duration = self.dict_reply['routes'][0]['legs'][0]['duration']['text']


    def get_steps(self):
        steps = self.dict_reply['routes'][0]['legs'][0]['steps']
        if self.steps == []:
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

                    if step_mode == "WALKING":
                        step_departure_location_latitude = item['start_location']['lat']
                        step_departure_location_longitude = item['start_location']['lng']
                        step_arrival_location_latitude = item['end_location']['lat']
                        step_arrival_location_longitude = item['end_location']['lng']





                    self.steps.append(
                        {'distance': step_distance, 'duration': step_duration, 'instruction': step_instruction,
                         'type' : step_mode, 'line' : step_line, 'stops' : step_num_stations,
                         'departure_station' : step_departure_station, 'arrival_station' : step_arrival_station,
                         'direction' : step_direction, 'arrival_time' : step_arrival_time, 'departure_time' : step_departure_time,
                         'departure_location_lat' : step_departure_location_latitude, 'departure_location_lng' : step_departure_location_longitude,
                         'arrival_location_lat' : step_arrival_location_latitude, 'arrival_location_lng' : step_arrival_location_longitude})


                else :
                    self.steps.append(
                        {'distance': step_distance, 'duration': step_duration, 'instruction': step_instruction})

        return self.steps

    def display_steps(self):
        step_num = 1
        self.get_steps()
        if 'line' in self.steps[0].keys():
            print("{:14}{:14}{:14}{:50}{:10}{:7}{:10}{:40}{:40}{:40}{:20}{:20}{:20}{:20}{:20}{:20}".format("Steps", "Duration", "Distance", "Instruction","Type",
                                                                     "Line", "Stops", "Departure Station", "Arrival Station", "Direction",
                                                                             "Arrival Time", "Departure Time", "Dep Lat", "Dep Lng", "Arr Lat",
                                                                             "Arr Lng"))


        else :
            print("{:14}{:14}{:14}{:50}".format("Steps", "Duration", "Distance", "Instruction"))



        print("-"*200)
        if 'line' in self.steps[0].keys():
            for step in self.steps:
                print("{:14}{:14}{:14}{:50}{:10}{:7}{:10}{:40}{:40}{:40}{:20}{:20}{:20}{:20}{:20}{:20}".format(
                str(step_num), step['duration'], step['distance'], step['instruction'], step['type'], step['line'],
                str(step['stops']), step['departure_station'], step['arrival_station'], step['direction'], str(step['arrival_time']),
                str(step['departure_time']), str(step['departure_location_lat']), str(step['departure_location_lng']), str(step['arrival_location_lat']),
                    str(step['departure_location_lng'])))
                step_num += 1

        else :
            for step in self.steps:
                print("{:14}{:14}{:14}{:50}".format(
                    str(step_num), step['duration'], step['distance'], step['instruction']))
                step_num += 1




    def get_distance(self):
        return self.distance

    def get_duration(self):
        return self.duration

    def get_departure_address(self):
        return self.departure_address

    def get_destination_address(self):
        return self.destination_address

    def display_addresses(self):
        print('{:14} : {} \n{:14} : {}'.format('Start Address', self.get_departure_address(), 'Destination', self.get_destination_address()))

    def display_distance_duration(self):
        print('{:14} : {} \n{:14} : {}'.format('Total duration',self.get_duration(), 'Total distance', self.get_distance()))

    def display_all(self):
        self.display_addresses()
        self.display_distance_duration()
        print('')
        self.display_steps()

if __name__ == "__main__":
    start_location = Position(48.837284, 2.472064, "")
    autolib_depart = Position(48.864136, 2.2883, "")
    autolib_arrivee = Position(48.856579, 2.353831, "")
    end_location = Position(48.848009, 2.312288, "")

    route1 = RouteManager(start_location, end_location, 't')
    route1.display_all()