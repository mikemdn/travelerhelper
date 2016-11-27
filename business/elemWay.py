class ElemWay:
    def __init__(self, departure, arrival, type='w', duration=0, distance=0, price=0, steps=[]):
        # TODO : faire bien attention à comment les données sont récupérées
        self.type = type
        self.duration = duration
        self.distance = distance
        self.price = price
        self.steps = steps
        self.departure = departure
        self.arrival = arrival
