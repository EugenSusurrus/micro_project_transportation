# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:21:38 2018

@author: yuy1
@format designer: eugen
"""

#import bumps
#import Delays
#import gmplot_show
import data_import
import bumps
import gmplot_show
import Delays
import app_func

def main_test(Input):
    """Unit Test Fuction"""
    if int(Input) == 1:
        gmplot_show.main()
        return 1
    if int(Input) == 2:
        bumps.main()
        return 2
    if int(Input) == 3:
        Delays.main()
        return 3
    if int(Input) == 4:

        return 4
    if int(Input) == 5:
        return 5
    if int(Input) == 6:
        time, sound = app_func.get_sound(data_import.TIME, data_import.SOUND_LEVEL)
        sound_f = app_func.filt_data(sound)
        app_func.plot_heatmap(data_import.LATITUDES, data_import.LONGITUDES,\
                              sound_f, 'gm_sound_levels.html')
        print("Wow, quite loud! Better bring some earplugs!")
        return 6
    if int(Input) == 7:
        indexes = app_func.device_out(data_import.LIGHT)
        app_func.plot_maploc(data_import.LATITUDES.iloc[indexes], data_import.LONGITUDES.iloc[indexes],\
                'gm_phone_out.html')
        print("Device taken out of the pocket at these locations.")
        return 7
    if int(Input) == 8:
        return 8
    if int(Input) == 9:
        return 9
    if int(Input) == 10:
        return 10
    return -1

while True:
    Input = input("Hi Dear User, You have already choosed the datafile and now \
which Features do you want to know?\n\n \t1.\tRoute of your journey\n \t2.\tBumps in your journey\n \
\t3.\tDelay of your journey\n \t4.\tDistance your journey covered\n \t5.\tAverage speed of your journey\n \t6.\t\
Sound Intensity Heatmap\n \t7.\tDevice taken out of the pocket\n \t8.\t\n \t9.\t\n \t10.\tYou don not want more informations\n")
    if int(Input) == 1:
        gmplot_show.main()
        continue
    if int(Input) == 2:
        bumps.main()
        continue
    if int(Input) == 3:
        Delays.main()
        continue
    if int(Input) == 4:

        continue
    if int(Input) == 5:
        continue
    if int(Input) == 6:
        time, sound = app_func.get_sound(data_import.TIME, data_import.SOUND_LEVEL)
        sound_f = app_func.filt_data(sound)
        app_func.plot_heatmap(data_import.LATITUDES, data_import.LONGITUDES,\
                              sound_f, 'gm_sound_levels.html')
        print("Wow, quite loud! Better bring some earplugs!")
        continue
    if int(Input) == 7:
        indexes = app_func.device_out(data_import.LIGHT)
        app_func.plot_maploc(data_import.LATITUDES.iloc[indexes], data_import.LONGITUDES.iloc[indexes],\
                'gm_phone_out.html')
        print("Device taken out of the pocket at these locations.")
        continue
    if int(Input) == 8:
        continue
    if int(Input) == 9:
        continue
    if int(Input) == 10:
        print("Thanks so much for using our app, Bye Bye")
        break
