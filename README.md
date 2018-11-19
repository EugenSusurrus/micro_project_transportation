# micro_project_transportation
A brief micro-project to visualize and analyze android smartphone sensor data and  integrate it into a transportation/travel application prototype.
****************************************************************************************************************************************
[![Build Status](https://travis-ci.org/EugenSusurrus/micro_project_transportation.svg?branch=master)](https://travis-ci.org/EugenSusurrus/micro_project_transportation)
[![codecov](https://codecov.io/gh/EugenSusurrus/micro_project_transportation/branch/master/graph/badge.svg)](https://codecov.io/gh/EugenSusurrus/micro_project_transportation)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/098d25e61aa94de88b7d913fbc581251)](https://www.codacy.com/app/EugenSusurrus/micro_project_transportation?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=EugenSusurrus/micro_project_transportation&amp;utm_campaign=Badge_Grade)
****************************************************************************************************************************************
### Contributors
****************************************************************************************************************************************
Contributor                                                      |  Functionality 
---------------------------------------------------------------: | :-----------------
Eugen R. [(@EugenSusurrus)](https://github.com/EugenSusurrus)    |  device_out
Eugen R. [(@EugenSusurrus)](https://github.com/EugenSusurrus)    |  noise_level
Rony B.  [(@BalayetRony)](https://github.com/BalayetRony)        |  distance
Rony B.  [(@BalayetRony)](https://github.com/BalayetRony)        |  avg_speed
Fahad S. [(@fahadsha)](https://github.com/fahadsha)              |  no_of_stops
Fahad S. [(@fahadsha)](https://github.com/fahadsha)              |  kind_of_transport            |  
Yu Y.    [(@)yuy1-kpit](https://github.com/yuy1-kpit)            |  traffic_delay
Yu Y.    [(@)yuy1-kpit](https://github.com/yuy1-kpit)            |  Route of the Journey
Yu Y.    [(@)yuy1-kpit](https://github.com/yuy1-kpit)            |  bumps

### Brief Description
****************************************************************************************************************************************
The sensor data was acquired via an Android smartphone while traveling on multiple means of transportation. The device was held as stable as possible in order to reduce noise and undesired signals. The data was then exported to a *.csv* format and the table header fields were filtered to remove the uninterpretable symbols and shorten the header names for easier 
acquisition.  All the datafile come from Fahad S.[(@fahadsha)](https://github.com/fahadsha). He travels everyday from Rosenheim to Munich(KPIT Office Location). The transport means he used include Bus, Train, S-Bahn, Walking. One datafile (Dest_kpit_rosenheim.csv) is used for analysing and the otherone (Dest_rosenheim_kpit_Testdata.csv) is used for testing. 
The *.csv* data contains the next fields:

* Acceleration along axes:           *ACC X (m/s2)|	ACC Y (m/s2)|	ACC Z (m/s2)*
* Gravity along axes:                *GRAV X (m/s2)|	GRAV Y (m/s2)|	GRAV Z (m/s2)*
* Linear acceleration along axes:    *LIN ACC X (m/s2)|	LIN ACC Y (m/s2)|	LIN ACC Z (m/s2)*
* Gyroscope around axes:             *GYRO X (rad/s)|	GYRO Y (rad/s)|	GYRO Z (rad/s)*
* Light intensity:                   *LIGHT (lux)*
* Magnetic field along axes:         *MAG FIELD X (T)| MAG FIELD Y (T)|	MAG FIELD Z (T)*
* Orientation along axes:            *ORIENT Z (deg)|	ORIENT X (deg)|	ORIENT Y (deg)*
* Proximity sensor:                  *PROXIMITY (m)*
* Sound level:                       *SOUND LEVEL (dB)*
* Location latitude and longitude:   *LOC LAT| LOC LON*	
* Altitude:                          *LOC ALT (m)*
* Speed:                             *LOC SPEED (Km/h)*	
* Location accuracy:                 *LOC ACCURACY (m)*
* Location orieintation:             *LOC ORIENT (deg)*
* Satelites in range:                *SAT IN RANGE*
* Time in ms:                        *TIME (ms)*
* Date format:                       *YYYY-MO-DD HH-MI-SS_SSS*

### Function description
****************************************************************************************************************************************
```python
def get_sound(time_df, levels_df)
```
>Takes as input the time dataframe <time_df> and soundlevels dataframe <levels_df> and returns the adjusted time in seconds <time> and the sound levels accordingly <sound_level>
****************************************************************************************************************************************
```python
def filt_data(levels_in):
```
>Takes as input the unfiltered data levels <levels_in> and returns a second degree filtered array of the input data <filt_data_2>
****************************************************************************************************************************************
```python
def plot_heatmap(lat_in, lon_in, values, filename):
```
>Plots an interactive heatmap with the values specified in the <values> dataframe at the latitudes and longitudes specified in the <lat_in> and <lon_in> accordingly. Saves the file with the specified <filename> Returns 0 at exit with success
  
*sample image:*
![alt text](https://raw.githubusercontent.com/EugenSusurrus/micro_project_transportation/master/sample_images/Heatmap.PNG "Heatmap")
***************************************************************************************************************************************
```python
def plot_maploc(lat_in, lon_in, filename):
```
>Plots markers located at latitudes <lat_in> dataframe and longitudes <lon_in> dataframe on a map.Suitable for marker plotting for a relatively low ammount of data. Saves the map with the specified <filename> filename and returns 0 on successful exit.
  
*sample image:*
![alt text](https://raw.githubusercontent.com/EugenSusurrus/micro_project_transportation/master/sample_images/Location%20on%20Map.PNG "Location on map")

***************************************************************************************************************************************
```python
def data_import:
```
>import all the data varibales. There are two choices of data file to import. Data1 is Dest_kpit_rosenheim.csv as analysis data. Data2 is Dest_rosenheim_kpit_Testdata.csv as testing data.
  
***************************************************************************************************************************************
```python
def bumps:
```
>Analysis All the Bumps the user experienced during travelling. The Lila area means that you may have a very big bumps here or you are walking. The pink area means that you have a small bumps here.

*sample image:*
![alt text](https://raw.githubusercontent.com/EugenSusurrus/micro_project_transportation/master/sample_images/Bumps.PNG "Bumps")
  
***************************************************************************************************************************************
```python
def gmplot_show:
```
>Show the travelling route of the user on the google map.
  
*sample image:*
![alt text](https://github.com/EugenSusurrus/micro_project_transportation/blob/master/sample_images/Route.PNG "Routes")
***************************************************************************************************************************************
```python
def Delays:
```
>calculate the difference between the expected travelling time (according to the google map) and the actually travelling time.
***************************************************************************************************************************************
```python
def no_stops_function:
```
>calculate the totally stops in your journey. It includes all means of tranportation.
***************************************************************************************************************************************
```python
def means_of_transport:
```
>What kinds of transport you have utilized in the whole journey

