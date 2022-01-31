from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    
    Inconsistentlist = inconsistent_typical_range_stations(stations)

    print(Inconsistentlist)

    
if __name__ == "__main__":
    run()
    
