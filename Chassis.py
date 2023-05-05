from Point import Point
from Wheel import Wheel
import matplotlib.pyplot as plt
import math 
import time


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


    def way(self, way):
        time.sleep(2)
        for value in way:
            if value[0] == 'Line':
                self.wayLine(value)
            elif value[0] == 'Arc':
                self.wayArc(value)


    def wayLine(self, value):
        td = 1
        self.newPosition(td, 0, 0)
        l = value[1]
        angle = value[2]
        t = value[3]
        
        if self.Angle != angle:
            t = t/2
            self.turn(angle, t, td)
        
        speed = l/t
        tnow = 0
        while(tnow < t):
            self.newPosition(td, speed, speed)
            tnow += td

    def turn(self, angle, t, dt):
        dangle = math.radians(angle) - self.Angle
        self.Wt = dangle / (t / dt)
        print(dangle)
        Vr = self.Wt * self.l / 2
        Vl = -1 * Vr

        tnow = 0
        while(tnow < t):
            self.newPosition(dt, Vl, Vr)
            tnow += dt

    def calc_wheel_speeds(self, R, angle, t):
        reversed = 1
        if angle < 0:
            reversed = -1
            angle = angle * (-1)
        # Вычисляем линейную скорость робота по дуге
        linear_velocity = R * math.radians(angle) / t

        # Вычисляем угловую скорость робота по дуге
        angular_velocity = math.radians(angle) / t

        # Вычисляем скорости левого и правого колес
        left_wheel_speed = (linear_velocity - 0.5 * angular_velocity * self.l * reversed)
        right_wheel_speed = (linear_velocity + 0.5 * angular_velocity * self.l * reversed)

        # Возвращаем скорости левого и правого колес в виде кортежа
        return left_wheel_speed, right_wheel_speed

    def wayArc(self, value):
        td = 0.1

        self.newPosition(td, 0, 0)
        r = value[1]
        # angle = math.radians(value[2] / 2)
        angle = value[2]
        time = value[3]

        Vl, Vr = self.calc_wheel_speeds(r, angle, time)

        tnow = 0
        while(tnow < time):
            self.newPosition(td, Vl, Vr)
            tnow += td



        
        
