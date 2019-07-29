#!/bin/bash

TEMPBOT=~/tempbot-2

python3 $TEMPBOT/temperature.py $TEMPBOT &
python3 $TEMPBOT/bot.py $TEMPBOT &
