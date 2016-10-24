from .station import Station


class AutolibStation(Station):

    def __init__(self, latitude, longitude, capacity):
        Station.__init__(self, latitude, longitude)
        self.capacity = capacity

    def object_to_string(self):
        print("\nLatitude : " + str(self.position.latitude) + "\nLongitude : " + str(self.position.longitude) + "\nCapacity : " + str(self.capacity))


