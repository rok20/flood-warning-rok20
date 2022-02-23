from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level

def test_stations_highest_rel_level():

# Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"

    s_id2 = "test-s-id2"
    m_id2 = "test-m-id2"
    label2 = "some station2"
    coord2 = (-2.02, 4.02)
    trange2 = (-5.3, 9.4445)
    river2 = "River X2"
    town2 = "My Town2"

    s_id3 = "test-s-id3"
    m_id3 = "test-m-id3"
    label3 = "some station3"
    coord3 = (-1.02, 6.02)
    trange3 = (-1.3, 4.4845)
    river3 = "River X3"
    town3 = "My Town3"

    s = [MonitoringStation(s_id, m_id, label, coord, trange, river, town), MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2), MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)]
    
    x = stations_highest_rel_level(s, 1)
    
test_stations_highest_rel_level()