import matplotlib.pyplot as plt

class Road:
    def __init__(self):
        self.MAX_X = 2 * 1000
        self.MAX_Y = 2 * 1000
        # Create Road
        fig, ax = plt.subplots()
        self.ax = ax
        self.fig = fig

        # Settings for Road
        ax.set_xlim(-self.MAX_X, self.MAX_X)
        ax.set_ylim(-self.MAX_X, self.MAX_X)
        ax.set_aspect('equal')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Differential Drive Chassis')

        

    def drawChassis(self, chassis, t=1, clear=True):
        self.chassis = chassis
        wheels = chassis.getWheels()
        wheelr = (wheels[0]).getDrawPoint()
        wheell = (wheels[1]).getDrawPoint()

        for i in chassis.getDrawList():
            self.ax.add_artist(i)  
        self.ax.add_artist(wheelr)
        self.ax.add_artist(wheell)

        if(not clear):
            self.ax.scatter((wheels[0]).getPoint().getX(), (wheels[0]).getPoint().getY(), c='green')
            self.ax.scatter((wheels[1]).getPoint().getX(), (wheels[1]).getPoint().getY(), c='red')
            self.ax.scatter(chassis.getT().getX(), chassis.getT().getY(), c='black')


        self.ax.set_xlim(-self.MAX_X, self.MAX_X)
        self.ax.set_ylim(-self.MAX_Y, self.MAX_Y)
        plt.draw()
        plt.pause(t)
        self.fig.canvas.draw()
    

    def showPlot(self):
        plt.show()
    
    def setMaxX(self, arg):
        self.MAX_X = arg
    
    def setMaxY(self, arg):
        self.MAX_Y = arg