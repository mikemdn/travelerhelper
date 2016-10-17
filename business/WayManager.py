import business

class WayManager:
    def __init__(self,**request):
        self.arrival = request["destination"]
        self.meteo = 10
        self.rich = request["rich"]
        self.bike = request["bike"]
        self.walk = request["walk"]
        self.charged = request["charged"]
        self.credit_card = request["credit card"]
        self.driving_license= request["driving licence"]
        self.geo_departure=0
        self.geo_arrival=0


    def get_relevant_ways(self):
        #way is a list of Ways().
        ways=[]
        if self.charged:
            ways+=WayManager.get_autolib_way()
            ways+=WayManager.get_driving_way()
        elif self.meteo > 5 :
            ways+=WayManager.get_walking_way()
            ways+=WayManager.get_cycling_way()
            ways+=WayManager.get_transit_way()
        else:
            ways+=WayManager.get_transit_way()


        return ways

    #### METHODES GLOBALES

    def get_walking_way(self):
        wway_elem=WayManager.get_walking_elem(geo_departure,geo_arrival)
        wway=Way()
        wway=Way+wway_elem
        return(wway)

    def get_cycling_way(self):
        departure_station,arrival_station=get_stations(departure,arrival)
        cway=Way()
        cway=cway+WayManager.get_walking_elem(self.geo_arrival,departure_station)
        cway=cway+WayManager.get_cycling_elem(departure_station,arrival_station)
        cway=cway+WayManager.get_walking_elem(arrival_station,self.arrival)
        return(cway)

    def get_driving_way(self):
        dway_elem=WayManager.get_driving_elem(geo_departure,geo_arrival)
        dway=Way()
        dway=Way+dway_elem
        return(dway)

    def get_transit_way(self):
        tway = Way()
        return(tway)

    def get_autolib_way(self):
        departure_station,arrival_station=get_stations(departure,arrival)
        dway=Way()
        dway=dway+WayManager.get_walking_elem(self.geo_arrival,departure_station)
        dway=dway+WayManager.get_driving_elem(departure_station,arrival_station)
        dway=dway+WayManager.get_driving_elem(arrival_station,self.arrival)
        return(dway)

    #### METHODES ELEMENTAIRES
    def get_walking_elem(departure,arrival):
        return(ElemWay())

    def get_cycling_elem(departure,arrival):
        return (ElemWay())

    def get_driving_elem(departure,arrival):
        return (ElemWay())

    def get_transit_elem(departure,arrival):
        return (ElemWay())

    def get_stations(departure,arrival):
        return(departure_station,arrival_station)

    def geolocation(address):
        return(longitude,latitude)