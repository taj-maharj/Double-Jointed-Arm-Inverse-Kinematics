import turtle
from Joint import Joints
class main:
    

    def __init__(self):
        self.armLengths = [35,40]
        self.globalX = 30
        self.globalY = 20
        self.joints = Joints(self.globalX, self.globalY, self.armLengths)
        self.armAngles = self.joints.calculateArmSlopes(self.globalX, self.globalY)
        turtle.setworldcoordinates(-50,-50,100,100)
        turtle.hideturtle()
        turtle.speed(1000000000)
        

    def draw(self,x,y):
        turtle.speed(1000000000)
        self.globalX = x
        self.globalY = y
        self.armAngles = self.joints.calculateArmSlopes(self.globalX, self.globalY)
        if self.armLengths[0]+self.armLengths[1] >= self.globalX:
            turtle.reset()
            turtle.speed(1000000000)
            turtle.hideturtle()
            turtle.radians()

            turtle.left(self.armAngles[0])
            if x<0:
                turtle.backward(self.armLengths[0])
            else:
                turtle.forward(self.armLengths[0])

            turtle.left(self.armAngles[1])

            if x<0:
                turtle.backward(self.armLengths[1])
            else:
                turtle.forward(self.armLengths[1])

            print(turtle.pos())

    
m = main()
m.draw(10,10)
turtle.onscreenclick(m.draw)
# turtle.Screen().clearscreen()
turtle.mainloop()





