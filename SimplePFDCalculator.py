# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Very simple model to calculate the potential flight distance based on a saw model. Some time is spent for climbing with an average climbing rate, then depending on the speed some time is spent to go to the next lift in the workingBand. This is repeated until the day is finished.
# As i found, not a very clever idea: since the model expects that a lift is found after the working height is used, best performance is achieved when the working band is minimal. This is certainly not true since updrafts stand some distance away from eachother.

# <codecell>

from numpy import linspace  
from pylab import *

polar = lambda x: 1.32-0.016*x # linear polar based on two points (discus)
v = np.linspace(110,160) # km/h


def PFDCalc(averageLift):   # returns the potential flight distance depending on the velocity profile
                            # for an given average climbe rate 
    workingBand =  500.      # m
    flightTime = 6*60*60     # in s
    climbeTime = workingBand/averageLift # in s
    timeBetweenLift = workingHeight/abs(polar(v))
    distanceTolift = v*1/3.6*timeBetweenLift
    iterationTime = climbeTime + timeBetweenLift
    nIterations = flightTime/iterationTime
    totalDistance = distanceTolift*nIterations/1000
    return totalDistance

plot(v,PFDCalc(0.5),v,PFDCalc(1),v,PFDCalc(1.5),v,PFDCalc(2),v,PFDCalc(3))
xlabel('Speed Between Lift [km/h]')
ylabel('Potential Flight Distance [km]')
legend(["0.5m/s", "1.0m/s","1.5m/s","2.0m/s","3.0m/s"],loc=2)
grid()
show()

# <codecell>


# <codecell>


# <codecell>


