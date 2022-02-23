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
        
            gradientlist.append([station.name, polynomial[0][1]])
            
        except:
            pass
#consider rising/falling significantly, say 0.5 for now?
greaterthanhalf = []
lessthanhalf = []
betweenthetwo = []
for item in gradientlist:
    if item[1] > 0.5:
        greaterthanhalf.append(item)
    elif item[1] < 0.5:
        lessthanhalf.append(item)
    else:
        betweenthetwo.append(item)

#Printing to show it works, this data is suitably sorted now for the purpose :) 
# now need to look at speeding it up, and the current levels to then sort into four categories.
#  Definitely needs speeding up!!!

print(greaterthanhalf)
print(lessthanhalf)
print(betweenthetwo)
    



   

