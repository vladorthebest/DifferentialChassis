import matplotlib.pyplot as plt

class Road:
    def __init__(self):
        fig, self.ax = plt.subplots()
        self.ax.set_xlim(-1.5, 1.5)
        self.ax.set_ylim(-1.5, 1.5)
        self.ax.set_aspect('equal')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_title('Differential Drive Chassis')

        plt.show()