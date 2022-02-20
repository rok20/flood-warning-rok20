from . import datafetcher
from . import stationdata
from .station import MonitoringStation
from .station import inconsistent_typical_range_stations
from .utils import sorted_by_key

def stations_highest_rel_level(stations, N):
    stationdata.update_water_levels(stations)
    #Create a list, and ensure using no None data, then make a list including the name and the difference between current level and the relative water level

    rel_level = []
    for station in stations:
        if station.latest_level != None:
            if station.relative_water_level() != None:
                x = station.relative_water_level()
                y = station.latest_level
                
                rel_level.append((station.name, y-x))
    #Sort the list from highest according to the most at risk. Then extract the first N

    rel_level.sort(key=lambda x:x[1], reverse=True)
    rel_level_final = rel_level[:N]

    return rel_level_final
    
    
#Take in a list of MonitoringStation objects and a tol value
#return a list of tuples (station with rel water level > tol, rel), sorted by rel high to low
def stations_level_over_threshold(stations, tol):
    stationdata.update_water_levels(stations)
    #create empty list
    x = []
    for station in stations:
        #record rel, only append tuple if rel exists and > tol
        rel = station.relative_water_level()
        if not rel == None:
            if rel > tol:
                x.append((station, rel))
    return sorted_by_key(x, 1, True)



