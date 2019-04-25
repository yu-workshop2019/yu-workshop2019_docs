#!/bin/bash
#set -eu
sudo nohup python  -m SimpleHTTPServer 88 >/dev/null 2>&1 &
sudo python /home/pi/bme280/bme280.py &
sudo /home/pi/bme280/measure_temp.sh &
