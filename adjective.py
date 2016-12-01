class Adjective:
    def __init__(self, d, i):
        self.trans = ""
        self.d = d
        self.i = i
        
    def adj(self):
        adjective = self.d.dictionary.get(self.i)
        try:
            self.trans = adjective[2]
        except IndexError:
            self.trans = adjective[0]
        except TypeError:
            self.trans = "-" 
        if self.i.endswith("est"):
            if self.trans.endswith("nen"):
                self.trans = self.trans[:-3] + "sin"
            else:
                self.trans = self.trans[:-1] + "in"
        else:
            self.trans = self.trans

