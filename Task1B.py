from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from test_geo import test_stations_by_distance

def run():
    stations = build_station_list()

    # Test the function before running to make sure we get a list.
    test_stations_by_distance() 
    
    x = stations_by_distance(stations, (52.2053, 0.1218))

    print(x)
if __name__ == "__main__":
    run()
    