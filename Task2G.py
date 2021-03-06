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
    for station in stations[:-2]:
        print(station.name, end=', ')
    print(stations[-1].name)
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

update_water_levels(exclude_low)

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


#New display options
still_loop = True
check_s, check_h, check_m, check_l = False, False, False, False
while (not check_s or not check_h or not check_m or not check_l) and still_loop:
    print("Risk level to show: ")
    x = input("Please input: severe/high/moderate/low\n")

    if x == "severe" or x == "Severe":
        if check_s:
            print("See above for severe risk.")
        else:
            print("Stations with severe risk:")
            print_station_names(severe)
            check_s = True
    elif x == "high" or x == "High":
        if check_h:
            print("See above for high risk.")
        else:
            print("Stations with high risk:")
            print_station_names(high)
            check_h = True
    elif x == "moderate" or x == "Moderate":
        if check_m:
            print("See above for moderate risk.")
        else:
            print("Stations with moderate risk:")
            print_station_names(moderate)
            check_m = True
    elif x == "low" or x == "Low":
        if check_l:
            print("See above for low risk.")
        else:
            print("Stations with low risk:")
            print_station_names(low)
            check_l = True
    else:
        print("Please enter one of the options shown above.")
    
    if not check_s or not check_h or not check_m or not check_l:
        y = input("Anything else to check? Y/N\n")
        if y == "N" or y == "n":
            still_loop = False
        elif y != "Y" and y != "y":
            raise ValueError("Wrong input.")
    else:
        print("All risk levels have been checked.")
    




    



   

