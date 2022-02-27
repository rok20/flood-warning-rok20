from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels, build_station_list
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

def test_stations_highest_rel_level():
    #I couldn't figure out how to put latest level into artificial stations
    #So I'm going to verify with real stations
    stations = build_station_list()
    update_water_levels(stations)

    #test that all returned stations have rel > tol, all not returned have rel <= tol
    stations_over = stations_level_over_threshold(stations, 0.8)
    isCorrect = True

    for station in stations:
        if station in stations_over:
            if station.relative_water_level() <= 0.8:
                isCorrect = False
        else:
            if station.relative_water_level() > 0.8:
                isCorrect = False
    
    assert isCorrect == True


    #check that the number of stations returned is correct
    highest_5 = stations_highest_rel_level(stations, 5)
    highest_10 = stations_highest_rel_level(stations, 10)
    highest_20 = stations_highest_rel_level(stations, 20)

    assert len(highest_5) == 5
    assert len(highest_10) == 10
    assert len(highest_20) == 20

