#!/usr/bin/env python3

import time
import bot
from temperature import Temperatures

tg = bot.TelegramBot()
temperatures = Temperatures()

while True:
    message = tg.next_message()
    if (message):
        tg.reply(message, temperatures)
    time.sleep(0.1)
