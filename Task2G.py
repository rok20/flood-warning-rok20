#Initial ideas::: Consider gradiwnt of line in polyfit? Consider how high above the typical high (relative height?), 
#Severe rising and a lot above the top band
#High rising and above the top band/ 
#Moderate rising and between the two bands/ decreasing but above the highest
#Low not rising and not above usual heighest

#write a function to determine gradient of line? Since the polyfit is set so 0 is present, the x coefficient is the gradient at present day
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime

stations = build_station_list()
listforgrad = []
dt = 1
for station in stations:
    if station.measure_id != None:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        listforgrad.append((station.name, dates, levels))
    
def gradient(dates, levels):
    list = polyfit(dates, levels, 4)
    print(list)

