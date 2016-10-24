from .position import Position


class Station:

    def __init__(self, latitude, longitude):
        position = Position(latitude, longitude, "")
        self.position = position

    def get_position(self):
        return self.position
