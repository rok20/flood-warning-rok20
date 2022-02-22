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
    s = [MonitoringStation(s_id, m_id, label, coord, trange, river, town)]
    x = stations_highest_rel_level(s, 1)

print(test_stations_highest_rel_level())