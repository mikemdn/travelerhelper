from .position import Position


class Station:

    def __init__(self, latitude, longitude, capacity):
        position = Position(latitude, longitude, "")
        self.position = position
        self.capacity = capacity

    def get_position(self):
        return self.position
