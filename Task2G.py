#Initial ideas::: Consider gradiwnt of line in polyfit? Consider how high above the typical high (relative height?), 
#Severe rising and a lot above the top band
#High rising and above the top band/ 
#Moderate rising and between the two bands/ decreasing but above the highest
#Low not rising and not above usual heighest


#write a function to determine gradient of line? Since the polyfit is set so 0 is present, the x coefficient is the gradient at present day
import string
from time import time
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import floodsystem.datafetcher
from numba import jit
from floodsystem.flood import stations_level_over_threshold
import floodsystem.station

#My definition for the different levels of flooding:
#condition for already flooding: relative water level (hereby rel) > 1
#low risk: rel < tol_low,set at 0.8
#moderate risk: tol_low < rel< 1, and currently not increasing (potentially can flood, not yet)
#high risk: 1. tol_low < rel < 1, and is increasing; 2. rel > 1, and not increasing
#severe: rel > 1, and increasing

stations = build_station_list()
update_water_levels(stations)
listforgrad = []
#fetch data for only the past 3 hrs
dt = 0.125

#tolerance relative water level for low risk
tol_low = 0.8
#gradient threshold
k_0 = 0.5

# Four categories and then look at initial conditions to sort into 4 groups ?
severe = []
high = []
moderate = []
low = []

#to make code clear
def print_station_names(stations):
    for station in stations:
        print(station.name, end=' ')
    print()

#def gradient(dates, levels):
    
    #list = polyfit(dates, levels, 4)
    #return list



#preprocess station data to decrease number of stations for further inspection
#exclude and separate low risk stations, they do not need more calculations
exclude_low = []
for item in stations_level_over_threshold(stations, tol_low):
    exclude_low.append(item[0])
for station in stations:
    if station not in exclude_low:
        low.append(station)



gradientlist = []
#Test how long it takes to calculate gradients
#print('Starting gradient calculation')
#gradientlist = [(station.name, gradient(fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt)))[0][1], fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))[1][0], station.typical_range) for station in stations]
for station in exclude_low:    
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

    try:
        polynomial = polyfit(dates, levels, 3)
        #make a list of tuples with station itself and the linear gradient of the last 3 hrs 
        gradientlist.append((station, polynomial[0][1]))
    except:
        pass

#print('Finished gradient calculation')




#print('start classifying')
for item in gradientlist:
    rel = item[0].relative_water_level()
    k = item[1]
    
    try:
        if rel < 1:
            moderate.append(item[0])
            
        elif rel >= 1 and rel <= 5:
            if k < k_0:
                high.append(item[0])
            elif k >= k_0:
                severe.append(item[0])
        elif rel > 5:
            severe.append(item[0])
    except:
        pass
#print('finished classifying')
#  Definitely needs speeding up!!!
#speeding up~

print("Stations with severe risk:")
print_station_names(severe)

print("Stations with high risk:")
print_station_names(high)

print("Stations with moderate risk:")
print_station_names(moderate)

print("Stations with low risk:")
print_station_names(low)






    



   

