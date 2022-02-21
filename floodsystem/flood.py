from . import stationdata
from .station import MonitoringStation
from .station import inconsistent_typical_range_stations
from .utils import sorted_by_key

def stations_highest_rel_level(stations, N):
    stationdata.update_water_levels(stations)
    #create a list to hold tuples of all stations and their relative water level

    rel_level = []
    for station in stations:
        if station.relative_water_level() != None and station.relative_water_level() < 10: 
            rel_level.append((station, station.relative_water_level()))
    #sort the list by relative water level in descending order
    rel_level = sorted_by_key(rel_level, 1, True)
    #take the station object of the first N terms of the previous list and make into a new list
    first_N = []
    for i in range(N):
        first_N.append(rel_level[i][0])
        
    return first_N
    
    
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



