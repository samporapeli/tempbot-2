#!/usr/bin/env python3

import os
import time
import temperature

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
        temperatures = temperature.Temperatures()
        temperatures.write_temps()
        clear()
        print(temperatures)
        print("Loaded", end="\r")
        
    time.sleep(0.2)
