#!/usr/bin/env python3

import os
import config

def sensor_list():
    sensors = os.listdir(config.onewire_path)
    sensors.remove("w1_bus_master1")
    return sensors

def sensor_temp(sensor):
    try:
        file_path = "{path}{sensor}/w1_slave".format(
            path = config.onewire_path, sensor = sensor)
        with open(file_path) as sensor_file:
            data = sensor_file.readlines()
    except:
        return "Error with accessing sensor data"
    try:
        # The temperature information is on the second line
        # after "t="
        second_line_elements = data[1].split(" ")
        t = list(filter(lambda x: "t=" in x, second_line_elements))
        # First element starting with "t=" is the right one
        # (there should only be one)
        millicelcius = float(t[0].split("=")[1])
        return millicelcius / 1000
    except:
        return "Error with parsing temperature data"

def pretty_temp(sensor):
    raw = sensor_temp(sensor)
    rounded = str(round(raw, 1))
    if (config.use_decimal_comma):
        rounded = rounded.replace(".", ",")
    return rounded + "°C"
