#!/usr/bin/python

import wiringpi as wp
import time

LED_PIN = 26
INTERVAL = 0.5

wp.wiringPiSetupGpio()

wp.pinMode(LED_PIN , 1)

try:
    while True:
        wp.digitalWrite(LED_PIN, 1)
        time.sleep(INTERVAL)
        wp.digitalWrite(LED_PIN, 0)
        time.sleep(INTERVAL)

except:
    wp.digitalWrite(LED_PIN, 0)
