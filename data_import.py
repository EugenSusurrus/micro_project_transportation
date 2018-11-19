# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:33:48 2018

@author: yuy1
"""
import pandas as pd
#DATAFILE_NAME = input("Which travel data you want us to analysis? \
#please type the Excel file name:  ")
#print(DATAFILE_NAME)
DATAFILE_NAME_1 = 'Dest_kpit_rosenheim.csv'
DATAFILE_NAME_2 = 'Dest_rosenheim_kpit_Testdata.csv'
INPUT = input('Which Datafile do you want?(Data1 or Data2)')
if INPUT == 'Data1':
    DATAFILE_NAME = DATAFILE_NAME_1
    print('You have choosed %s' %DATAFILE_NAME_1)
elif INPUT == 'Data2':
    DATAFILE_NAME = DATAFILE_NAME_2
    print('You have choosed %s' %DATAFILE_NAME_2)
else:
    print('Sorry, we have only two datafiles, please choose Data1 or Data2')

DF = pd.read_csv(DATAFILE_NAME)
TIME = DF['Time since start in ms ']
TOTAL_TIME = TIME[len(TIME)-1] - TIME[0]
print('total recording time is : %f min' %(TOTAL_TIME/60000))
#acceloration
ACC_X = DF['ACCELEROMETER X (m/s²)']
ACC_Y = DF['ACCELEROMETER Y (m/s²)']
ACC_Z = DF['ACCELEROMETER Z (m/s²)']
#gravity
GRAV_X = DF['GRAVITY X (m/s²)']
GRAV_Y = DF['GRAVITY Y (m/s²)']
GRAV_Z = DF['GRAVITY Z (m/s²)']
#MAGNETIC FIELD X (Î¼T)
MAG_X = DF['MAGNETIC FIELD X (μT)']
MAG_Y = DF['MAGNETIC FIELD Y (μT)']
MAG_Z = DF['MAGNETIC FIELD Z (μT)']
#linear acc
LINEAR_ACC_X = DF['LINEAR ACCELERATION X (m/s²)']
LINEAR_ACC_Y = DF['LINEAR ACCELERATION Y (m/s²)']
LINEAR_ACC_Z = DF['LINEAR ACCELERATION Z (m/s²)']
#GYROSCOPE (rad/s)
GYRO_X = DF['GYROSCOPE X (rad/s)']
GYRO_Y = DF['GYROSCOPE Y (rad/s)']
GYRO_Z = DF['GYROSCOPE Z (rad/s)']
#LOCATION
LATITUDES = DF['LOCATION Latitude : ']
LONGITUDES = DF['LOCATION Longitude : ']
ALTITUDE = DF['LOCATION Altitude ( m)']
Aver_Loca_accuracy = DF['LOCATION Accuracy ( m)'].mean()
#light
LIGHT = DF['LIGHT (lux)']
#Sound
SOUND_LEVEL = DF['SOUND LEVEL (dB)']
#speed
LOCATION_SPEED = DF['LOCATION Speed ( Kmh)']
