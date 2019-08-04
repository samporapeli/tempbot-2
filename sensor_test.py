#!/usr/bin/env python3

import os
import time
import sensors
import config

update_seconds = 5
last_updated = time.time() - update_seconds

def clear():
    os.system("clear")

clear()

while True:
    # If enough time has passed
    if time.time() - last_updated > update_seconds:
        print("Loading new data...", end="\r")
        last_updated = time.time()
        current_sensors = sensors.sensor_list()
        output = []
        for sensor in current_sensors:
            sensor_name = config.sensor_names.get(sensor, 
                "Sensor " + str(current_sensors.index(sensor) + 1))
            output.append(sensor_name + ": " + sensors.pretty_temp(sensor))
        clear()
        for out in output:
            print(out)
        print("Loaded", end="\r")
        
    time.sleep(0.2)
