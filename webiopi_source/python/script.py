#!/usr/bin/python
#coding:utf-8

#@以下の部分(デコレータ)で定義された値を受け取り、
#対応するC言語のプログラムを外部起動する

import webiopi		#GPIOやWebインタフェイス
import os		#Pythonから外部プログラムを起動するsystem()関数
import time		#sleep()関数

#LIGHT_STATUS = 0
#LIGHT_STATUS_PAST = 0


@webiopi.macro
def sendCommand(command):
	os.system("sudo sh " + command)
	return "OK"

@webiopi.macro
def PythonGPIO(command):
	#os.system('sudo /home/pi/rasp_remote/light_on.out')
	os.system("sudo python /home/pi/webiopi_source/" + command)
	#time.sleep(1)	#1秒待つ
	return "OK"

@webiopi.macro
def resetServo():
	os.system("sudo python /home/pi/webiopi_source/servo_set_zero.py")
	#time.sleep(1)	#1秒待つ
	return "OK"
