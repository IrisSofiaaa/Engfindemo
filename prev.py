class Prev():
    def __init__(self, i, s1, s2, s3, s4, s5, s6):
        self.i = i
        self.strip1 = s1
        self.strip2 = s2
        self.strip3 = s3
        self.strip4 = s4
        self.strip5 = s5
        self.strip6 = s6
        self.prev = ""
        self.previous()
        
    def previous(self):
            if self.i == self.strip1:
                self.prev = "None"
            elif self.i == self.strip2:
                self.prev = self.strip1
            elif self.i == self.strip3:
                self.prev = self.strip2
            elif self.i == self.strip4:
                self.prev = self.strip3
            elif self.i == self.strip5:
                self.prev = self.strip4
            else:
                self.prev = self.strip5
            
