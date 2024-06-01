#!/usr/bin/python
# Enciende relay 1 "ON"

import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

def relayon():

    pinList = [3]

    for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        #i =- 1

    try:
        GPIO.output(i, GPIO.LOW)
        print ("turned on")

    except KeyboardInterrupt:
        print ("Quit")
        GPIO.cleanup()

#reon = relayon()
