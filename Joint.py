import math

class Joints:
    def __init__(self, x, y, length) -> None:
        self.x = x
        self.y = y
        self.armLengths = length

    def calculateArmSlopes(self):
        vertexHeight = math.sqrt(self.armLengths[0]**2-self.x/2**2) #Pythagorean theorem
        # jointOneAngle = math.asin(vertexHeight/self.length)
        jointOneAngle = math.acos((self.x/2)/self.armLengths[0])

        jointTwoAngle = (180-2*jointOneAngle)/2 #divide by two since angle is bisected
        if self.y == 0:
            return [jointOneAngle, jointTwoAngle]
        
    def calculateArmSlopes(self,x,y):
        self.jointTwoAngle = math.acos((x**2+y**2-self.armLengths[0]**2-self.armLengths[1]**2)/(2*self.armLengths[0]*self.armLengths[1]))

        self.jointOneAngle = math.atan(y/x) - math.atan((self.armLengths[1]*math.sin(self.jointTwoAngle))/(self.armLengths[0]+self.armLengths[1]*math.cos(self.jointTwoAngle)))

        return [self.jointOneAngle, self.jointTwoAngle]