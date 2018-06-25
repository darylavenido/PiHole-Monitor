#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
# WiFi Monitoring Script
#
# This script extracts parameters from the
# iwconfig command line utility to monitor
# the health of the WiFi connection.
#
# The intention is that this script would be imported
# into another script that would make use of the
# parameters of interest. See iwconfig_log.py for an
# example.
#
# Please see https://www.raspberrypi-spy.co.uk/
# for more information.
#
# Author : Matt Hawkins
# Date   : 23/06/2018
#
#--------------------------------------

import time
import subprocess

# Define some functions

def getOutput(interface='wlan0'):
  # Get text output of iwconfig for specified interface
  try:
    output=subprocess.check_output(['iwconfig', interface])
    output=output.decode("utf-8") 
    output=output.replace('\n', '|')
  except:
    output="x"

  return output

def extract(output,startstr,stopstr):
  # Take a string and cut out characters between
  # two specified strings
  start=output.find(startstr)
  stop=output.find(stopstr,start)
  if start>-1 and stop>-1 and (stop>start):
    output=output[start+len(startstr):stop].strip()
  else:
    output="-"

  return output

def getParameters(data):
  # Extract each parameter from text output
  parameters={}
  essid=extract(data,"ESSID:"," ")
  mode=extract(data,"Mode:","Frequency")
  frequency=extract(data,"Frequency:","Access")
  access=extract(data,"Access Point:","|")
  bitrate=extract(data,"Bit Rate=","Tx-Power")
  txpower=extract(data,"Tx-Power=","|")
  powermanage=extract(data,"Power Management:","|")
  quality=extract(data,"Link Quality=","Signal")
  signal=extract(data,"Signal level=","|")

  # Build dictionary
  parameters={'ESSID':essid,
        'Mode':mode,
        'Frequency':frequency,
        'Access Point':access,
        'Bit Rate':bitrate,
        'Tx-Power':txpower,
        'Power Management':powermanage,
        'Link Quality':quality,
        'Signal Level':signal
    }

  return parameters

def printParameters(parameters):
  # Print all parameters
  print("ESSID            : "+parameters["ESSID"])
  print("Mode             : "+parameters["Mode"])
  print("Frequency        : "+parameters["Frequency"])
  print("Access Point     : "+parameters["Access Point"])
  print("Bit Rate         : "+parameters["Bit Rate"])
  print("Tx-Power         : "+parameters["Tx-Power"])
  print("Power Management : "+parameters["Power Management"])
  print("Link Quality     : "+parameters["Link Quality"])
  print("Signal level     : "+parameters["Signal Level"])

def main():
  output=getOutput()
  # Extract parameters
  parameters=getParameters(output)

  # Print parameters
  printParameters(parameters)

# If script called directly run the main function
if __name__== "__main__":
  main()
