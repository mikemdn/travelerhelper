import business

class WayManager:
    def __init__(self,**request):
        self.departure=request["departure"]
        self.arrival = request["arrival"]
        self.meteo = request["meteo"]
        self.rich = request["rich"]
        self.bike = request["bike"]

    def get_relevant_ways(self):
        #way is a list of Ways().
        ways= []

        return ways
