from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list

stations = build_station_list()
x = stations_highest_rel_level(stations, 10)
print(x)