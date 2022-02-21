from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list

def run():
    # Build list of stations
    stations = build_station_list()
    
    x = stations_highest_rel_level(stations, 10)
    print(x)
    for item in x:
        print(item.name, item.relative_water_level())

if __name__ == "__main__":
    run()