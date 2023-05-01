from Chassis import DifferentialChassis
from Road import Road


def main():
    chassis = DifferentialChassis(r=50, l=300)
    road = Road()
    road.drawChassis(chassis)
    print(chassis)
    road.showPlot()

if __name__ == "__main__":
   
    main()