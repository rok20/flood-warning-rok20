from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from test_station import test_inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    test_inconsistent_typical_range_stations()
    Inconsistentlist = inconsistent_typical_range_stations(stations)
    namelist = []
    for inconsistent in Inconsistentlist:
        namelist.append(inconsistent.name)
    namelist.sort()
    print(namelist)

    
if __name__ == "__main__":
    run()
    
