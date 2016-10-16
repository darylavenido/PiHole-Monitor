#
#
# Based on "image.py" example from Adafruit_Nokia_LCD
#
# ----------------------------------------------------------------------------
#
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import time
import os
from PIL import Image

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

FPS = 20                        # Frames per second
FRAMESPATH = '/home/pi/frames/' # Frames path
CONTRAST = 40                   # Contrast

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Initialize library.
disp.begin(contrast=CONTRAST)

# Clear display.
disp.clear()
disp.display()

try:
  filelist = os.listdir(FRAMESPATH)
  while True:
    for file in filelist:
      if file.endswith('.ppm'):
        # Load image and convert to 1 bit color.
        image = Image.open('frames/'+file).convert('1')
        disp.image(image)
        disp.display()
        time.sleep(1/FPS)
except:
  print "Goodbye!"