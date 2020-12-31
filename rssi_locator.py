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
#from scipy.optimize import fsolve
#from math import exp
from numpy import linspace
from sys import stderr

def locator(dist1, dist2, dist3,x1,x2,x3,y1,y2,y3):
    
    #calculate distances btw beacons
    x=0;y=0
    centerTocenter1_2= ( (x1-x2)**2 + (y1-y2)**2 )**0.5
    centerTocenter1_3= ( (x1-x3)**2 + (y1-y3)**2 )**0.5
    centerTocenter2_3= ( (x2-x3)**2 + (y2-y3)**2 )**0.5
    
    #get the unit direction vectors, normalize by dividing to centerTocenter
    vector1_2= linspace(x2-x1,  y2-y1, 2)/centerTocenter1_2
    vector1_3= linspace(x3-x1 , y3-y1, 2)/centerTocenter1_3
    vector2_3= linspace(x3-x2 , y3-y2, 2)/centerTocenter2_3
    
    #use the closest among beacons cords as center cord
    centerdist=min(dist1,dist2,dist3)
    if centerdist==dist1:
        xClose=x1
        yClose=y1
    elif centerdist==dist2:
        xClose=x2
        yClose=y2
    else:
        xClose=x3
        yClose=y3
    
    
    #*********** CALCULATE CORDS OF 1st VERTEX ****************
    #get the distance to add or substract from the radius(dist)
    #note that it can be both negative or positive
    lineLength=(centerTocenter1_2-dist1-dist2)/2
    #get the coorinates of the first vertex of the triangle
    # x,y = (center cords) + (unitvector)*scaling factor
    d1=min(dist1,dist2)
    
    tri_x1,tri_y1= [x,y] +vector1_2*(d1+lineLength)
    
    #*********** CALCULATE CORDS OF 2nd VERTEX ****************
    #get the distance to add or substract from the radius(dist)
    #note that it can be both negative or positive
    lineLength=(centerTocenter1_3-dist1-dist3)/2
    #get the coorinates of the first vertex of the triangle
    # x,y = (center cords) + (unitvector)*scaling factor
    #use the closest among beacon 1 and beacon 3
    d2=min(dist1,dist3)
    if d2==dist1:
        x=x1
        y=y1
    else:
        x=x3
        y=y3
    tri_x2,tri_y2= [x,y] +vector1_3*(d2+lineLength)
    
    #*********** CALCULATE CORDS OF 3rd VERTEX ****************
    #get the distance to add or substract from the radius(dist)
    #note that it can be both negative or positive
    lineLength=(centerTocenter2_3-dist2-dist3)/2
    # print(lineLength)
    #get the coorinates of the first vertex of the triangle
    # x,y = (center cords) + (unitvector)*scaling factor
    d3=min(dist2,dist3)
    if d2==dist2:
        x=x2
        y=y2
    else:
        x=x3
        y=y3
    tri_x3,tri_y3= [x,y] +vector2_3*(d3+lineLength)
    
    #get the centeroid/center of mass coordinates,i.e devices location
    x_out =(tri_x1 + tri_x2 + tri_x3+xClose*10)/13
    y_out =(tri_y1 + tri_y2 + tri_y3+yClose*10)/13
    return x_out,y_out
    
    #def equations(vars):
        #x , y, z = vars
        #eq1 = (x-device_1.x)**2 + (y-device_1.y)**2 - device_1.distance**2
        #eq2 = (x-device_2.x)**2 + (y-device_2.y)**2 - device_2.distance**2
        #eq3 = (x-device_3.x)**2 + (y-device_3.y)**2 - device_3.distance**2
        #return [eq1, eq2, eq3]

    #x, y, z =  fsolve(equations, (1, 1, 1))    
