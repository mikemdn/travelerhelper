import business

class Way:
    def __init__(self,*elemWays):
        self.elemWaysTable=[]
        self.duration=0
        self.distance=0
        self.price=0
        self.steps={}
        self.type=[]


    def __add__(self,other):
        waySum=Way()
        waySum.price = self.price + other.price
        waySum.steps = self.steps + other.steps
        waySum.distance= self.distance + other.distance
        waySum.type = self.type
        waySum.elemWaysTable=self.elemWaysTable

        if isinstance(other,Way):
            waySum.elemTable+=other.elemWaysTable
            for type in other.type:
                if type not in waySum.type:
                    waySum.type+=type

        else:
            waySum.elemTable+=other.elemWaysTable

            if other.type not in waySum.type:
                waySum.type+=other.type

        return waySum









