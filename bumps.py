# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:20:40 2018

@author: yuy1
"""
import os
import matplotlib.pyplot as plt
import numpy as np
from gmplot import gmplot
from scipy.signal import find_peaks
import data_import


RMS_LINEAR_ACC = np.sqrt((data_import.LINEAR_ACC_X)**2+(data_import.LINEAR_ACC_Y)**2+ \
                           (data_import.LINEAR_ACC_Z)**2)
"""
plt.figure(1, figsize=(15, 10))
plt.plot(data_import.TIME/1000, RMS_LINEAR_ACC, 'r', label='RMS of the linear acc')
plt.ylabel('RMS of linear ACC in m/s²', fontsize=16)
plt.xlabel('Time in s', fontsize=16)
plt.minorticks_on()
plt.grid(which='major', color='b', linestyle='-', linewidth=1)
plt.grid(which='minor', linestyle='-', linewidth=0.2, color='black')
plt.legend(fontsize=16)
PEAKS, _ = find_peaks(RMS_LINEAR_ACC, height=0)
NO_PEAKS = len(PEAKS)
"""
def show_bumps_distribution(Rms_acc, latitudes, longitudes):
    """bumps function"""
    min_lat, max_lat, min_lon, max_lon = \
    min(latitudes), max(latitudes), \
    min(longitudes), max(longitudes)
    mymap = gmplot.GoogleMapPlotter(min_lat + (max_lat - min_lat) / 2,\
                                min_lon + (max_lon - min_lon) / 2, 10)
    i = 0
    latitudes_bumps = []
    longitudes_bumps = []
    latitudes_change_trans = []
    longitudes_change_trans = []
    for i in range(len(RMS_LINEAR_ACC)):
        if RMS_LINEAR_ACC[i] > 10:
            latitudes_change_trans.append(latitudes[i])
            longitudes_change_trans.append(longitudes[i])
        elif (RMS_LINEAR_ACC[i] > 4) and (RMS_LINEAR_ACC[i] < 6):
            latitudes_bumps.append(latitudes[i])
            longitudes_bumps.append(longitudes[i])



    mymap.scatter(latitudes_bumps, longitudes_bumps, '#3B0B39', size=80, marker=False)
    mymap.scatter(latitudes_change_trans, longitudes_change_trans, '#FF1493', size=40, marker=False)
    mymap.marker(latitudes[0], longitudes[0], 'cornflowerblue')
    mymap.draw("mymap_bumps_distribution.html")
    os.system('mymap_bumps_distribution.html')

def main():
    """main"""
    show_bumps_distribution(RMS_LINEAR_ACC, data_import.LATITUDES, data_import.LONGITUDES)
    print('The Lila area means that you may have a very big bumps here or you are walking \
The pink area means that you have a small bumps here.')

if __name__ == "__main__":
    main()
