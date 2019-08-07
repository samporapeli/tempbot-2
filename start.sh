#!/bin/bash

TEMPBOT=~/tempbot-2/

source $TEMPBOT/venv/bin/activate
python3 $TEMPBOT/tempbot_2.py $TEMPBOT &
python3 $TEMPBOT/temperature_service.py $TEMPBOT
