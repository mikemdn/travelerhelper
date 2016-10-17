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
                self.steps.append({'distance' : step_distance, 'duration' : step_duration, 'instruction' : step_instruction})
        return self.steps

    def display_steps(self):
        step_num = 1
        self.get_steps()
        print("{:14}{:14}{:14}{}".format("Steps", "Duration", "Distance", "Instruction"))
        print("-"*80)
        for step in self.steps:
            print("{:14}{:14}{:14}{}".format(
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
    start_location = Position(48.862725, 2.287592, "")
    autolib_depart = Position(48.864136, 2.2883, "")
    autolib_arrivee = Position(48.856579, 2.353831, "")
    end_location = Position(0, 0, "Paris")

    route1 = RouteManager(start_location, autolib_depart, 'w')
    route2 = RouteManager(autolib_depart, autolib_arrivee, 'd')
    route3 = RouteManager(autolib_arrivee, end_location, 'w')

    route1.display_all()
    route2.display_all()
    route3.display_all()