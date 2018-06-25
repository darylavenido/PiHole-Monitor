#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
# WiFi Monitoring Script Example
#
# This script uses the iwconfig.py script
# to extract the quality parameter of a known
# WiFi interface and writes that value to a test file.
#
# Please see https://www.raspberrypi-spy.co.uk/
# for more information.
#
# Author : Matt Hawkins
# Date   : 25/06/2018
#
#--------------------------------------

import time
import logging
import iwconfig as iw

interface='wlan0'

outputFile = open("iwconfig.log", "w")

try:
  while True:

    wifidata=iw.getOutput(interface)
    parameters=iw.getParameters(wifidata)
    print(interface+" : "+parameters["Link Quality"])
    outputFile.write(parameters["Link Quality"]+"\n")
    
    time.sleep(5)

except KeyboardInterrupt:
  outputFile.close() 
