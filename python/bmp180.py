#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____          
#   / _ \/ _ \(_) __/__  __ __ 
#  / , _/ ___/ /\ \/ _ \/ // / 
# /_/|_/_/  /_/___/ .__/\_, /  
#                /_/   /___/   
#
#           bmp180.py
#  Read data from a digital pressure sensor.
#
# Author : Matt Hawkins
# Date   : 29/03/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------
import smbus
import time
from ctypes import c_short
 
# Simple function to convert binary data into
# a string
def convertToString(data):
  return str((data[1] + (256 * data[0])) / 1.2)
 
# Define some constants from the datasheet

DEVICE     = 0x77 # Device address
OVERSAMPLE = 3    # 0 - 3

# Register Addresses
REG_ID    = 0xD0
REG_CALIB = 0xAA
REG_MEAS  = 0xF4
REG_MSB   = 0xF6
REG_LSB   = 0xF7

# Control Register Address
CRV_TEMP  = 0x2E
CRV_PRES  = 0x34

#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

# return two bytes from data as a signed 16-bit value
def get_short(data, index):
        return c_short((data[index] << 8) + data[index + 1]).value

# return two bytes from data as an unsigned 16-bit value
def get_ushort(data, index):
        return (data[index] << 8) + data[index + 1]

(chip_id, chip_version) = bus.read_i2c_block_data(DEVICE, REG_ID, 2)
print "Chip ID:", chip_id
print "Version:", chip_version

print
# Read calibration data
# Read calibration data from EEPROM
cal = bus.read_i2c_block_data(DEVICE, REG_CALIB, 22)

# Convert byte data to word values
AC1 = get_short(cal, 0)
AC2 = get_short(cal, 2)
AC3 = get_short(cal, 4)
AC4 = get_ushort(cal, 6)
AC5 = get_ushort(cal, 8)
AC6 = get_ushort(cal, 10)
B1  = get_short(cal, 12)
B2  = get_short(cal, 14)
MB  = get_short(cal, 16)
MC  = get_short(cal, 18)
MD  = get_short(cal, 20)

# Read temperature
bus.write_byte_data(DEVICE, REG_MEAS, CRV_TEMP)
time.sleep(0.005)
(msb, lsb) = bus.read_i2c_block_data(DEVICE, REG_MSB, 2)
UT = (msb << 8) + lsb

# Read pressure
bus.write_byte_data(DEVICE, REG_MEAS, CRV_PRES + (OVERSAMPLE << 6))
time.sleep(0.04)
(msb, lsb, xsb) = bus.read_i2c_block_data(DEVICE, REG_MSB, 3)
UP = ((msb << 16) + (lsb << 8) + xsb) >> (8 - OVERSAMPLE)

# Refine temperature
X1 = ((UT - AC6) * AC5) >> 15
X2 = (MC << 11) / (X1 + MD)
B5 = X1 + X2
temperature = (B5 + 8) >> 4

# Refine pressure
B6  = B5 - 4000
B62 = B6 * B6 >> 12
X1  = (B2 * B62) >> 11
X2  = AC2 * B6 >> 11
X3  = X1 + X2
B3  = (((AC1 * 4 + X3) << OVERSAMPLE) + 2) >> 2

X1 = AC3 * B6 >> 13
X2 = (B1 * B62) >> 16
X3 = ((X1 + X2) + 2) >> 2
B4 = (AC4 * (X3 + 32768)) >> 15
B7 = (UP - B3) * (50000 >> OVERSAMPLE)

P = (B7 * 2) / B4

X1 = (P >> 8) * (P >> 8)
X1 = (X1 * 3038) >> 16
X2 = (-7357 * P) >> 16
pressure = P + ((X1 + X2 + 3791) >> 4)

print "Temperature : ", temperature/10.0, "C"
print "Pressure    : ", pressure/ 100.0, "mbar"