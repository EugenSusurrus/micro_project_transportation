# micro_project_transportation
A brief micro-project to visualize and analyze android smartphone sensor data and  integrate it into a transportation/travel application prototype.
### Contributors
****************************************************************************************************************************************
Contributor                                                      |  Functionality 
---------------------------------------------------------------: | :-----------------
Eugen R. [(@EugenSusurrus)](https://github.com/EugenSusurrus)    |  device_out
Eugen R. [(@EugenSusurrus)](https://github.com/EugenSusurrus)    |  noise_level
Rony B.  [(@BalayetRony)](https://github.com/BalayetRony)        |  distance
Rony B.  [(@BalayetRony)](https://github.com/BalayetRony)        |  avg_speed
Fahad S. [(@fahadsha)](https://github.com/fahadsha)              |  no_of_stops
Fahad S. [(@fahadsha)](https://github.com/fahadsha)              |  kind_of_transport
Yu Y.    [(@)yuy1-kpit](https://github.com/yuy1-kpit)            |  traffic_jam
Yu Y.    [(@)yuy1-kpit](https://github.com/yuy1-kpit)            |  bumps

### Brief Description
****************************************************************************************************************************************
The sensor data was acquired via an Android smartphone while traveling on multiple means of transportation. The device was held as stable as possible in order to reduce noise and undesired signals. The data was then exported to a *.csv* format and the table header fields were filtered to remove the uninterpretable symbols and shorten the header names for easier 
acquisition. The *.csv* data contains the next fields:

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
get_sound(time_df, levels_df)
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
