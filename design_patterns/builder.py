class BuilderCar:
    def buildDoor(self, number = None):
        # if number != None:
        self.door = number
        # return self.door
    
    def buildWheel(self, number):
        self.wheel = number
        # return self.wheel
    
    def buildMotor(self, view):
        self.motor = view
        # return self.motor

    def buildGps(self, availability):
        self.gps = availability
        # return self.gps

    def buildSpareWheel(self, availability):
        self.spareWheel = availability 
        # return self.spareWheel 


bmw = BuilderCar()
bmw = bmw.buildDoor(2)
print(bmw)
# bmw = bmw.buildWheel(4)
# print(bmw)