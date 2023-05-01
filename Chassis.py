from Point import Point
from Wheel import Wheel
import matplotlib.pyplot as plt
import math 


class DifferentialChassis:

    def __init__(self, r, l):

        # Parameters
        self.l = l #mm

        # Position
        self.T = Point(0, 0)
        self.Angle = 0

        # Wheel
        self.startL = Point(0, self.T.getY() - (l/2) )
        self.startR = Point(0, self.T.getY() + (l/2) )
        self.wheelR = Wheel(r, self.startL, 'r')
        self.wheelL = Wheel(r, self.startR, 'l')

        # Speed
        self.Wt = 0
        self.Vr = 0
        self.Vl = 0
        self.Vt = 0

        # Draw
        self.drawLine = plt.Line2D(
            (self.wheelL.getPoint().getX(), self.wheelR.getPoint().getX(),),
            (self.wheelL.getPoint().getY(), self.wheelR.getPoint().getY(),),
            color='black'
        )

    def getWheels(self):
        return (self.wheelL, self.wheelR)

    def getDrawLine(self):
        return self.drawLine

    def updateVt(self):
        self.Vt = (self.Vr + self.Vl)/2
    
    def updateWt(self):
        self.Wt = (self.Vr - self.Vl)/self.l

    def updateVWt(self):
        self.updateVt()
        self.updateWt()

    def updateAngle(self, dt):
        dAngle = self.Wt * dt
        self.Angle = self.Angle + dAngle

    def updateWheels(self):
        self.wheelR.setNewPoint(Point(self.T.getX(), self.T.getY() + (self.l/2)))
        self.wheelL.setNewPoint(Point(self.T.getX(), self.T.getY() - (self.l/2)))
        self.drawLine.set_data(
            (self.wheelL.getPoint().getX(), self.wheelR.getPoint().getX()),
            (self.wheelL.getPoint().getY(), self.wheelR.getPoint().getY())
        )


    def newPosition(self, dt, Vl, Vr):
        self.Vr = Vr 
        self.Vl = Vl
        self.updateVWt()
        self.updateAngle(dt)


        print(self.Angle)
        Vx = self.Vt * math.cos(self.Angle)
        Vy = self.Vt * math.sin(self.Angle)

        Xt = Vx*dt + self.T.getX()
        Yt = Vy*dt + self.T.getY()
        self.T.setX(Xt)
        self.T.setY(Yt)
        self.updateWheels()
        print(self.T)



