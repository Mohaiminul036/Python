class Rect:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.area = self.width*self.height

    def setSize(self,size):
        self.width, self.height = size
        self.area = self.width*self.height
        print("setSize(): I worked like a common property, but actually, I am a method.")

    def getSize(self):
        print("getSize(): I am a method too.")
        return self.width,self.height

    size = property(getSize,setSize)


r0 = Rect()
r0.size = 120,20
r1 = Rect()
r1.size = 13,30
print("Rect:", r0.size, "Area =",r0.area)
print("Rect:", r1.size, "Area =",r1.area)