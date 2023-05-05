from Chassis import DifferentialChassis
from Road import Road

def def1():
    road = Road()
    chassis = DifferentialChassis(r=50, l=300, road=road)
    
    tc = 1
    t = [0, 5, 10, 15, 20, 25]
    Vl = [0, 200, -100, 100, 100]
    Vr = [0, 200, 200, 100, -200]
    tn = 0
    i = 0
    while(tn < t[-1]):
        chassis.newPosition(tc, Vl[i], Vr[i])
        if i+1 < len(t)-1 and t[i+1] == tn: 
            i+=1
        tn += tc
    
    road.showPlot()


def main():
    road = Road()
    road.setMaxX(1500)
    road.setMaxY(3000)
    chassis = DifferentialChassis(r=50, l=300, road=road)
    chassis.setClearRoad(False)
    chassis.setDeltaT(0.5)
    
    way = []

    way.append(('Arc', 500, 90, 5))
    way.append(('Line', 500, 90, 5))
    way.append(('Arc', 500, -90, 5))
    
    chassis.way(way)
    road.showPlot()


if __name__ == "__main__":
    # def1()
    main()






