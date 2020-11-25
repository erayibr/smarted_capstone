import bluetooth_device
from scipy.optimize import fsolve
from math import exp

def triangulate(device_1, device_2, device_3):
        
    def equations(vars):
        x , y, z = vars
        eq1 = (x-device_1.x)**2 + (y-device_1.y)**2 - device_1.distance**2
        eq2 = (x-device_2.x)**2 + (y-device_2.y)**2 - device_2.distance**2
        eq3 = (x-device_3.x)**2 + (y-device_3.y)**2 - device_3.distance**2
        return [eq1, eq2, eq3]

    x, y, z =  fsolve(equations, (1, 1, 1))

    print(x, y)
