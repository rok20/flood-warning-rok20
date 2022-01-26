# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa

from haversine import haversine, Unit

# Install haversine if not already: "pip install haversine"

# A function that, given a list of stations and a coordinate will return a list of (station, distance) tuples, sorted by distance.
def stations_by_distance(stations, p):
    #need to isolate coordinates and name from each? Not sure bout this part


    names = len(stations)*[None]
    coords = len(stations)*[None]
    place = len(stations)*[None]

    for i in range(len(stations)):

        names[i] = stations[i].name
        coords[i] = stations[i].coord
        place[i] = stations[i].town


    list = len(stations)*[None]
    distance = len(stations)*[None]
    # Go through each entry and find the distance and make a list of tuples including the station and the distance.
    for i in range(len(stations)):
        distance[i] = haversine(coords[i], p)
        list[i] = (names[i], place[i], distance[i])

    # Sort the list in order of distance largest to smallest and return the result
    sortedbydistance = sorted_by_key(list, 2)
    return sortedbydistance

