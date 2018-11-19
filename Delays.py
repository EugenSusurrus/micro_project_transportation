# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:20:53 2018

@author: yuy1
"""
import data_import

def delay_calculaion(total_time, supposed_time):
    """delay calculation"""
    delay = total_time/60000 - supposed_time
    return delay

def main():
    """main"""
    google_time = input("How long is your journey supposed to be according to the\
                      google map?(in min)")
    delay = delay_calculaion(data_import.TOTAL_TIME, float(google_time))
    if delay < 0:
        print("Your journey is faster than expected!!")
    elif 0 <= delay < 30:
        print("You have about %d min delay, but it is ok, not too much" %delay)
    else:
        print("You should complain about the delay!!")



if __name__ == "__main__":
    main()