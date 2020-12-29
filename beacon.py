class beacon:
    
    def __init__(self, uuid): 
        self.uuid = uuid
        self.count = 0
        self.distance = 0 #in meters


    def average(self):
        self.distance = self.distance/self.count
