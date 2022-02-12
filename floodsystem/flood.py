from . import datafetcher
from . import stationdata
from .station import MonitoringStation 
from .station import inconsistent_typical_range_stations


def stations_highest_rel_level(stations, N):
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
    
    
        



