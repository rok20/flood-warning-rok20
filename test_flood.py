from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels, build_station_list
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

def test_stations_highest_rel_level():

    stations = build_station_list()
    update_water_levels(stations)



    #check that the number of stations returned is correct
    highest_5 = stations_highest_rel_level(stations, 5)
    highest_10 = stations_highest_rel_level(stations, 10)
    highest_20 = stations_highest_rel_level(stations, 20)

    assert len(highest_5) == 5
    assert len(highest_10) == 10
    assert len(highest_20) == 20

def test_stations_level_over_threshold():
    #I couldn't figure out how to put latest level into artificial stations
    #So I'm going to verify with real stations
    stations = build_station_list()
    update_water_levels(stations)

    #test that all returned stations have rel > tol, all not returned have rel <= tol
    temp = stations_level_over_threshold(stations, 0.8)
    stations_over = []
    for each in temp:
        stations_over.append(each[0])

    isCorrect = True

    for station in stations:
        rel = station.relative_water_level()
        if station in stations_over:
            #print('not empty')
            if rel <= 0.8 or rel == None:
                isCorrect = False
        elif station not in stations_over:
            if rel != None:
                if rel > 0.8:
                    isCorrect = False
                    #print('is over 0.8')
    
    assert isCorrect == True
