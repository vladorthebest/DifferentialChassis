from Point import Point
import matplotlib.pyplot as plt


class Wheel:

    def __init__(self, r):
        self.point = Point(0, 0)
        self.r = r
        self.V = 0
        self.drawPoint = plt.Circle((self.point.getX(), self.point.getY()), r*2, color='black')

    def __init__(self, r, point):
        self.point = point
        self.r = r
        self.drawPoint = plt.Circle((self.point.getX(), self.point.getY()), r*2, color='black')

    def setNewPoint(self, point):
        self.point = point

    def getDrawPoint(self):
        return self.drawPoint
