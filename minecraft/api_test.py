# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

# Get player position
pPos = mc.player.getPos()
pPos = minecraft.Vec3(int(pPos.x),int(pPos.y),int(pPos.z))

mc.postToChat("API Test!")

# Change block
print "Create stone block"   
mc.setBlocks(pPos.x-1,pPos.y,pPos.z-1,pPos.x+1,pPos.y+2,pPos.z+1,block.STONE)

print "Position player on top" 
mc.player.setPos(pPos.x,pPos.y+3,pPos.z)