class Station:

    radius = 300

    def __init__(self, latitude, longitude, capacity, availability, status):
        self.latitude = latitude
        self.longitude = longitude
        self.capacity = capacity
        self.availability = availability
        self.status = status

    def is_available(self):
        if self.status and self.availability > 0:
            return True
        else:
            return False

    def get_available_item_number(self):
        return self.availability
