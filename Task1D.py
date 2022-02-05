from floodsystem.stationdata import build_station_list
from test_geo import test_river_with_stations
from floodsystem.geo import river_with_station

def run():
    stations = build_station_list()
    test_river_with_stations()
    riverswithstations = river_with_station(stations)

    print(riverswithstations)

    
if __name__ == "__main__":
    run()
    