# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:21:04 2018

@author: mdb99
"""

from math import radians, cos, sin, asin, sqrt
import data_import

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    A = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    C = 2 * asin(sqrt(A))
    R = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return C * R

def distance_calculation(latitude,longitude):
    DISTANCES = []
    count = 0
    while True:
        if count < len(latitude)-1:
            DISTANCES.append(haversine(longitude[count], latitude[count], longitude[count+1],\
                                       latitude[count+1]))
            count = count + 1
        else:
            break
    return sum(DISTANCES)

def main():
    LATITUDE = data_import.LATITUDES
    LONGITUDE = data_import.LONGITUDES
    Route_distance = distance_calculation(LATITUDE,LONGITUDE)
    print("The total distance of your journey is %d km" %Route_distance)
    
if __name__ == "__main__":
    main()
