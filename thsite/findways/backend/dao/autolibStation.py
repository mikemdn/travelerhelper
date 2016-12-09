from .station import Station


class AutolibStation(Station):

    def __init__(self, latitude, longitude, capacity):
        Station.__init__(self, latitude, longitude)
        self.capacity = capacity
