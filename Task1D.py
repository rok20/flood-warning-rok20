from floodsystem.stationdata import build_station_list

from floodsystem.geo import river_with_station

def run():
    stations = build_station_list()
    riverswithstations = river_with_station(stations)

    print(riverswithstations)

    
if __name__ == "__main__":
    run()