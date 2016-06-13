"""
Created on Thu May 19 10:18:42 2016

@author: Stijn Mast
"""

# This python script outputs the mission duration optimization approach

import numpy as np
import matplotlib.pyplot as plt

x = 7070./88775*360                  # Equation 5.4 of the report (x = Upsilon = 28.67 degrees)
n = 1330                             # Number of orbits required to map planet twice
r = np.array([0])                    # Dummy arrays and variables
s = np.array([])
d = 0     

for i in range(n):
    d = d+x
    if d>360:
        d = d-360
    else:
        d = d
    r = np.append(r,d)
r = np.sort(r)                       # r is now a sorted array which contains the longitudes of the equatorial crossings


r = r/360.*3385*2*np.pi              # Convert the longitudes to distances in kilometers on the equator of Mars


for j in range(n):                   # Obtain an array which contains the difference in kilometers between the equatorial crossings (which should be smaller than half the swath width to map the planet twice)
    k = r[j+1]-r[j]
    s = np.append(s,k)

z = 400.*np.tan(3.5*np.pi/180.)*2.   # z is the swath width
duration = n*(117.*60+50.)/3600./24. # Mission duration in days

print 'The number of orbits is',n,', with a mission duration of',duration,'days.'  # printing the results of the simulation
print 'The maximum distance between two equatorial crossings is',max(s),'km, which is smaller than half of the swath width, which is',z/2.,'km.'

