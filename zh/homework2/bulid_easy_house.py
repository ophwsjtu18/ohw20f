import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
class POS():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

#pos = POS(200, 0, 0)
  
size = 10 #暂只能偶数
bulid_id = 5

class House(object):
    def __init__(self, x, y, z, size):
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        print("the house location:(" + str(x) + ", " + str(y) + ", " + str(z) + ") the size is: " + str(size))

    def clear(self):
        for i in range(-2*size, 2*size):
            for j in range(-2*size, 2*size):
                for k in range(3*size):
                    mc.setBlock(pos.x + j, pos.y + k, pos.z + i, 0)

    def creat_wall_and_floor(self):
        for i in range(size):
            for j in range(size):
                mc.setBlock(pos.x - size//2 + j, pos.y, pos.z - size//2 + i, bulid_id)

        for i in range(size // 2):
            for j in range(size):
                mc.setBlock(pos.x - size//2 + j, pos.y + i, pos.z - size//2, bulid_id)
                mc.setBlock(pos.x - size//2, pos.y + i, pos.z - size//2 + j, bulid_id)
                mc.setBlock(pos.x + size//2, pos.y + i, pos.z - size//2 + j, bulid_id)
                mc.setBlock(pos.x - size//2 + j, pos.y + i, pos.z + size//2, bulid_id)

        for i in range(size//2):
            mc.setBlock(pos.x + size//2, pos.y + i, pos.z + size//2, bulid_id)

        mc.setBlock(pos.x + 1, pos.y, pos.z, 1)

        #roof
        glass_id_1 = 20
        for i in range(1, size//2 + 1):
            for j in range(i, size - i + 1):
                mc.setBlock(pos.x - size//2 + j, pos.y + size//2 + i - 1, pos.z + size//2 - i, glass_id_1)
                mc.setBlock(pos.x + size//2 - i, pos.y + size//2 + i - 1, pos.z - size//2 + j, glass_id_1)
                mc.setBlock(pos.x - size//2 + j, pos.y + size//2 + i - 1, pos.z - size//2 + i, glass_id_1)
                mc.setBlock(pos.x - size//2 + i, pos.y + size//2 + i - 1, pos.z - size//2 + j, glass_id_1)


    def creat_door(self):
        mc.setBlock(pos.x + size//2, pos.y + 1, pos.z, 0)
        mc.setBlock(pos.x + size//2, pos.y + 2, pos.z, 0)

    def creat_window(self):
        glass_id_2 = 102
        for i in range(2):
            for j in range(2):
                mc.setBlock(pos.x + size//2, pos.y + 2 + j, pos.z + 2 + i, glass_id_2)
                mc.setBlock(pos.x + size//2, pos.y + 2 + j, pos.z - 2 - i, glass_id_2)
                mc.setBlock(pos.x + 2 + i, pos.y + 2 + j, pos.z + size//2, glass_id_2)
                mc.setBlock(pos.x - 2 - i, pos.y + 2 + j, pos.z + size//2, glass_id_2)
                mc.setBlock(pos.x + 2 + i, pos.y + 2 + j, pos.z - size//2, glass_id_2)
                mc.setBlock(pos.x - 2 - i, pos.y + 2 + j, pos.z - size//2, glass_id_2)
                mc.setBlock(pos.x - size//2, pos.y + 2 + j, pos.z + 2 + i, glass_id_2)
                mc.setBlock(pos.x - size//2, pos.y + 2 + j, pos.z - 2 - i, glass_id_2)

    def creat_whole_house(self):
        self.clear()
        self.creat_wall_and_floor()
        self.creat_door()
        self.creat_window()
        
house = House(pos.x, pos.y, pos.z, 10)
house.creat_whole_house()

'''
stayed_time = 0
while True:
    
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    
    pos_now=mc.player.getTilePos()
    mc.postToChat("please goto home x=100 y=0 z=0 for 15s to fly")
    mc.postToChat("x:"+str(pos_now.x)+"y:"+str(pos_now.y)+"z:"+str(pos_now.z))
    
    hits=mc.events.pollBlockHits() 
    for hit in hits:
        mc.postToChat("Hit:"+"x"+str(hit.pos_now.x)+"y"+str(hit.pos_now.y)+"z"+str(hit.pos_now.z))
        
    if 100 - size//2 <= pos_now.x <= 100 + size//2 and 0 <= pos_now.y <= 0 + size//2 and 0 - size//2 <= pos_now.z <= 0 + size//2:
        mc.postToChat("welcome home,please wait for 30 rounds for fly")
        mc.postToChat("Or hit something by right click sword, you will fly immediately")
        if len(hits) !=0:
            stayed_time=31
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(80,20,0)
            stayed_time=0
    else:
        stayed_time=0
'''