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

        

    def drawChassis(self, chassis, t=1):
        self.chassis = chassis
        wheels = chassis.getWheels()
        wheelr = (wheels[0]).getDrawPoint()
        wheell = (wheels[1]).getDrawPoint()

        for i in chassis.getDrawList():
            self.ax.add_artist(i)
        self.ax.add_artist(wheelr)
        self.ax.add_artist(wheell)

        
        self.ax.set_xlim(-self.MAX_X, self.MAX_X)
        self.ax.set_ylim(-self.MAX_X, self.MAX_X)
        plt.draw()
        plt.pause(t)
        self.fig.canvas.draw()
    

    def showPlot(self):
        plt.show()