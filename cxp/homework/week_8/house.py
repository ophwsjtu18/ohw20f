import mcpi.minecraft as minecraft
import serial
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
ser = serial.Serial("COM10")


class House():
    def __init__(self, xyz):
        self.x = xyz[0]
        self.y = xyz[1]
        self.z = xyz[2]

    def setLWH(self, lwh):
        self.l = lwh[0]
        self.w = lwh[1]
        self.h = lwh[2]

    def set_house_name(self, name):
        self.name = name

    def add_song(self, song):
        self.song = song

    def __build_roof(self):
        for r in range(self.l // 2 + 1):
            rx = self.x - 1 + r
            rz = self.z - 1 + r
            rh = self.y + self.h + r
            for i in range(self.l + 2 - 2 * r):
                mc.setBlock(rx + i, rh, rz, 46)
                mc.setBlock(rx + i, rh, rz + self.l + 1 - 2 * r, 46)
                mc.setBlock(rx, rh, rz + i, 46)
                mc.setBlock(rx + self.l + 1 - 2 * r, rh, rz + i, 46)

    def __build_wall(self):
        for y in range(self.h):
            for x in range(self.l):
                mc.setBlock(self.x + x, self.y + y, self.z, 1)
                mc.setBlock(self.x + x, self.y + y, self.z + self.w - 1, 1)
            for z in range(self.w):
                mc.setBlock(self.x, self.y + y, self.z + z, 1)
                mc.setBlock(self.x + self.l - 1, self.y + y, self.z + z, 1)

    def __build_floor(self):
        for x in range(self.l + 6):
            for z in range(self.w + 6):
                mc.setBlock(self.x - 3 + x, self.y - 1, self.z - 3 + z, 2)
        for x in range(self.l):
            for z in range(self.w):
                mc.setBlock(self.x + x, self.y - 1, self.z + z, 3)

    def __build_door(self):
        door_l = self.l // 3
        door_h = self.h // 2 + 1
        for x in range(door_l, 2 * door_l):
            for y in range(0, door_h):
                mc.setBlock(self.x + x, self.y + y, self.z, 0)

    def __build_window(self):
        window_l = self.l // 3
        window_h = self.h // 3
        for x in range(window_l, 2 * window_l):
            for y in range(window_h, 2 * window_h):
                mc.setBlock(self.x + x, self.y + y, self.z + self.w - 1, 20)
                mc.setBlock(self.x, self.y + y, self.z + x, 20)
                mc.setBlock(self.x + self.l - 1, self.y + y, self.z + x, 20)

    def build_all(self):
        self.__build_floor()
        self.__build_wall()
        self.__build_roof()
        self.__build_door()
        self.__build_window()

    def rebuild_floor(self, floor):
        for x in range(self.l):
            for z in range(self.w):
                if floor[x][z] == '0':
                    cl = 5
                else:
                    cl = 41
                mc.setBlock(self.x + x, self.y - 1, self.z + z, cl)


# [(坐标), (大小), "名字", "歌名"]
bases = [[(-26, 21, -48), (9, 9, 9), "cc", "You Are Not Alone"],
         [(-13, 21, -48), (9, 9, 9), "dd", "Yesterday once more"],
         [(-0, 21, -48), (9, 9, 9), "ee", "Fairy Tale"]]

houses = []

for base in bases:
    house = House(base[0])
    house.setLWH(base[1])
    house.set_house_name(base[2])
    house.add_song(base[3])
    houses.append(house)

for house in houses:
    house.build_all()

# 设置地板花纹
f = open("floor.csv", "r")
floor = []
t = f.readlines()
for line in t:
    line = line.strip().split(",")
    floor.append(line)

for house in houses:
    house.rebuild_floor(floor)

while True:
    time.sleep(0.5)
    pos = mc.player.getTilePos()
    for base in bases:
        if base[0][0] <= pos.x <= base[0][0] + base[1][0] \
                and base[0][1] <= pos.y <= base[0][1] + base[1][1] and \
                base[0][2] <= pos.z <= base[0][2] + base[1][2]:
            print("Welcome to", base[2])
            ser.write(base[3].encode())
