# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

mc.postToChat("Let's build a castle!")

def CreateWalls(size,baseheight,height,material,battlements,walkway):
  mc.setBlocks(-size,baseheight+1,-size,size,baseheight+height,-size,material) 
  mc.setBlocks(-size,baseheight+1,-size,-size,baseheight+height,size,material)
  mc.setBlocks(size,baseheight+1,size,-size,baseheight+height,size,material) 
  mc.setBlocks(size,baseheight+1,size,size,baseheight+height,-size,material) 

  # Add battlements to top edge
  if battlements==True:
    for x in range(0,(2*size)+1,2):
      mc.setBlock(size,baseheight+height+1,(x-size),material) 
      mc.setBlock(-size,baseheight+height+1,(x-size),material) 
      mc.setBlock((x-size),baseheight+height+1,size,material) 
      mc.setBlock((x-size),baseheight+height+1,-size,material)
      
  # Add wooden walkways
  if walkway==True:  
    mc.setBlocks(-size+1,baseheight+height-1,size-1,size-1,baseheight+height-1,size-1,block.WOOD_PLANKS)   
    mc.setBlocks(-size+1,baseheight+height-1,-size+1,size-1,baseheight+height-1,-size+1,block.WOOD_PLANKS)  
    mc.setBlocks(-size+1,baseheight+height-1,-size+1,-size+1,baseheight+height-1,size-1,block.WOOD_PLANKS)   
    mc.setBlocks(size-1,baseheight+height-1,-size+1,size-1,baseheight+height-1,size-1,block.WOOD_PLANKS)  

def CreateLandscape():
  # Set upper half to air
  mc.setBlocks(-128,1,-128,128,128,128,block.AIR) 
  # Set lower half of world to dirt with a layer of grass
  mc.setBlocks(-128,0,-128,128,0,128,block.GRASS)
  mc.setBlocks(-128,-1,-128,128,-128,128,block.DIRT)
  # Water
  mc.setBlocks(-33,0,-33,33,0,33,block.WATER)
  # Island
  mc.setBlocks(-23,0,-23,23,1,23,block.GRASS)  

def CreateWindows(x,y,z,dir):

  if dir=="N" or dir=="S":
    z1=z
    z2=z
    x1=x-2
    x2=x+2

  if dir=="E" or dir=="W":
    z1=z-2
    z2=z+2
    x1=x
    x2=x

  mc.setBlocks(x1,y,z1,x1,y+1,z1,block.AIR)
  mc.setBlocks(x2,y,z2,x2,y+1,z2,block.AIR) 

  if dir=="N":
    a=3
  if dir=="S":
    a=2
  if dir=="W":
    a=0
  if dir=="E":
    a=1

  mc.setBlock(x1,y-1,z1,109,a)
  mc.setBlock(x2,y-1,z2,109,a)

  #mc.setBlocks(x1+x3,y-1,z1+z3,x2+x3,y-1,z2+z3,block.STONE) 
  #mc.setBlocks(x1+x3,y  ,z1+z3,x2+x3,y  ,z2+z3,block.FENCE) 

def CreateKeep(size,baseheight,levels):
  # Create a keep with a specified number
  # of floors levels and a roof
  height=(levels*5)+5
  
  CreateWalls(size,baseheight,height,block.STONE_BRICK,True,True)
  
  # Floors & Windows
  for level in range(1,levels+1):
    mc.setBlocks(-size+1,(level*5)+baseheight,-size+1,size-1,(level*5)+baseheight,size-1,block.WOOD_PLANKS)

  # Windows
  for level in range(1,levels+1):
    CreateWindows(0,(level*5)+baseheight+2,size,"N")
    CreateWindows(0,(level*5)+baseheight+2,-size,"S")
    CreateWindows(-size,(level*5)+baseheight+2,0,"W")
    CreateWindows(size,(level*5)+baseheight+2,0,"E")

  # Door
  mc.setBlocks(0,baseheight+1,size,0,baseheight+2,size,block.AIR)

# Setup ground
CreateLandscape()  

# Outer walls
CreateWalls(21,1,5,block.STONE_BRICK,True,True)
# Inner walls
CreateWalls(13,1,6,block.STONE_BRICK,True,True)

# Keep
CreateKeep(5,1,4)

print "Position player in corner" 
mc.player.setPos(0,2,0)