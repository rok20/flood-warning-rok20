from floodsystem.stationdata import build_station_list
from test_geo import test_river_by_station_number
from floodsystem.geo import rivers_by_station_number

def run():
    stations = build_station_list()
    test_river_by_station_number
    river_station_count = rivers_by_station_number(stations, 11)

    print(river_station_count)

    
if __name__ == "__main__":
    run()