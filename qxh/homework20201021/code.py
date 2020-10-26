import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
class House():
	def __init__(self,x,y,z):
	    self.x=x
	    self.y=y
	    self.z=z
	    print("Hello world.I will build a house at:",self.x,self.y,self.z)
	def setLWH(self,l,w,h):
		  self.l=l
		  self.w=w
		  self.h=h
	def __buildwall(self):
		  for y in range(self.h):
			    for a in range(self.l):
				      mc.setBlock(self.x+a, self.y+y, self.z,5)
				      mc.setBlock(self.x+a, self.y+y, self.z+self.w-1,5)
			for a in range(self.w):
			    mc.setBlock(self.x, self.y+y, self.z+a,5)
				  mc.setBlock(self.x+self.l-1, self.y+y, self.z+a,5)
	def __buildroof(self):
		   for x in range(self.l):
			     mc.setBlock(self.x+x, self.y, self.z,5)
			     mc.setBlock(self.x+x, self.y, self.z+self.w,5)
		   for z in range(self.w):
			     mc.setBlock(self.x, self.y, self.z+z,5)
			     mc.setBlock(self.x+self.l, self.y, self.z+z,5)
	def __builddoor(self):
		   mc.setBlock(self.x+self.l//2, self.y+1, self.z,64)
		   mc.setBlock(self.x+self.l//2, self.y+2, self.z,64)
	def __buildwindow(self):
		   for z in range(2):
			     for y in range(2):
				       mc.setBlock(self.x, self.y+y+2, self.z+z+self.w//2-1, 20)
				       mc.setBlock(self.x+self.l-1, self.y+y+2, self.z+z+self.w//2-1, 20)
	def buildall(self):
		   self.__buildwall()
		   self.__buildroof()
		   self.__builddoor()
		   self.__buildwindow()
house1 = House(pos.x,pos.y,pos.z)
house1.setLWH(10,10,10)
house1.buildall()
