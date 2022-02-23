from floodsystem.analysis import polyfit
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels
import numpy as np

def test_polyfit():
     # Create a station
    dates = ['2008-12-01T00:00:59.000000000-0800',
                 '2008-12-01T00:00:59.000000000-0800',
                 '2008-12-01T00:00:59.000000000-0800',
                 '2008-12-01T00:09:26.000000000-0800',
                 '2008-12-01T00:09:41.000000000-0800']
    levels = [0.1, 0.2, 0.3, 0.4, 0.5]
    x = polyfit(dates, levels, 2)
    
    assert round(x[0](0), 5) == 2.00000e-01
    assert round(x[0](1), 1) == 89204.6
    assert round(x[1],1) == 14214.3
