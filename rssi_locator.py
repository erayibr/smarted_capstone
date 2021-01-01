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
#from math import exp
#from numpy import linspace
from numpy import power

def locator(dist1, dist2, dist3,x1,x2,x3,y1,y2,y3):
    def equations(vars):
        x , y, z = vars
        eq1 = (x-x1)**2 + (y-y1)**2 - power(r1,2)
        eq2 = (x-x2)**2 + (y-y2)**2 - power(r2,2)
        eq3 = (x-x3)**2 + (y-y3)**2 - power(r3,2)
        return [eq1, eq2, eq3]
    #calculate distances btw beacons
    x=0;y=0
    centerTocenter1_2= ( (x1-x2)**2 + (y1-y2)**2 )**0.5
    centerTocenter1_3= ( (x1-x3)**2 + (y1-y3)**2 )**0.5
    centerTocenter2_3= ( (x2-x3)**2 + (y2-y3)**2 )**0.5
    
    # #get the unit direction vectors, normalize by dividing to centerTocenter
    # vector1_2= linspace(x2-x1,  y2-y1, 2)/centerTocenter1_2
    # vector1_3= linspace(x3-x1 , y3-y1, 2)/centerTocenter1_3
    # vector2_3= linspace(x3-x2 , y3-y2, 2)/centerTocenter2_3
    
    # #use the closest among beacons cords as center cord
    # centerdist=min(dist1,dist2,dist3)
    # if centerdist==dist1:
    #     xClose=x1
    #     yClose=y1
    # elif centerdist==dist2:
    #     xClose=x2
    #     yClose=y2
    # else:
    #     xClose=x3
    #     yClose=y3
    
    
    # #*********** CALCULATE CORDS OF 1st VERTEX ****************
    # #get the distance to add or substract from the radius(dist)
    # #note that it can be both negative or positive
    # lineLength=abs(centerTocenter1_2-dist1-dist2)/2
    # #get the coorinates of the first vertex of the triangle
    # # x,y = (center cords) + (unitvector)*scaling factor
    # d1=min(dist1,dist2)
    # if d1==dist1:
    #     x=x1
    #     y=y1
    # else:
    #     x=x2
    #     y=y2
    #     #reverse the direction of unit vector
    #     vector1_2=vector1_2*(-1)
    # if d1<1:
    #     lineLength=lineLength/2
    # tri_x1,tri_y1= [x,y] +vector1_2*(d1+lineLength)
    
    # #*********** CALCULATE CORDS OF 2nd VERTEX ****************
    # #get the distance to add or substract from the radius(dist)
    # #note that it can be both negative or positive
    # lineLength=abs(centerTocenter1_3-dist1-dist3)/2
    # #get the coorinates of the first vertex of the triangle
    # # x,y = (center cords) + (unitvector)*scaling factor
    # #use the closest among beacon 1 and beacon 3
    # d2=min(dist1,dist3)
    # if d2==dist1:
    #     x=x1
    #     y=y1
    # else:
    #     x=x3
    #     y=y3
    #     #reverse the direction of unit vector
    #     vector1_3=vector1_3*(-1)
    # if d2<1:
    #     lineLength=lineLength/2
    # tri_x2,tri_y2= [x,y] +vector1_3*(d2+lineLength)
    
    # #*********** CALCULATE CORDS OF 3rd VERTEX ****************
    # #get the distance to add or substract from the radius(dist)
    # #note that it can be both negative or positive
    # lineLength=abs(centerTocenter2_3-dist2-dist3)/2
    # # print(lineLength)
    # #get the coorinates of the first vertex of the triangle
    # # x,y = (center cords) + (unitvector)*scaling factor
    # d3=min(dist2,dist3)
    # if d2==dist2:
    #     x=x2
    #     y=y2
    # else:
    #     x=x3
    #     y=y3
    #     #reverse the direction of unit vector
    #     vector2_3=vector2_3*(-1)
    # if d2<1:
    #     lineLength=lineLength/2
    # tri_x3,tri_y3= [x,y] +vector2_3*(d3+lineLength)
    
    # #get the centeroid/center of mass coordinates,i.e devices location
    # centerCoef=0.25
    # if centerdist<0.6:
    #     centerCoef=10
    # elif centerdist>1.5:
    #     centerCoef=0
    # divisor=3 + centerCoef    
    # x_out =(tri_x1 + tri_x2 + tri_x3+xClose*centerCoef)/divisor
    # y_out =(tri_y1 + tri_y2 + tri_y3+yClose*centerCoef)/divisor
    # print (x_out,y_out)
    # """
    # UNCOMMENT THIS IF YOU WANT OUTPUTS FROM THE VECTOR SOLUTION
    
    # """
    # #return x_out,y_out
    
    #use three circles and solve with scipy.optimize.fsolve
    d=min(dist1,dist2,dist3)
    if d<2:
        if d==dist1:
            r1= dist1
            r2= (dist2/(dist1 + dist2))    *centerTocenter1_2
            r3= (dist3/(dist1 + dist3))    *centerTocenter1_3
        elif d==dist2:
            r1= (dist1/(dist1 + dist2))    *centerTocenter1_2
            r2= dist2
            r3= (dist3/(dist2 + dist3))    *centerTocenter2_3
        else:
            r1= (dist1/(dist1 + dist3))    *centerTocenter1_3
            r2= (dist2/(dist2 + dist3))    *centerTocenter2_3
            r3= dist3
    else:
        r1= dist1
        r2= dist2
        r3= dist3
    
    x, y, z =  fsolve(equations, (1, 1, 1))
    if x>3.9:
        x=3.9
    if y>3.4:
        y=3.4
    return abs(x),abs(y)
   