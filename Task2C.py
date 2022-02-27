from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    
    x = stations_highest_rel_level(stations, 10)
    
    for item in x:
        print(item.name, item.relative_water_level())

if __name__ == "__main__":
    run()