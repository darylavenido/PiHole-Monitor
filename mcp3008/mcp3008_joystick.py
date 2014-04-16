#!/usr/bin/python
#--------------------------------------   
# This script reads data from a 
# MCP3008 ADC device using the SPI bus.
#
# Analogue joystick version!
#
# Author : Matt Hawkins
# Date   : 16/04/2014
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

import spidev
import time
import os

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Define sensor channels
swt_channel = 0
vrx_channel = 1
vry_channel = 2
# unused channel 3
# unused channel 4
# unused channel 5
# unused channel 6
# unused channel 7

# Define delay between readings (s)
delay = 1

while True:

  # Read the joystick position data
  vrx_position = ReadChannel(vrx_channel)
  vry_position = ReadChannel(vry_channel)

  # Read switch state
  swt_value = ReadChannel(swt_channel)

  # Print out results
  print "--------------------------------------------"  
  print("X : {}  Y : {}  Switch : {}".format(vrx_position,vry_position,swt_value))

  # Wait before repeating loop
  time.sleep(delay)