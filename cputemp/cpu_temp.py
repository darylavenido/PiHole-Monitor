#!/usr/bin/python3
#-----------------------------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
# Project : Pi CPU Temperature Logger
# File    : cpu_temp.py
#
# Script to log the CPU temperature to a CSV text file.
#
# Author : Matt Hawkins
# Date   : 31/10/2019
# Source : https://bitbucket.org/MattHawkinsUK/rpispy-misc/src/master/cputemp/
#
# Additional details here:
# https://www.raspberrypi-spy.co.uk/
#
# gpiozero CPUTemperature reference:
# https://gpiozero.readthedocs.io/en/stable/api_internal.html?#cputemperature
#
#-----------------------------------------------------------

# Standard libraries
from time import sleep, strftime, time
from gpiozero import CPUTemperature

# Create CPU object
cpu = CPUTemperature()

# Define function to write temps to file
def log_temp(samples,interval):
    with open("/home/pi/cpu_temp.csv", "a") as log:
        for x in range(samples):
            temp = cpu.temperature
            data = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp))
            print(data, end='')
            log.write(data)
            sleep(interval)
try:
    while True:
        # Log temps every 10 seconds, update file every 6 writes
        log_temp(6,10)
except KeyboardInterrupt:
    print()
