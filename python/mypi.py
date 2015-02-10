#!/usr/bin/python
#--------------------------------------
#
#                mypi.py
#  Functions to display Pi properties
#
#  If called directly outputs :
#  - Revision number
#  - Serial number
#  - Mac address
#  - IP address
#
# Author : Matt Hawkins
# Date   : 10/02/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Define functions

def getmac(interface='eth0'):
  # Return the MAC address of interface
  try:
    line = open('/sys/class/net/%s/address' %interface).readline()
  except:
    line = "Error"
  return line[0:17]

def getserial():
  # Extract serial from cpuinfo file
  mycpuserial = "Error"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        mycpuserial = line[10:26]
    f.close()
  except:
    mycpuserial = "Error"

  return cpuserial

def getrevision():
  # Extract board revision from cpuinfo file
  myrevision = "Error"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:8]=='Revision':
        myrevision = line[11:-1]
    f.close()
  except:
    myrevision = "Error"

  return myrevision

def getip(interface='eth0'):
  # Read ifconfig.txt and extract IP address
  try:
    #filename = 'ifconfig_' + interface + '.txt'
    #os.system('ifconfig ' + interface + ' > /home/pi/' + filename)
    #f = open('/home/pi/' + filename, 'r')
    f = open('d:\ifconfig.txt', 'r')
    line = f.readline() # skip 1st line
    line = f.readline() # read 2nd line
    line = line.strip()
    f.close()

    if line.startswith('inet addr:'):
      a,b,c = line.partition('inet addr:')
      a,b,c = c.partition(' ')
    else:
      a = 'None'

    return a

  except:
    return 'Error'


if __name__ == '__main__':

  # Script has been called directly

  #myRevision = getrevision()
  #mySerial = getserial()
  #myMAC = getMAC()
  myIp = getip()

  print "Revision Number : " + myIp
  print "Serial Number   : " + myIp
  print "Mac Address     : " + myIp
  print "IP Address      : " + myIp