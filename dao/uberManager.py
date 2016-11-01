import requests
import constants
from dao.uber import *


class UberManager:
    """Class that allows us to get information of a ride from the Uber API"""
    def __init__(self, start_latitude, start_longitude, end_latitude, end_longitude, dway):
        self.start_latitude = str(start_latitude)
        self.start_longitude = str(start_longitude)
        self.end_latitude = str(end_latitude)
        self.end_longitude = str(end_longitude)
        self.elemwayTable = dway.elemWaysTable
        self.duration = dway.duration
        self.distance = dway.distance
        self.uberTable = self.get_uber()

    def get_uber(self):
        uber_list = []
        url = "https://api.uber.com/v1/estimates/price?start_latitude=" + self.start_latitude + "&start_longitude=" + self.start_longitude + "&end_latitude=" + self.end_latitude + "&end_longitude=" + self.end_longitude + "&server_token=" + str(constants.uber_api_key)
        response = requests.get(url).json()["prices"]
        for option in response:
            #Creation of a new Uber object
            uber = Uber()
            #Gives it attributes thanks to the Uber API
            uber.display_name = option["display_name"]
            uber.low_price_estimate = option["low_estimate"]
            uber.high_price_estimate = option["high_estimate"]
            uber.price = remove_symbol(option["estimate"])
            uber.surge_multiplier = option["surge_multiplier"]
            uber.wait_time = option["duration"]
            #Gives it information about distance and duration thanks to Google Maps
            uber.duration = self.duration
            uber.distance = self.distance
            #Gives it a default step
            elemway = self.elemwayTable[0]
            elemway.steps = [{'distance': '', 'duration':'','instruction':'Connect to the Uber App !'}]
            uber.elemWaysTable = [elemway]
            uber_list.append(uber)
        return uber_list

    def display_uber(self):
        for uber in self.uberTable:
            uber.uber_to_string()
            print('')

if __name__ == "__main__":
    uberRoute = UberManager(48.771896, 2.2707479999999998, 48.856614, 2.3522219)
    uberRoute.display_uber()