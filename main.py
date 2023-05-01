from Chassis import DifferentialChassis
from Road import Road


def main():
    chassis = DifferentialChassis(r=50, l=300)
    road = Road()
    t = [0, 5, 10, 15, 20, 25]
    Vl = [0, 200, -100, 100, 100]
    Vr = [0, 200, 200, 100, -200]
    tn = 0
    i = 0
    while(tn < t[-1]):
        chassis.newPosition(1, Vl[i], Vr[i])
        if t[i] == tn and i+1 < len(t)-1: 
            i+=1
        road.drawChassis(chassis)
        tn += 1
    
    
    
    
    road.showPlot()



if __name__ == "__main__":
   
    main()