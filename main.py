from travelerhelper.dao import stationManager

stationManager = stationManager.StationManager()
stationManager.find_stations_in_radius(48.862725, 2.287592, True, False, 2000)