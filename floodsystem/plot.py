from .analysis import polyfit
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def plot_water_level_with_fit(station, dates, levels, p):
    list = polyfit(dates, levels, p)
    
    dates2 = matplotlib.dates.date2num(dates) 
    
    dates2 = dates2 - dates2[0]
    
    points  = np.linspace(dates2[0], dates2[-1], 30)
    
    plt.plot(dates2, levels)
    plt.plot(points, list[0](points))
    plt.xlabel("Dates")
    plt.ylabel("Water Level")
    plt.title(station)

    return plt.show


