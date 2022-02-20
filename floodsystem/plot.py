from .analysis import polyfit
import numpy as np
import matplotlib.pyplot as plt

def plot_water_level_with_fit(station, dates, levels, p):
    list = polyfit(dates, levels, p)
    x = dates
    y = levels

    plt.plot(dates, levels)

    plt.plot(list[1], list[0])

    plt.show


