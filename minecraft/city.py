import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

CityBlockSize=10

def clearWorld(blk):
  print "Clear world"
  mc.setBlocks(-128, -128, -128, 128, 128, 128, blk)
  mc.setBlocks(-128, -1, -128, 128, -1, 128, block.DIRT.id)
  mc.player.setPos(0,10,0)

def processLine(line,z):
  x=0
  line=cleanList(line)
  for symbol in line:
    x=x+1
    processSymbol(symbol,x,z)

def processSymbol(symbol,x,z):
  
  functions = {
    '.': symbolGrass,
    'w': symbolWater,
    '|': symbolRoadNorth,
    '-': symbolRoadWest,
    'x': symbolRoadCross,
    '1': symbol1
  }

  func = functions[symbol]
  func(x,z)

def cleanList(list):

  CleanedList=[]

  for item in list:
    if item!="\n":
      CleanedList.append(item)

  return CleanedList

def symbolGrass(x,z):
  X=coordScale(x)
  Z=coordScale(z)
  print "[",x,",",z,"] ", "[",X,",",Z,"] Grass"
  mc.setBlocks(X, 0, Z, X+9, 0, Z+9, block.GRASS.id)
  
def symbolWater(x,z):
  X=coordScale(x)
  Z=coordScale(z)
  print "[",x,",",z,"] ", "[",X,",",Z,"] Water"
  mc.setBlocks(X, 0, Z, X+9, 0, Z+9, block.WATER.id)

def symbolRoadNorth(x,z):
  X=coordScale(x)
  Z=coordScale(z)
  print "[",x,",",z,"] ","Road"
  mc.setBlocks(X, 0, Z, X+9, 0, Z+9, block.GRASS.id)
  mc.setBlocks(X+1, 0, Z, X+8, 0, Z+9, block.STONE.id)
  mc.setBlocks(X+1, 0, Z, X+1, 0, Z+9, block.IRON_ORE.id)
  mc.setBlocks(X+8, 0, Z, X+8, 0, Z+9, block.IRON_ORE.id)

def symbolRoadWest(x,z):
  X=coordScale(x)
  Z=coordScale(z)
  print "[",x,",",z,"] ", "[",X,",",Z,"] Road"
  mc.setBlocks(X, 0, Z, X+9, 0, Z+9, block.STONE.id)

def symbolRoadCross(x,z):
  X=coordScale(x)
  Z=coordScale(z)
  print "[",x,",",z,"] ","Road"
  mc.setBlocks(X, 0, Z, X+9, 0, Z+9, block.STONE.id)

def symbol1(x,z):

  X=coordScale(x)
  Z=coordScale(z)
  print "[",x,",",z,"] ", "[",X,",",Z,"] Building1"
  mc.setBlocks(X, 0, Z, X+9, 0, Z+9, block.STONE.id)
  mc.setBlocks(X+1, 0, Z+1, X+8, 5, Z+8, block.STONE.id)

def coordScale(i):
  global CityBlockSize
  I=((i-1)*CityBlockSize)-128
  return I

def main():

  mc.postToChat("Start city building")

  clearWorld(block.AIR.id)

  f = open('city.map', 'r')
  listLines = f.readlines()

  z=0
  for line in listLines:
    z=z+1
    processLine(line,z)

  mc.postToChat("All finished")

if __name__ == "__main__":
  main()