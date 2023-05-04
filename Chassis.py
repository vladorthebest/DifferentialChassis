from Point import Point
from Wheel import Wheel
import matplotlib.pyplot as plt
import math 


class DifferentialChassis:

    def __init__(self, r, l, road):
        # Road
        self.road = road

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
        self.centerPoint = plt.Circle((self.T.getX(), self.T.getY()), r/2, color='black')

    def getWheels(self):
        return (self.wheelL, self.wheelR)

    def getDrawList(self):
        return (self.drawLine, self.centerPoint)

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
        # New X Y for Right
        x = self.T.getX() + (self.l/2) * math.sin(self.Angle)
        y = self.T.getY() + (self.l/2) * -math.cos(self.Angle)
        self.wheelR.setNewPoint(Point(x, y))
        
        # New X Y for Left
        x = self.T.getX() + (self.l/2) * -math.sin(self.Angle)
        y = self.T.getY() + (self.l/2) * math.cos(self.Angle)
        self.wheelL.setNewPoint(Point(x, y))


        self.drawLine.set_data(
            (self.wheelL.getPoint().getX(), self.wheelR.getPoint().getX()),
            (self.wheelL.getPoint().getY(), self.wheelR.getPoint().getY())
        )
        self.centerPoint.center =  (self.T.getX(), self.T.getY())


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
        self.road.drawChassis(self, dt)


    def way(self, way, avgSpeed=200):
        for type, value in way.items():
            if type == 'Line':
                self.wayLine(value, avgSpeed)


    def wayLine(self, value, avgSpeed):

        l = value[0]
        angl = value[1]

        t = l/avgSpeed
        td = 1
        tnow = 0
        while(tnow < t):
            self.newPosition(td, avgSpeed, avgSpeed)
            tnow += td
