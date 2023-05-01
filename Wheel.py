from Point import Point
import matplotlib.pyplot as plt


class Wheel:

    def __init__(self, r, point, side):
        self.point = point
        self.r = r

        if side == 'r':
            color = "red"
        else:
            color = "green"
        self.drawPoint = plt.Circle((self.point.getX(), self.point.getY()), r*2, color=color)

    def setNewPoint(self, point):
        self.point = point

    def getDrawPoint(self):
        return self.drawPoint