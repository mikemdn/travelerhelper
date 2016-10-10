class ElemWay:
    def __init__(self, type, duration, distance, price, steps):
        #TO DO : faire bien gaffe à comment les données sont récupérées
        self.type = type
        self.duration = duration
        self.distance = distance
        self.price = price
        self.steps = steps

    def __iter__(self):
        

