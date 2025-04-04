#!/usr/bin/python3
from gpiozero import Button
from signal import pause
import os
import time
import logging

# Setup logging
logging.basicConfig(
    filename='/home/stanfield/power_button.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

try:
    button = Button(3)  # GPIO3 (Pin 5)
    press_time = None

    def on_press():
        global press_time
        press_time = time.time()
        logging.info("Button pressed")

    def on_release():
        duration = time.time() - press_time
        if duration >= 2:
            logging.info("Long press: Shutting down")
            os.system("sudo shutdown -h now")
        else:
            logging.info("Short press: Rebooting")
            os.system("sudo reboot")

    button.when_pressed = on_press
    button.when_released = on_release

    logging.info("Power button script started")
    pause()

except Exception as e:
    logging.exception("Script crashed with exception")
