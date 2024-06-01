#!/usr/bin/python
# Apaga relay 1 "OFF"

import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
def relayoff():
    pinList = [3]

    for h in pinList:
        GPIO.setup(h, GPIO.OUT)
        #h =- 1

    try:
        GPIO.output(h, GPIO.HIGH)
        print ("turned off")

    except KeyboardInterrupt:
        print ("Quit")
        GPIO.cleanup()

#reof = relayoff()
