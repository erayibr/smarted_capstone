import numpy as np
class beacon:
    
    def __init__(self, uuid): 
        self.uuid = uuid
        self.rssi = [] #in meters
        self.distance = float(0)
        self.N = float(2)
    
    def flush(self):
        temp = []
        self.rssi = temp

    def calc(self):
        self.distance = 10**((float(-55)-float(np.median(self.rssi)))/(10*self.N))


        
    
