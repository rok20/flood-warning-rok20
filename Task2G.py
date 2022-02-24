#Initial ideas::: Consider gradiwnt of line in polyfit? Consider how high above the typical high (relative height?), 
#Severe rising and a lot above the top band
#High rising and above the top band/ 
#Moderate rising and between the two bands/ decreasing but above the highest
#Low not rising and not above usual heighest
#wants speeding up


#write a function to determine gradient of line? Since the polyfit is set so 0 is present, the x coefficient is the gradient at present day
import string
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import floodsystem.datafetcher


stations = build_station_list()
listforgrad = []
dt = 1
def gradient(dates, levels):
    
    list = polyfit(dates, levels, 4)
    return list
    
gradientlist = []
for station in stations:
    #print(type(station.measure_id))
    if type(station.measure_id) == str:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        
        try:
            polynomial = gradient(dates, levels)
            
            #make a list of tuples with station name, the gradient and the current level and typical range: LATEST LEVEL isnt working 
            gradientlist.append([station.name, polynomial[0][1], levels[0], station.typical_range])
            
        except:
            pass

# Four categories and then look at initial conditions to sort into 4 groups ?
severe = []
high = []
moderate = []
low = []
print(gradientlist)
for item in gradientlist:
    try:
        if item[1] > 0 and item[2] > 5* item[3][1]:
            severe.append(item[0])
        elif item[1] > 0 and item[2] < 5* item[3][1] and item[2] > item[3][1] or item[1] <0 and item[2] > 5* item[3][1]:
            high.append(item[0])
        elif item[1] < 0 and item[2] < 3* item[3][1] and item[2] > item[3][1] or item[1] > 0 and item[2] > item[3][0] and item[2] < item[3][1]:
            moderate.append(item[0])
        elif item[1] < 0 and item[2] > item[3][0] and item[2] < item[3][1] or item[1] > 0 and item[2] < item[3][0]:
            low.append(item[0])
    except:
        pass

#  Definitely needs speeding up!!!

print("Stations with severe risk:")
print(severe)

print("Stations with high risk:")
print(high)

print("Stations with moderate risk:")
print(moderate)

print("Stations with low risk:")
print(low)




    



   

