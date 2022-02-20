import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    #shift the dates so they are floats
    flt = matplotlib.dates.date2num(dates)
    tup = []
    #find the polynomial using the data
    p_coeff = np.polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)
    for i in range(len(poly)):
        tup.append((poly, flt))

    return tup


