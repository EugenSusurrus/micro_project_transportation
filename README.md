# micro_project_transportation
========================================================================================================================================
A brief micro-project to visualize and analyze android smartphone sensor data and  integrate it into a transportation/travel application prototype.
========================================================================================================================================
CONTRIBUTOR:                 |       FUNCTIONALITY:
-----------------------------------------------------
Eugen R. (@EugenSusurrus)    |       device_out
                             |       noise_level
Rony B.  (@BalayetRony)      |       distance
                             |       avg_speed
Fahad S. (@fahadsha)         |       no_of_stops
                             |       kind_of_transport
Yu Y.    (@)                 |       traffic_jam
                             |       bumps
****************************************************************************************************************************************
# Data acquisition description
****************************************************************************************************************************************
The sensor data was acquired via an Android smartphone while traveling on multiple means of transportation. The device was held as stable as possible in order to reduce noise and undesired signals. The data was then exported to a *.csv* format and the table header fields were filtered to remove the uninterpretable symbols and shorten the header names for easier 
acquisition. The *.csv* data contains the next fields:

>Acceleration along axes:           ACC X (m/s2)|	ACC Y (m/s2)|	ACC Z (m/s2)
-----------------------------------------------------------------------------------------
>Gravity along axes:                GRAV X (m/s2)|	GRAV Y (m/s2)|	GRAV Z (m/s2)
-----------------------------------------------------------------------------------------
>Linear acceleration along axes:    LIN ACC X (m/s2)|	LIN ACC Y (m/s2)|	LIN ACC Z (m/s2)
-----------------------------------------------------------------------------------------
>Gyroscope around axes:             GYRO X (rad/s)|	GYRO Y (rad/s)|	GYRO Z (rad/s)
-----------------------------------------------------------------------------------------
>Light intensity:                   LIGHT (lux)
-----------------------------------------------------------------------------------------
>Magnetic field along axes:         MAG FIELD X (T)| MAG FIELD Y (T)|	MAG FIELD Z (T)
-----------------------------------------------------------------------------------------
>Orientation along axes:            ORIENT Z (deg)|	ORIENT X (deg)|	ORIENT Y (deg)
-----------------------------------------------------------------------------------------
>Proximity sensor:                  PROXIMITY (m)
-----------------------------------------------------------------------------------------
>Sound level:                       SOUND LEVEL (dB)
-----------------------------------------------------------------------------------------
>Location latitude and longitude:   LOC LAT| LOC LON	
-----------------------------------------------------------------------------------------
>Altitude:                          LOC ALT (m)
-----------------------------------------------------------------------------------------
>Speed:                             LOC SPEED (Km/h)	
-----------------------------------------------------------------------------------------
>Location accuracy:                 LOC ACCURACY (m)
-----------------------------------------------------------------------------------------
>Location orieintation:             LOC ORIENT (deg)
-----------------------------------------------------------------------------------------
>Satelites in range:                SAT IN RANGE
-----------------------------------------------------------------------------------------
>Time in ms:                        TIME (ms)
-----------------------------------------------------------------------------------------
>Date format:                       YYYY-MO-DD HH-MI-SS_SSS
-----------------------------------------------------------------------------------------
****************************************************************************************************************************************
# Function description
****************************************************************************************************************************************

