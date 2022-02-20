from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
import datetime
import floodsystem.station

def run():
    # Build list of stations
    stations = build_station_list()
    listof5 = stations_highest_rel_level(stations, 5)
    listofdata = 5*[]
    dt = 2
    print(stations)
    for i in range(5):
        if stations.name == listof5[i]:
            listofdata[i] = (stations.name, stations.measure_id, datetime.timedelta(days=dt))

   

if __name__ == "__main__":
    run()