# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:39:31 2018

@author: mdb99
"""

import data_import
import Distance

def average_speed(all_distance, all_time):
    Average_Speed = all_distance/all_time
    return Average_Speed
    

def main():
    LATITUDE = data_import.LATITUDES
    LONGITUDE = data_import.LONGITUDES
    All_Distance = Distance.distance_calculation(LATITUDE,LONGITUDE)
    #print(All_Distance)
    averagespeed = average_speed (All_Distance, data_import.TOTAL_TIME/60000)
    #print(averagespeed)
    
    print ("The average speed of your journey is %f km/h" %(averagespeed*60))
    

if __name__ == "__main__":
    main()
    
    
