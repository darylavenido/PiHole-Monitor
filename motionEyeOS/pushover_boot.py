#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#           pushover_boot.py
#  Send pushover notification when motionEyeOS boots.
#  Use with userinit.sh
#
# Author : Matt Hawkins
# Date   : 12/06/2020
#
# https://www.raspberrypi-spy.co.uk/tag/motioneyeos/
#
# Based on Python examples here:
# https://pushover.net/faq#library
#
#--------------------------------------
import httplib, urllib
import sys
import socket
import subprocess

def get_ip(interface):
  ip_address=""
  try:
    process = subprocess.Popen(['ifconfig', interface],stdout=subprocess.PIPE,universal_newlines=True)
    ifconfig_output=process.communicate()[0]
    x=ifconfig_output.find("inet ")
    if x>0:
      y=ifconfig_output.find(" ",x+5)
      ip_address=ifconfig_output[x+5:y]
  except:
    pass
  return ip_address

if len(sys.argv)==4:

  # Get 3 arguments passed to this script
  myip=sys.argv[1]
  myuser=sys.argv[2]
  mytoken=sys.argv[3]
  
  # Get hostname of this system
  myhostname=socket.gethostname()
  
  # Get local ip address of this system
  eth0_address=get_ip("eth0")
  wlan0_address=get_ip("wlan0")

  # Create parameters to pass to Pushover service
  mytitle=myhostname+" camera rebooted"

  mymessage ="<p>"+myhostname+" has just rebooted</p>"
  if eth0_address<>"":
    mymessage+="<p>IP (eth0): <a href='http://"+eth0_address+"'>"+eth0_address+"</a></p>"
  if wlan0_address<>"":
    mymessage+="<p>IP (wlan0): <a href='http://"+wlan0_address+"'>"+wlan0_address+"</p>"
  mymessage+="<p>Internet IP: <a href='http://"+myip+"'>"+myip+"</a></p>"

  print(mytitle)

  conn = httplib.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
    urllib.urlencode({
      "token": mytoken,      # Pushover app token
      "user": myuser,        # Pushover user token
      "html": "1",           # 1 for HTML, 0 to disable
      "title": mytitle,      # Title of message
      "message": mymessage,  # Message (HTML if required)
      "sound": "cosmic",     # Sound played on receiving device
    }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()
