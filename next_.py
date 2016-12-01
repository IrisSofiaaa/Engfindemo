class Next():
    def __init__(self, sent, s1, s2, s3, s4, s5, s6):
        self.sent = sent
        self.strip1 = s1
        self.strip2 = s2
        self.strip3 = s3
        self.strip4 = s4
        self.strip5 = s5
        self.strip6 = s6
        self.next_ = ""
        
    def nextie(self):
        for i in self.sent.split():
                if i == self.strip6:
                    self.next_ = "None"
                elif i == self.strip5:
                    self.next_ = self.strip6
                elif i == self.strip4:
                    self.next_ = self.strip5
                elif i == self.strip3:
                    self.next_ = self.strip4
                elif i == self.strip2:
                    self.next_ = self.strip3
                else:
                    self.next_ = self.strip2
