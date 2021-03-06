# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        
        #check if data is available, if not, return false
        if self.typical_range == None:
            return False
        else:
            #take h1 to be typical low, h2 to be typical high
            h_1, h_2 = self.typical_range[0], self.typical_range[1]
            if h_1 > h_2:
                return False
            else:
                return True

    def relative_water_level(self):
        #A variable to store relative water level, None if inconsistent
        x = 0
        if (not self.typical_range_consistent()) or (self.latest_level == None):
            x = None
        else:
            x = (self.latest_level - self.typical_range[0])/(self.typical_range[1] - self.typical_range[0])
        return x
        



def inconsistent_typical_range_stations(stations):
    x = []
    for station in stations: 
        if not station.typical_range_consistent():
            x.append(station)
        elif station.typical_range_consistent():
            pass
        # print(MonitoringStation.typical_range_consistent)
    return x

        