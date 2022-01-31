# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa
#somehow I had to change .utils to utils to make it work

from haversine import haversine, Unit

# Install haversine if not already: "pip install haversine"

# A function that, given a list of stations and a coordinate will return a list of (station, distance) tuples, sorted by distance.

def stations_by_distance(stations, p):
    #Create an empty list for each variable and iterate over to fill with data

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


# This function, given a radius r and coordinate x, will return a list containing all stations withing the radius of x

def stations_within_radius(stations, centre, r):
    #create an empty list
    stations_within = []
    for station in stations:
        #if a station is within radius, then append it to the list
        if haversine(station.coord, centre) < r:
            stations_within.append(station)
    return stations_within

# A function that, given a list of stations, will return a container with the names of the rivers with a monitoring station

def river_with_station(stations):
   # Create an empty dictionary
  dictionary = {}
  # iterate through the rivers, if it is already in the dictionary, add the new river onto the end and if not create a new slot in the dictionary for the new river. 
  # This currently has duplicates!!!!
  for station in stations:
    if station.river in dictionary:        
        dictionary[station.river] += [station.name]   
    elif station.river not in dictionary:
      dictionary[station.river] = [station.name]
  for station.river in dictionary:
      
      dictionary[station.river] = set(dictionary[station.river])
      dictionary[station.river] = sorted(dictionary[station.river])
      
  return dictionary