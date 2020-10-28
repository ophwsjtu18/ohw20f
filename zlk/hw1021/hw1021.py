import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

class House:
    def __init__(self,halflendth,halfwidth,height,pos,mc):
        self.halflendth=halflendth
        self.halfwidth=halfwidth
        self.height=height
        self.x=pos.x
        self.y=pos.y
        self.z=pos.z
        self.mc=mc
        self.__buildwall()
        self.__buildwindow()
        self.__builddoor()
        self.__buildroof()
    def __buildwall(self):
        for i in range(self.height):
            for j in range(2*self.halflendth+1):
                mc.setBlock(self.x+self.halfwidth-j,self.y+i,self.z-self.halflendth,block.STONE.id)
                mc.setBlock(self.x+self.halfwidth-j,self.y+i,self.z+self.halflendth,block.STONE.id)
        for i in range(self.height):
            for j in range(2*self.halflendth+1):
                mc.setBlock(self.x-self.halfwidth,self.y+i,self.z+self.halflendth+1-j,block.STONE.id)
                mc.setBlock(self.x+self.halfwidth,self.y+i,self.z+self.halflendth+1-j,block.STONE.id)
    def __buildwindow(self):
        self.setBlocks(pos.x-1,self.x+1,self.y+self.height-4,self.y+self.height-2,self.z+self.halflendth,self.z+self.halflendth,0)
        self.setBlocks(self.x-self.halfwidth,self.x-self.halfwidth,self.y+self.height-4,self.y+self.height-2,self.z-1,self.z+1,0)
        self.setBlocks(self.x+self.halfwidth,self.x+self.halfwidth,self.y+self.height-4,self.y+self.height-2,self.z-1,self.z+1,0)

    def __builddoor(self):
        self.setBlocks(pos.x-2,self.x+2,self.y,self.y+3,self.z-self.halflendth,self.z-self.halflendth,0)
    
    def __buildroof(self):
        self.setBlocks(pos.x-self.halfwidth,self.x+self.halfwidth,self.y+self.height,self.y+self.height,self.z-self.halflendth,self.z+self.halflendth,block.DIAMOND_BLOCK.id)
    def setBlocks(self,a,b,c,d,e,f,id):
        for i in range(a,b+1):
            for j in range(c,d+1):
                for k in range(e,f+1):
                    mc.setBlock(i,j,k,id)



House(4,4,8,pos,mc)


