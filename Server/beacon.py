import numpy as np
class beacon:
    
    def __init__(self, uuid, pos_x, pos_y, center): 
        self.uuid = uuid
        self.rssi = [] #in meters
        self.distance = float(0)
        self.N = float(2.5)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.center = center

    
    def flush(self):
        temp = []
        self.rssi = temp

    def calc(self):
        self.distance = 10**((float(-50)-float(np.median(self.rssi)))/(10*self.N))

    def angle_check(self, angle):
        return (((self.center + 70) > angle) and ((self.center - 70) < angle))


        
    
