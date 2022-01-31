from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, river_with_station, stations_within_radius, rivers_by_station_number

#Ensure that Task1B runs and is a list.
def test_stations_by_distance():
    
    stations = build_station_list()
    station_distance = stations_by_distance(stations, (0,0))
    
    assert type(station_distance) == list

#Ensure task 1c runs
def test_stations_within_radius():
    stations = build_station_list()
    in_range_list = stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert type(in_range_list) == list

#Ensure the data is alphabetical and no repeats.
def test_river_with_stations():

    stations = build_station_list()
    rivers_list = river_with_station(stations)
    
    for i in range(len(rivers_list)):
        
        for j in range(len(list(rivers_list.values())[i])-1):
            
            assert list(rivers_list.values())[i][j] < list(rivers_list.values())[i][j+1]

def test_river_by_station_number():
    stations = build_station_list()
    river_station_count = rivers_by_station_number(stations, 10)
    assert type(river_station_count) == list
