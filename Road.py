import matplotlib.pyplot as plt

class Road:
    def __init__(self):

        # Create Road
        fig, ax = plt.subplots()
        self.ax = ax
        self.fig = fig

        # Settings for Road
        ax.set_xlim(-1000, 1000)
        ax.set_ylim(-1000, 1000)
        ax.set_aspect('equal')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Differential Drive Chassis')

        

    def drawChassis(self, chassis):
        self.chassis = chassis
        wheels = chassis.getWheels()
        wheelr = (wheels[0]).getDrawPoint()
        wheell = (wheels[1]).getDrawPoint()

        self.ax.add_artist(wheelr)
        self.ax.add_artist(wheell)

        self.fig.canvas.draw()
        plt.pause(0.02)
    

    def showPlot(self):
        plt.show()