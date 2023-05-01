from Point import Point
from Wheel import Wheel
import matplotlib.pyplot as plt

class DifferentialChassis:

    def __init__(self, r, l):

        # Parameters
        self.l = l

        # Position
        self.T = Point(0, 0)

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

    def getWheels(self):
        return (self.wheelL, self.wheelR)

    def getDrawLine(self):
        return plt.Line2D(
            (self.startL.getX(), self.startR.getX()), 
            (self.startL.getY(), self.startR.getY()), 
            color='black'
        )


