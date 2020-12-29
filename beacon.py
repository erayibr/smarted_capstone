class beacon:
    
    def __init__(self, uuid): 
        self.uuid = uuid
        self.count = 0
        self.distance = 0 #in meters


    def average(self):
        if(self.count > 0):
            self.distance = self.distance/self.count
        return(self.distance)
    
    def flush(self):
        self.distance = 0
        self.count = 0
        
    
