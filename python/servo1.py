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
# Date   : 01/01/2018
#
# https://www.raspberrypi-spy.co.uk/tag/servo/
#
#--------------------------------------
from gpiozero import Servo
from time import sleep

myGPIO=17

servo = Servo(myGPIO)

print("Using GPIO17")
print("Using Gpiozero defaults for the servo class")

while True:
  servo.mid()
  print("Set to middle position")
  sleep(1)
  servo.min()
  print("Set to minimum position")
  sleep(1)
  servo.mid()
  print("Set to middle position")
  sleep(1)
  servo.max()
  print("Set to maximum position")
  sleep(1)