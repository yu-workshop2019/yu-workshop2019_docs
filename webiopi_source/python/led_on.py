#!/usr/bin/python

import wiringpi as wp
import time

LED_PIN = 26

wp.wiringPiSetupGpio()

wp.pinMode(LED_PIN , 1)

try:
    wp.digitalWrite(LED_PIN, 1)
except:
    pass
