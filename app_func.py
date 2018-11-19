# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 22:13:27 2018

@author: eugenr

app_func
===============================================
Contains the basic transportation app functions:
* get_sound
* filt_data
* plot_heatmap
* device_out
* plot_maploc
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import folium
from folium.plugins import HeatMap
import data_import



def get_sound(time_df, levels_df):
    """Takes as input the time dataframe <time_df> and soundlevels dataframe
    <levels_df> and returns the adjusted time in seconds <time> and the
    sound levels accordingly <sound_level>"""
    time = round((time_df - time_df.iloc[0]) / 1000)
    time = time.tolist()
    sound_level = levels_df.tolist()
    return time, sound_level



def filt_data(levels_in):
    """Takes as input the unfiltered data levels <levels_in> and
    returns a second degree filtered array of the input data <filt_data_2>"""
    # Sets the filter window as 10% of the entire dataframe
    filt_window = round(0.1 * len(levels_in))
    # Filtter window has to be odd. Makes sure the filter window is odd
    if filt_window % 2 == 0:
        filt_window += 1
    # 1st degree filter
    filt_data_1 = savgol_filter(levels_in, filt_window, 2)
    # 2nd degree filter
    filt_data_2 = savgol_filter(filt_data_1, filt_window, 2)
    return filt_data_2



def plot_heatmap(lat_in, lon_in, values, filename):
    """Plots an interactive heatmap with the values specified in the <values>
    dataframe at the latitudes and longitudes specified in the <lat_in> and <lon_in>
    accordingly. Saves the file with the specified <filename> Returns 0 at exit with success"""
    normed = (values - min(values)) / (max(values)-min(values))
    heat_map = folium.Map(location=[np.mean(lat_in), np.mean(lon_in)],\
                                    zoom_start=16, tiles="Stamen Toner")

    hm_data = HeatMap(list(zip(lat_in.values, lon_in.values, normed)),\
                      min_opacity=0.15,\
                      max_val=max(values),\
                      radius=20,\
                      blur=15,\
                      max_zoom=1)

    heat_map.add_child(hm_data)
    heat_map.save(filename)
    os.system(filename)
    return 0



def plot_maploc(lat_in, lon_in, filename):
    """Plots markers located at latitudes <lat_in> dataframe and longitudes
    <lon_in> dataframe on a map.Suitable for marker plotting for a relatively low ammount of data.
    Saves the map with the specified <filename> filename and returns 0 on successful exit."""
    map_loc = folium.Map(location=[np.mean(lat_in), np.mean(lon_in)],\
                                   zoom_start=16, tiles="Stamen Toner")
    for lat, lon in zip(lat_in, lon_in):
        folium.Marker([lat, lon]).add_to(map_loc)
    map_loc.save(filename)
    os.system(filename)
    return 0



def device_out(light_val):
    """Returns the indexes of the dataframe of when the device has been taken out of the
    pocket based on the light intensity values."""
    return light_val[light_val > 0].index.values



def main():
    """An example of hoiw the above functionality works."""
    # Getting the sound and time values from the imported dataset
    time, sound = get_sound(data_import.TIME, data_import.SOUND_LEVEL)
    # Getting the filtered sound levels
    sound_f = filt_data(sound)

    # Plotting the filtered sound levels against the raw sound levels
    plt.figure(figsize=(16, 8))
    plt.plot(time, sound)
    plt.plot(time, sound_f)
    plt.grid()
    plt.title('Raw sound levels vs filtered sound levels')
    plt.legend(['Raw Sound', 'Filtered Sound'])
    plt.xlabel('Time [s]')
    plt.ylabel('Sound intensity [dB]')

    # Ploting the sound levels heatmap
    plot_heatmap(data_import.LATITUDES, data_import.LONGITUDES, sound_f, 'gm_sound_levels.html')

    # Getting the indexes of the locations where the phone was taken out of the pocket
    indexes = device_out(data_import.LIGHT)

    # Plots the locations where the phone was taken out of the pocket
    plot_maploc(data_import.LATITUDES.iloc[indexes], data_import.LONGITUDES.iloc[indexes],\
                'gm_phone_out.html')

if __name__ == "__main__":
    main()
