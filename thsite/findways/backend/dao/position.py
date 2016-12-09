import requests
import constants


class Position:

    def __init__(self, latitude, longitude, address):
        if latitude == 0 and longitude == 0:
            self.address = address
            self.latitude = Position.get_coordinates_from_address(self)[0]
            self.longitude = Position.get_coordinates_from_address(self)[1]
        elif address == "":
            self.latitude = latitude
            self.longitude = longitude
            self.address = Position.get_address_from_coordinates(self)
        else:
            # lever une exception
            print("Il y a un souci...")

    def get_address_from_coordinates(self):
        # Get address from Google Maps Geocoding API
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(self.latitude) + "," + str(self.longitude) + "&key=" + constants.google_maps_api_key
        result = requests.get(url).json()
        return result["results"][0]["formatted_address"]

    def get_coordinates_from_address(self):
        # Get coordinates from Google Maps Geocoding API
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + "\"{}\"".format(self.address) + "&key=" + constants.google_maps_api_key
        result = requests.get(url).json()
        return result["results"][0]["geometry"]["location"]["lat"], result["results"][0]["geometry"]["location"]["lng"]

    def get_coordinates(self):
        return [self.latitude, self.longitude]

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def get_address(self):
        return self.address
