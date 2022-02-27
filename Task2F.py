from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
import datetime
import floodsystem.station
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
from test_analysis import test_polyfit

def run():
    #Test the function polyfit
    test_polyfit()
    # Build list of stations
    stations = build_station_list()
    listof5 = stations_highest_rel_level(stations, 5)
    listofdata = []
    typicalhighlow = []
    dt = 2
    #Find all stations that are highest relative water level and extract necessray data
    for i in stations:
        for j in listof5:
            if i.name == j.name:
                
                dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
                listofdata.append([i.name, dates, levels]) 
                typicalhighlow.append(i.typical_range) 
                
    #iterate over list to plot a graph for each case and provide high low lines.
    for n in range(5):
        plot_water_level_with_fit(listofdata[n][0], listofdata[n][1], listofdata[n][2], 4)
        
        plt.axhline(y = typicalhighlow[n][0], color = 'b', label = "Typical range low")
        plt.axhline(y = typicalhighlow[n][1], color = 'r', label = "Typical range high")
        plt.show()
    


if __name__ == "__main__":
    run()