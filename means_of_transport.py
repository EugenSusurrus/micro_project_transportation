# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:15:26 2018

@author: fahads99
"""

import data_import
#import pandas as pd
#from scipy import integrate
#from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def means_transport():
 
    ACC_X = data_import.LINEAR_ACC_X
    ACC_Y = data_import.LINEAR_ACC_Y
    ACC_Z = data_import.LINEAR_ACC_Z
    RMS_ACC = np.sqrt((ACC_X)**2+(ACC_Y)**2+(ACC_Z)**2)
    plt.figure(figsize=(11,10))
    plt.plot(data_import.TIME/1000, RMS_ACC)
    Subway_threshold_low = 2.2
    Subway_threshold_up = 3.1
    train_threshold_low = 1.1
    train_threshold_up = 3.0
    tram_threshold_low = 2.1
    tram_threshold_up = 2.9
    Subway_no = 0
    train_no = 0
    tram_no = 0
    for i in range(len(RMS_ACC)):
        if Subway_threshold_low <RMS_ACC[i] < Subway_threshold_up:
            Subway_no = Subway_no+1
        if train_threshold_low <RMS_ACC[i] < train_threshold_up:
            train_no = train_no+1
        if tram_threshold_low <RMS_ACC[i] < tram_threshold_up:
            tram_no = tram_no+1
     
    if Subway_no > 50:
       print("There are Subway in your journey")
    if train_no > 100:
       print("There are train in your journey")
    if tram_no > 50:
       print("There are tram in your journey")
    
def main():
     means_transport()


if __name__ == "__main__":
    main()    