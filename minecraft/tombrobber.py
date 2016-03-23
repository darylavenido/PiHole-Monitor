#!/usr/bin/python
#--------------------------------------
#
#     Minecraft Python API
#        Tomb Robber
#
# This script randomly places tombs in the
# world for the player to find.
#
# Author : Matt Hawkins
# Date   : 23/06/2016
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block
import random

#--------------------------------------
# Define Functions
#--------------------------------------

def createTomb(pos,size,blockID):
  # A tomb at a set position with a given material
  x1 = pos[0] + (size/2)
  y1 = pos[1]
  z1 = pos[2] + (size/2)
  x2 = pos[0] - (size/2)
  y2 = pos[1] - size
  z2 = pos[2] - (size/2)
  mc.setBlocks(x1,y1,z1,x2,y2,z2,blockID) 
  
def addTreasure(pos,size,blockID)
  # Add treasure to tomb at position "pos"
  x = pos[0]
  y = pos[1] - (size-1)
  z = pos[2]
  mc.setBlock(x,y,z,blockID)
  
def getLocation():

  scan=True
  while scan==True:
    x = random.randint(-120, 120)
    z = random.randint(-120, 120)  
    y = mc.getHeight(x,y)
  
    # check what block we have hit  
    if getBlock(x,y,z) in [block.SAND,block.DIRT]:
      scan=False
  
  pos=(x,y,z)
  
  return pos
  
#--------------------------------------
#
# Main Script  
#
#--------------------------------------

mc = minecraft.Minecraft.create()

random.seed

mc.postToChat("Let's rob some graves!")

print("Place 5 random tombs and treasure")

for tomb in range[5]:
  
  pos = getLocation()
  
  # Place marker in the sky
  mc.setBlock(pos[0],pos[1]+20,pos[2],block.GLASS)  
  createTomb(pos,8,block.STONE)  
  addTreasure(pos,8,block.GOLD)
 
  print("Tomb "+ tomb + " placed "+pos) 

# mc.player.setPos(0,30,4)