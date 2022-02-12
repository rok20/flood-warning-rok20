from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key
from . import datafetcher
from . import stationdata
from .station import MonitoringStation 
from .station import inconsistent_typical_range_stations


def stations_highest_rel_level(stations, N):
<<<<<<< HEAD
    stationdata.update_water_levels(stations)

    rel_level = []
    for station in stations:
        if station not in inconsistent_typical_range_stations(stations):
            if station.latest_level != None:
                x = station.typical_range
                y = station.latest_level
            
                rel_level.append((station.name, y - x[1]))
    rel_level.sort(key=lambda x:x[1], reverse=True)
    rel_level_final = rel_level[:N]

    return rel_level_final
    
    
        



=======
    data = datafetcher.fetch_latest_water_level_data()

#Take in a list of MonitoringStation objects and a tol value
#return a list of tuples (station with rel water level > tol, rel), sorted by rel high to low
def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    #create empty list
    x = []
    for station in stations:
        #record rel, only append tuple if rel exists and > tol
        rel = station.relative_water_level()
        if not rel == None:
            if rel > tol:
                x.append((station, rel))
    return sorted_by_key(x, 1, True)
>>>>>>> 436456f5880a8a6ae6a02bfb077305b7c0037db3
