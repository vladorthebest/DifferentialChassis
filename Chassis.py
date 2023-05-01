from Point import Point
from Wheel import Wheel

class DifferentialChassis:

    def __init__(self, r, l):

        # Parameters
        self.l = l

        # Position
        self.T = Point(0, 0)

        # Wheel
        startL = Point(0, self.T.getY() - (l/2) )
        startR = Point(0, self.T.getY() + (l/2) )
        self.wheelR = Wheel(r, startL)
        self.wheelL = Wheel(r, startR)

        # Speed
        self.Wt = 0
        self.Vr = 0
        self.Vl = 0
        self.Vt = 0

    def getWheels(self):
        return (self.wheelL, self.wheelR)



