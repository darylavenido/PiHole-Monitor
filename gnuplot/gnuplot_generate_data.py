#!/usr/bin/python
import math

f = open('mydata.dat', 'w')

# Loop
for degrees in range(720):

  s = math.sin(math.radians(degrees))
  c = 0.5 * math.cos(math.radians(degrees))
  
  # Write raw data to text file
  data = "{} {} {}\n".format(degrees,s,c)
  f.write(data)

f.close()
