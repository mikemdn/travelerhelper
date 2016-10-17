from .station import Station


class VelibStation(Station):

    def __init__(self, latitude, longitude, capacity, availability, status):
        Station.__init__(self, latitude, longitude, capacity)
        self.availability = availability
        self.status = status

    def object_to_string(self):
        print("\nlongitude : " + str(self.position.longitude) + "\nlatitude : " + str(self.position.latitude) + "\ncapacity : " + str(self.capacity) + "\navailability : " + str(self.availability) + "\nstatus : " + str(self.status))