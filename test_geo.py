from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, river_with_station

#Ensure that Task1B runs and is a list.
def test_stations_by_distance():
    
    stations = build_station_list()
    station_distance = stations_by_distance(stations, (0,0))
    
    assert type(station_distance) == list

#Ensure the data is alphabetical and no repeats.
def test_river_with_stations():

    stations = build_station_list()
    rivers_list = river_with_station(stations)
    
    for i in range(len(rivers_list)):
        
        for j in range(len(list(rivers_list.values())[i])-1):
            
            assert list(rivers_list.values())[i][j] < list(rivers_list.values())[i][j+1]
