# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 03:58:05 2020

@author: Furkan
"""
"""
SMARTED 2020
locator function
gets RSSI outputs as distance (all in any typical unit)
gets the 2-D coordinates of three beacons (all in any typical unit)
returns the location of the device in 2-D cords (in the same unit as inputs)
"""
from scipy.optimize import fsolve
#numpy calls C code, used for optimization
from numpy import power



def locator(dist1, dist2, dist3,x1,x2,x3,y1,y2,y3):
    def equations(vars):
        x , y, z = vars
        eq1 = power((x-x1) ,2) + power((y-y1) ,2) - power(r1,2)
        eq2 = power((x-x2) ,2) + power((y-y2) ,2) - power(r2,2)
        eq3 = power((x-x3) ,2) + power((y-y3) ,2) - power(r3,2)
        return [eq1, eq2, eq3]
    #calculate distances btw beacons
    # x=0;y=0
    centerTocenter1_2= ( (x1-x2)**2 + (y1-y2)**2 )**0.5
    centerTocenter1_3= ( (x1-x3)**2 + (y1-y3)**2 )**0.5
    centerTocenter2_3= ( (x2-x3)**2 + (y2-y3)**2 )**0.5
    
    #use three circles and solve with scipy.optimize.fsolve
    d=min(dist1,dist2,dist3)
    
    if d>1.5:
        r1= dist1
        r2= dist2
        r3= dist3
    else:
        if d==dist1:
            r1= dist1
            r2= (dist2/(dist1 + dist2))    *centerTocenter1_2
            r3= (dist3/(dist1 + dist3))    *centerTocenter1_3
        elif d==dist2:
            r1= (dist1/(dist1 + dist2))    *centerTocenter1_2
            r2= dist1
            r3= (dist3/(dist2 + dist3))    *centerTocenter2_3
        else:
            r1= (dist1/(dist1 + dist3))    *centerTocenter1_3
            r2= (dist2/(dist2 + dist3))    *centerTocenter2_3
            r3= dist3
    
    r1= dist1
    r2= dist2
    r3= dist3
    
    x, y, z =  fsolve(equations, (1, 1, 1))
    
    if x>4:
        x=4
    if y>3.5:
        y=3.5
    
    return abs(x),abs(y)
   