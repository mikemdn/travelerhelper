import requests
import constants


class Position:

    def __init__(self):
        self.latitude = 0
        self.longitude = 0
        self.address = ""

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_address_from_coordinates(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        # Get address from Google Maps Geocoding API
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(self.latitude) + "," + str(self.longitude) + "&key=" + constants.google_maps_api_key
        result = requests.get(url).json()
        self.address = result["results"][0]["formatted_address"]

    def get_coordinates_from_address(self, address):
        self.address = address
        # Get coordinates from Google Maps Geocoding API
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + self.address + "&key=" + constants.google_maps_api_key
        result = requests.get(url).json()
        self.latitude = result["results"][0]["geometry"]["location"]["lat"]
        self.longitude = result["results"][0]["geometry"]["location"]["lng"]
        print(self.latitude)
        print(self.longitude)

    def get_coordinates(self):
        return [self.latitude, self.longitude]

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def get_address(self):
        return self.address
