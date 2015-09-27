#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#  
#       Hall Effect Sensor
#
# This script tests the sensor on GPIO17.
#
# Author : Matt Hawkins
# Date   : 27/09/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#-------------------------------------- 

# Import required libraries
import RPi.GPIO as GPIO
import time
import datetime

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

print "Setup GPIO pin as input"

# Set Switch GPIO as input
GPIO.setup(17 , GPIO.IN)

def sensorCallback(channel):
  # Called if sensor output goes Low
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  print "Sensor triggered " + stamp

def main():
  # Wrap main content in a try block so we can
  # catch the user pressing CTRL-C and run the
  # GPIO cleanup function. This will also prevent
  # the user seeing lots of unnecessary error
  # messages.
  
  GPIO.add_event_detect(17, GPIO.FALLING, callback=sensorCallback)  
  
  try:
    # Loop until users quits with CTRL-C
    while True :
      time.sleep(0.1)
        
  except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()
  
if __name__=="__main__":
   main()