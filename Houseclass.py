class House():
    def __init__(self,x,y,z,l,w,h):
        self.x=x
        self.y=y
        self.z=z
        self.l=l
        self.w=w
        self.h=h
        print("I will build a house on",self.x,self.y,self.z,self.l,self.w,self.h)
    def __buildwall__(self):
        print("build wall",self.l,self.w,self.h)
    def __buildroof(self):
        print("build a rectangel roof")
    def buildall(self):
        self.__buildwall__()
        self.__buildroof()

house1=House(100,100,100,10,10,10)
house1.buildall()

class RoundHouse(House):
    def __init__(self,x,y,z,l,w,h,r):
        super(RoundHouse,self).__init__(x,y,z,l,w,h)
        self.r=r
        print("i will build a round roof house r is",self.r)
    def __buildroof(self):
        print("build a round roof")
    def buildall(self):
        super(RoundHouse,self).__buildwall__()
        self.__buildroof()

        

house2=RoundHouse(100,100,100,10,10,10,8)
house2.buildall()

