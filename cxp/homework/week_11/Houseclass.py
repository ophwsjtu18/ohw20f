import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()


class House():
    def __init__(self, x, y, z, l, w, h):
        self.x = x
        self.y = y
        self.z = z
        self.l = l
        self.w = w
        self.h = h

    def build_floor(self):
        for x in range(self.l + 6):
            for z in range(self.w + 6):
                mc.setBlock(self.x - 3 + x, self.y - 1, self.z - 3 + z, 2)
        for x in range(self.l):
            for z in range(self.w):
                mc.setBlock(self.x + x, self.y - 1, self.z + z, 3)

    def build_wall(self):
        for y in range(self.h):
            for x in range(self.l):
                mc.setBlock(self.x + x, self.y + y, self.z, 1)
                mc.setBlock(self.x + x, self.y + y, self.z + self.w - 1, 1)
            for z in range(self.w):
                mc.setBlock(self.x, self.y + y, self.z + z, 1)
                mc.setBlock(self.x + self.l - 1, self.y + y, self.z + z, 1)

    def build_door(self):
        door_l = 4
        door_h = 5
        for x in range(door_l - 1, 2 * door_l - 1):
            for y in range(0, door_h):
                mc.setBlock(self.x + x, self.y + y, self.z, 0)

    def build_window(self):
        window_l = 4
        window_h = 4
        for x in range(window_l - 1, 2 * window_l - 1):
            for y in range(window_h - 1, 2 * window_h - 1):
                mc.setBlock(self.x + x, self.y + y, self.z + self.w - 1, 20)
                mc.setBlock(self.x, self.y + y, self.z + x, 20)
                mc.setBlock(self.x + self.l - 1, self.y + y, self.z + x, 20)

    def build_roof(self):
        for x in range(self.l):
            for z in range(self.w):
                mc.setBlock(self.x + x, self.y + 10, self.z + z, 1)

    def build_all(self):
        self.build_floor()
        self.build_wall()
        self.build_roof()
        self.build_door()
        self.build_window()


class RoundHouse(House):

    def build_roof(self):
        for x in range(self.l):
            mc.setBlock(self.x + x, self.y + 10, self.z, 1)
            mc.setBlock(self.x + x, self.y + 10, self.z + self.w - 1, 1)
        for z in range(self.w):
            mc.setBlock(self.x, self.y + 10, self.z + z, 1)
            mc.setBlock(self.x + self.l - 1, self.y + 10, self.z + z, 1)
        f = open("roof_r.csv", "r")
        floor = []
        t = f.readlines()
        for line in t:
            line = line.strip().split(",")
            floor.append(line)
        for x in range(self.l):
            for z in range(self.w):
                y = eval(floor[x][z]) + 10
                mc.setBlock(self.x + x, self.y + y, self.z + z, 1)

    def build_all(self):
        super().build_floor()
        super().build_wall()
        super().build_door()
        super().build_window()
        self.build_roof()


class TriangleHouse(House):

    def build_roof(self):
        f = open("roof_t.csv", "r")
        floor = []
        t = f.readlines()
        for line in t:
            line = line.strip().split(",")
            floor.append(line)
        for x in range(self.l):
            for z in range(self.w):
                y = eval(floor[x][z]) + 10
                mc.setBlock(self.x + x, self.y + y, self.z + z, 1)

    def build_all(self):
        super().build_floor()
        super().build_wall()
        super().build_door()
        super().build_window()
        self.build_roof()


for i in range(3):
    house1 = House(150 + i*16, 21, -100, 10, 10, 10)
    house1.build_all()
    house2 = RoundHouse(150 + i*16, 21, -100-16, 10, 10, 10)
    house2.build_all()
    house3 = TriangleHouse(150 + i*16, 21, -100-32, 10, 10, 10)
    house3.build_all()
