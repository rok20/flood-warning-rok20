from floodsystem.stationdata import build_station_list

from floodsystem.geo import river_with_station


stations = build_station_list()
riverswithstations = river_with_station(stations)

print(riverswithstations)

