import numpy as np
class beacon:
    
    def __init__(self, uuid, pos_x, pos_y): 
        self.uuid = uuid
        self.rssi = [] #in meters
        self.distance = float(0)
        self.N = float(2.5)
        self.pos_x = pos_x
        self.pos_y = pos_y

    
    def flush(self):
        temp = []
        self.rssi = temp

    def calc(self):
        self.distance = 10**((float(-50)-float(np.median(self.rssi)))/(10*self.N))



        
    
