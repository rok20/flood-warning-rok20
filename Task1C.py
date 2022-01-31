from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_within_radius
from test_geo import test_stations_within_radius

def run():
    stations = build_station_list()

    # Test the function before running to make sure we get a list.
    test_stations_within_radius() 
    
    #use the function to create the list, centre (52.2053, 0.1218), radius 10km
    in_range_list = stations_within_radius(stations, (52.2053, 0.1218), 10)

    names = []
    for station in in_range_list:
        names.append(station.name)
    names.sort()
    print(names)
if __name__ == "__main__":
    run()