import numpy as np
import math
class beacon:
    
    def __init__(self, uuid, pos_x, pos_y, center, audio_file): 
        self.audio_file = audio_file
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
        if(math.isnan(self.distance)):
            self.distance = 7.5
        else:
            self.distance = min(self.distance, 7.5)

    def calc_default(self):
        return 10**((float(-50)-float(np.median(self.rssi)))/(10*self.N))

    def angle_check(self, angle):
        return (((self.center + 70) > angle) and ((self.center - 70) < angle))


        
    
