# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 09:51:49 2018

@author: fahads99
"""
import data_import
#import pandas as pd
#from scipy import integrate
#from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def no_of_stops():
    """
    The purpose of function is to obtain & calculate no. of stops during journey
    """
    ACC_X = data_import.LINEAR_ACC_X
    ACC_Y = data_import.LINEAR_ACC_Y
    ACC_Z = data_import.LINEAR_ACC_Z
    RMS_ACC = np.sqrt((ACC_X)**2+(ACC_Y)**2+(ACC_Z)**2)
    stop_threshold_low = 2
    stop_threshold_up = 2.1
    no_stop = 0
    for i in range(len(RMS_ACC)):
        if stop_threshold_low < RMS_ACC[i] < stop_threshold_up:
            no_stop = no_stop+1    
    print("There are total %d stops in your journey" %no_stop)
def main():
    """used to obtain the values tabulated in no.of stops function"""
    no_of_stops()


if __name__ == "__main__":
    main()
    