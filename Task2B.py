from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from test_flood import stations_level_over_threshold, test_stations_level_over_threshold

def run():
    # Build list of stations
    stations = build_station_list()

    test_stations_level_over_threshold()

    x = stations_level_over_threshold(stations, 0.8)
    
    for each in x:
        #This is a faulty station
        if each[0].name != 'Letcombe Bassett':
            print(each[0].name, each[1])

if __name__ == "__main__":
    run()