
from .analysis import polyfit
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def plot_water_levels(station, dates, levels):
    #plot the dates and water levels
    plt.plot(dates, levels, label = 'Water level')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station " + station.name)

    #add typical high and low
    low, high = station.typical_range[0], station.typical_range[1]
    plt.axhline(y = low, color = 'b', label = 'Typical low')
    plt.axhline(y = high, color = 'r', label = 'Typical High')


    # Display plot
    plt.tight_layout()  
    # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    list = polyfit(dates, levels, p)
    
    dates2 = matplotlib.dates.date2num(dates) 

    #adjust dates so values aren't so high
    dates2 = dates2 - dates2[0]
    
    #provide points at set intervals for the polynomial
    points  = np.linspace(dates2[0], dates2[-1], 30)
    
    #plot data in hours for each curve, label the axis and provide a title.
    plt.plot(24*dates2, levels, label = "Actual data")
    plt.plot(24*points, list[0](points), label = "Best fit polynomial")
    plt.xlabel("Hours in the past")
    plt.ylabel("Water Level")
    plt.title(station)
    

    plt.show


