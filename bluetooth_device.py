import numpy as np
class bluetooth_device:
    
    def __init__(self, addr): 
        self.addr = addr
        self.rssi = -200.000 #in dB
        self.distance = 100.000 #in meters
        self.power = -53.000 #expected RSSI at 1 meter
        self.N = 2.000 # environmental factor. Lower means better signal reception

    def set_strength(self, rssi):
        self.rssi = rssi
        self.set_distance()

    def set_distance(self):
        self.distance = np.float_power(10, ((self.power - self.rssi)/(10*self.N)))
    