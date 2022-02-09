from floodsystem.stationdata import build_station_list
from test_geo import test_river_with_stations, test_stations_by_river
from floodsystem.geo import river_with_station, stations_by_river


def run():
    stations = build_station_list()
    test_river_with_stations()
    riverswithstations = river_with_station(stations)
    
    print("Number:", len(riverswithstations), "The first 10 are:", riverswithstations[:10])
    
if __name__ == "__main__":
    run()
    
def run():
    stations = build_station_list()
    test_stations_by_river()
    stationsbyriver = stations_by_river(stations)
    
    print("River Aire stations:", stationsbyriver["River Aire"])
    print("River Cam stations:", stationsbyriver["River Cam"])
    print("River Thames stations:", stationsbyriver["River Thames"])
    
    
if __name__ == "__main__":
    run()