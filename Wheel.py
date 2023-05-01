from Point import Point

class Wheel:

    def __init__(self, d):
        self.point = Point(0, 0)
        self.d = d
        self.V = 0

    def __init__(self, d, point):
        self.point = point
        self.d = d

    def setNewPoint(self, point):
        self.point = point
