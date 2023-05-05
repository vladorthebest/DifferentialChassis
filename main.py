from Chassis import DifferentialChassis
from Road import Road

def def1():
    road = Road()
    chassis = DifferentialChassis(r=50, l=300, road=road)
    # chassis.setClearRoad(False)
    t = [0, 5, 10, 15, 20, 25]
    Vl = [0, 200, -100, 100, 100]
    Vr = [0, 200, 200, 100, -200]
    timedelta = 1
    tn = 0
    i = 0
    while(tn < t[-1]):
        chassis.newPosition(timedelta, Vl[i], Vr[i])
        if i+1 < len(t)-1 and t[i+1] == tn: 
            i+=1
        tn += timedelta
    
    road.showPlot()

def def3():
    road = Road()
    road.setMaxX(2000)
    road.setMaxY(2000)
    chassis = DifferentialChassis(r=50, l=300, road=road)
    # chassis.setClearRoad(False)
    chassis.setDeltaT(0.5)
    
    way = []

    way.append(('Arc', 500, 90, 3))
    way.append(('Line', 500, 90, 6))
    way.append(('Arc', 500, -90, 3))
    chassis.way(way)
    road.showPlot()


def main():
    road = Road()
    road.setMaxX(2000)
    road.setMaxY(2000)
    chassis = DifferentialChassis(r=50, l=300, road=road)
    # chassis.setClearRoad(False)
    chassis.setDeltaT(0.5)
    
    way = []

    way.append(('Line', 1000, 0, 3))
    way.append(('Line', 1000, 90, 6))
    way.append(('Line', 1000, 180, 6))
    way.append(('Line', 1000, 270, 6))
    chassis.way(way)
    road.showPlot()


if __name__ == "__main__":
    def3()
    # main()






