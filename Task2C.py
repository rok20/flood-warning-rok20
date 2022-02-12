from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list

def run():
    # Build list of stations
    stations = build_station_list()
    
    x = stations_highest_rel_level(stations, 10)
    for item in x:
        print(item[0], item[1])

if __name__ == "__main__":
    run()