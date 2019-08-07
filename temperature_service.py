#!/usr/bin/env python3

from temperature import Temperatures
import config
from time import time, sleep

temperatures = Temperatures()
update_seconds = config.temperature_update_seconds
last_updated = time() - update_seconds

while True:
    if time() - last_updated > update_seconds:
        last_updated = time()
        temperatures.write_temps()
    sleep(time() - last_updated)
    
