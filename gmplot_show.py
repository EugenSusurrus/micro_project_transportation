# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 23:34:38 2018
show the road on Google map
@author: yuy1
"""
import os
import gmplot
import data_import

def show_googlemap(latitudes, longitudes):
    """show our travel data on google map
    """
    min_lat, max_lat, min_lon, max_lon = \
    min(latitudes), max(latitudes), \
    min(longitudes), max(longitudes)
    mymap = gmplot.GoogleMapPlotter(min_lat + (max_lat - min_lat) / 2,\
                                min_lon + (max_lon - min_lon) / 2, 10)
    mymap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=2)
    mymap.marker(latitudes[5], longitudes[5], 'cornflowerblue')

    mymap.draw("mymap.html")
    os.system('mymap.html')

def main():
     show_googlemap(data_import.LATITUDES, data_import.LONGITUDES)


if __name__ == "__main__":
    main()