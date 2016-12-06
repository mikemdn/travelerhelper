from findways.backend.dao import routeManager


class Way:
    def __init__(self, *elemWays):
        self.elemWaysTable = []
        self.duration = 0
        self.distance = 0
        self.price = 0
        self.type = []

    def __add__(self, other):
        way_sum = Way()
        way_sum.price = self.price + other.price
        way_sum.distance = self.distance + float(other.distance)
        way_sum.duration = self.duration + float(other.duration)
        way_sum.type = self.type
        way_sum.elemWaysTable = self.elemWaysTable
        way_sum.duration = self.duration + routeManager.convert_duration_into_minutes(other.duration)

        if isinstance(other, Way):
            way_sum.elemWaysTable += other.elemWaysTable
            for i in range(len(other.type)):
                if other.type[i] not in way_sum.type:
                    way_sum.type += other.type[i]

        else:
            way_sum.elemWaysTable.append(other)

            if other.type not in way_sum.type:
                way_sum.type += other.type

        return way_sum

    def __repr__(self):
        return "<Type {} (distance = {}, duration = {}, price = {} >"\
            .format(self.type, self.distance, self.duration, self.price)
