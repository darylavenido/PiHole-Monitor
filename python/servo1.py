#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#           servo1.py
#  Basic example script to control a servo
#  connected to GPIO17 using the Gpiozero library.
#
# Use CTRL-C to break out of While loop.
#
# Author : Matt Hawkins
# Date   : 19/12/2017
#
# http://www.raspberrypi-spy.co.uk/tag/dht11/
#
#--------------------------------------
from gpiozero import Servo
from time import sleep

myGPIO=17

servo = Servo(myGPIO)

while True:
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.min()
    print("min")
    sleep(1)
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.max()
    print("max")
    sleep(1)