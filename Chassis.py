from Point import Point
from Wheel import Wheel

class DifferentialChassis:

    def __init__(self, d, l):

        # Parameters
        self.l = l

        # Position
        self.T = Point(0, 0)

        # Wheel
        startL = Point(0, self.T.getY() - (l/2) )
        startR = Point(0, self.T.getY() + (l/2) )
        self.wheelR = Wheel(d, startL)
        self.wheelL = Wheel(d, startR)

        # Speed
        self.Wt = 0
        self.Vr = 0
        self.Vl = 0
        self.Vt = 0




