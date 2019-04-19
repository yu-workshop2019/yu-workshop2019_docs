#!/bin/bash
#coding: utf-8
#measure CPU-temp
while true
do
	cat /sys/class/thermal/thermal_zone0/temp > /home/pi/webiopi_source/bme280/cpu_temp.txt
	sleep 1s
done
