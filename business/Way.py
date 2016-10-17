class Way:
    def __init__(self, *elemWays):
        self.elemWaysTable = []
        self.duration = 0
        self.distance = 0
        self.price = 0
        self.type = []

    def __add__(self, other):
        waySum = Way()
        waySum.price = self.price + other.price
        waySum.distance= self.distance + other.distance
        waySum.type = self.type
        waySum.elemWaysTable = self.elemWaysTable

        if isinstance(other, Way):
            waySum.elemWaysTable += other.elemWaysTable
            for i in range(len(other.type)):
                if other.type[i] not in waySum.type:
                    waySum.type += other.type[i]

        else:
            waySum.elemWaysTable.append(other)

            if other.type not in waySum.type:
                waySum.type += other.type

        return(waySum)
