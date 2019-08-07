#!/usr/bin/env python3

import os

onewire_path = "/sys/bus/w1/devices/"
temperature_directory = os.path.expanduser("~") + "/tempbot-2/log/"
sensor_names = {
    "28-0516b2fb91ff":"Ulko",
    "28-0516b2e398ff":"Serveri",
    "28-04169353faff":"Sisä",
    "28-0516b2fa75ff":"Lattia"
}
use_decimal_comma = True

