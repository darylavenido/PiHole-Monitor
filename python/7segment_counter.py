#!/usr/bin/python
#-------------------------------------------------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
# 4-digit 7-Segment Module Counter Demo
#
# This example uses the Adafruit library to display
# a counter on an LED module.
#
# Please see :
# https://www.raspberrypi-spy.co.uk/2018/11/raspberry-pi-7-segment-led-display-module-using-python/
# for more information.
#
# Author : Matt Hawkins
# Date   : 05/11/2018
#
#-------------------------------------------------------------------------------

# Import required libraries
import time
from Adafruit_LED_Backpack import SevenSegment


# Create display instance on default I2C address (0x70) and bus number.
display = SevenSegment.SevenSegment()

# Initialize the display. Must be called once before using the display.
display.begin()

# Keep track of the colon being turned on or off.
colon = False

# Run through different number printing examples.
print('Press Ctrl-C to quit.')

# Toggle colon display
display.clear()
display.set_colon(True)
display.write_display()
time.sleep(1)
display.set_colon(False)
display.write_display()
time.sleep(1)

# Display sequence of numbers
while True:
  for i in range(500,1000):
    display.clear()
    display.print_float(i,decimal_digits=0)
    display.write_display()
    # Delay for a second.
    time.sleep(0.1)
