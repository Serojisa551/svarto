class BuilderCar:
    def buildDoor(self, number):
        self.door = number
        return self
    
    def buildWheel(self, number):
        self.wheel = number
        return  self
    
    def buildMotor(self, view):
        self.motor = view
        return self 

    def buildGps(self, availability):
        self.gps = availability
        return self

    def buildSpareWheel(self, availability):
        self.spareWheel = availability 
        return self


bmw = BuilderCar()
bmw = bmw.buildDoor(2)
bmw = bmw.buildMotor("petrol")
bmw = bmw.buildGps("network")
bmw = bmw.buildWheel(4)
print(bmw.door)
# bmw = bmw.buildWheel(4)
# print(bmw)