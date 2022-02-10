from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key
from . import datafetcher

def stations_highest_rel_level(stations, N):
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