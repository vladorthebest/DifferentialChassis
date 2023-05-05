from Chassis import DifferentialChassis
from Road import Road
from collections import OrderedDict
import math

def def1():
    road = Road()
    chassis = DifferentialChassis(r=50, l=300, road=road)
    
    tc = 1
    # t = [0, 5, 10, 15, 20, 25]
    # Vl = [0, 200, -100, 100, 100]
    # Vr = [0, 200, 200, 100, -200]
    t = [0, 10]
    Vl = [100, 200]
    Vr = [100, 200]
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
    chassis = DifferentialChassis(r=50, l=300, road=road)
    way = []
    way.append(('Arc', 500, 90, 10))
    way.append(('Line', 200, 0, 10))
    way.append(('Arc', 500, -90, 10))
    
    chassis.way(way)


if __name__ == "__main__":
    # def1()
    main()






