import business
from dao.position import Position
class ElemWay:
    def __init__(self, departure, arrival, type='w', duration=0, distance=0, price=0, steps=[]):
        #TO DO : faire bien gaffe à comment les données sont récupérées
        self.type = type
        self.duration = duration
        self.distance = distance
        self.price = price
        self.steps = steps
        self.departure = departure
        self.arrival= arrival

a=ElemWay()
a.price=10
a.distance=20
a.steps=["droite","gauche"]
a.type='w'

b=ElemWay()
b.price=80
b.distance=25
b.steps=["gauche","gauche"]
b.type='d'