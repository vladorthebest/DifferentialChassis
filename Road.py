import matplotlib.pyplot as plt

class Road:
    def __init__(self):
        self.MAX_X = 5 * 1000
        self.MAX_Y = 5 * 1000
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

        

    def drawChassis(self, chassis):
        self.chassis = chassis
        wheels = chassis.getWheels()
        wheelr = (wheels[0]).getDrawPoint()
        wheell = (wheels[1]).getDrawPoint()

        
        self.ax.add_artist(chassis.getDrawLine())
        self.ax.add_artist(wheelr)
        self.ax.add_artist(wheell)

        
        self.ax.set_xlim(-self.MAX_X, self.MAX_X)
        self.ax.set_ylim(-self.MAX_X, self.MAX_X)
        plt.draw()
        plt.pause(2)
        self.fig.canvas.draw()
    

    def showPlot(self):
        plt.show()