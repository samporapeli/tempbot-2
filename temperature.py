#!/usr/bin/env python3

import time
import sensors
import config

dir = config.temperature_directory

def read_file_temp(sensor_id):
    temp_location = dir + sensor_id + ".csv" 
    try:
        with open(temp_location, "r") as temp_file:
            data = temp_file.readlines()
        write_time = float(data[1].split(";")[0])
        write_temp = float(data[1].split(";")[1])
        if write_time < time.time() - (60 * 60):
           return "Temperature data older than an hour"
        else:
         return write_temp
    except:
        return "Could not open file " + temp_location 

def write_file_temp(temperature):
    line1 = "unix_time;temperature\n"
    line2 = "{write_time};{write_temp}\n".format(
        write_time = time.time(), 
        write_temp = temperature.sensor_temp())
    with open(dir + temperature.sensor_id + ".csv", "w+") as temp_file:
        temp_file.writelines([line1, line2])

class Temperature:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    def name(self):
        return config.sensor_names.get(self.sensor_id, self.sensor_id)
    def read_temp(self):
        return read_file_temp(self.sensor_id)
    def write_temp(self):
        write_file_temp(self)
    def sensor_temp(self):
        return sensors.sensor_temp(self.sensor_id)
    def to_string(self):
        return self.name() + ": " + str(self.read_temp())

class Temperatures:
    def __init__(self):
        self.temps = []
        self.update_temps()
    def update_temps(self):
        self.temps = list(map(lambda temp: Temperature(temp), sensors.sensor_list()))
    def list_temps(self):
        return list(map(lambda temp: temp.read_temp(), self.temps))
    def list_sensors(self):
        return list(map(lambda temp: temp.sensor_id, self.temps))
    def write_temps(self):
        return list(map(lambda temp: temp.write_temp(), self.temps))
    def to_string(self):
        return "\n".join(list(map(lambda temp: temp.to_string(), self.temps)))
