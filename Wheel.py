from Point import Point
import matplotlib.pyplot as plt


class Wheel:

    def __init__(self, r, point, side):
        self.point = point
        self.r = r # mm 

        if side == 'r':
            color = "red"
        else:
            color = "green"
        self.color = color
        self.drawPoint = plt.Circle((self.point.getX(), self.point.getY()), r, color=color)

    def setNewPoint(self, point):
        self.point = point
        x = self.point.getX()
        y = self.point.getY()
        self.drawPoint.center =  (x, y)

    def getDrawPoint(self):
        return self.drawPoint

    def getPoint(self):
        return self.point