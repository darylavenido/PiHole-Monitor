#!/usr/bin/env python

import max7219.led as led
import sys
import time
import random

def getRandomChar():
  # Get a random character 
  charset = '0123456789abcdefghijklmnopqrstuvwxyz-'
  val = random.randint(0,len(charset)-1)
  return sequence1[val]

if len(sys.argv)>1:
  mode=sys.argv[1]
  mode=mode.lower()
else:
  mode='random'
  
# Setup display
device = led.sevensegment()
device.brightness(2)
device.clear()

interval = 1.2

starttext = 'B0BA8ETT'

sequence = [' dmeug  ',
            ' 88888  ',
            ' dmeug  ',
            ' sexyn  ',
            ' kiqho  ',
            ' dmeug  ',
            ' njvwh  ',
            ' kiqho  ',
            ' dmeug  ',
            ' ntvzp  ',
            ' dmeug  ',
            ' sexyn  '
]

# Display text
for index, char in enumerate(starttext):
  device.letter(0, 8-index, char)   

time.sleep(1)

# Display random symbols
while mode=='random':
  for index in range(1,9):
    device.letter(0, index, getRandomChar())  
  time.sleep(interval)

# Display sequence
while mode=='seq':
  for item in sequence:
    for index, char in enumerate(item):
      device.letter(0, 8-index, char)      
    time.sleep(interval)