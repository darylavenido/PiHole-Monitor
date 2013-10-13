import spidev
import time
import os

spi = spidev.SpiDev()
spi.open(0,0)

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum):
  if ((adcnum > 7) or (adcnum < 0)):
    return -1
  r = spi.xfer2([1,(8+adcnum)<<4,0])
  adcout = ((r[1]&3) << 8) + r[2]
  return adcout

temp_channel = 1;
light_channel = 0;

while True:

  # read the analog pin
  light_level = readadc(light_channel)
  light_volt = (light_level) * 3.3 / 1023
  
  temp_level = readadc(temp_channel)
  temp_volt = (temp_level) * 3.3 / 1023
  temp = (temp_volt - 0.5) * 100
  
  print "Light : " + str(light_level)
  print "Temp  : " + str(temp_level)
  


  
  print "Light V : " + str(light_volt)
  print "Temp  V : " + str(temp_volt)  
  
  print "Temp = " + str(temp) + " degrees"
  
  print "-------------------------"
  
  time.sleep(5)
 