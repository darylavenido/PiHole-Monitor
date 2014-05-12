# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

playerPos = mc.player.getTilePos()
blockBelowPlayer = mc.getBlockWithData(playerPos.x, playerPos.y - 1, playerPos.z)

mc.postToChat("You are standing Block ID : {} Data : {}".format(blockBelowPlayer.id,blockBelowPlayer.data))

