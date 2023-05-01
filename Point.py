class Point:
    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y 

    def setX(self, x):
        self.x = x 

    def setY(self, y):
        self.y = y 

    def getX(self):
        return self.x

    def getY(self):
        return self.y


    def setPoint(self, newPoint):
        self.x = newPoint.getX() 
        self.y = newPoint.getY() 

    def __str__(self) -> str:
        return "x: " + str(self.x) + " y: " + str(self.y)

