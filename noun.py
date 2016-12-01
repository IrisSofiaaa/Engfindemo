from case import Case

class Noun(Case):
    def __init__(self, rest, d, c, i):
        self.rest = rest
        self.d = d
        self.trans = ""
        self.case = c.case
        self.i = i
        
    def noun(self):
                noun = self.d.dictionary.get(self.i)
                
                try:
                    self.trans = noun[2]
                except IndexError:
                    self.trans = noun[0]
                except TypeError:
                    self.trans = "-"

                if self.rest[self.i] == "NNS":
                    if self.trans.endswith("hti"):
                        self.trans = self.trans[:2] + "det"
                    elif self.trans.endswith("ti"):
                        self.trans = self.trans[:-2] + "dit"
                    elif self.trans.endswith("us"):
                        self.trans = self.trans[:-1] + "kset"
                    elif self.trans.endswith("e"):
                        self.trans = self.trans + "et"
                    elif self.trans.endswith("kä"):
                        self.trans = self.trans[:-2] + "gät"
                    else:
                        self.trans = self.trans + "t"
                elif self.i == "Her" or self.i == "her":
                    self.trans = "hänen"
                elif self.i == "His" or self.i == "his":
                    self.trans = "hänen"
                elif self.i == "My" or self.i == "my":
                    self.trans = "minun"
                elif self.i == "Their" or self.i == "their":
                    self.trans = "heidän"
                elif self.i == "Our" or self.i == "our":
                    self.trans = "meidän"
                elif self.i == "Your" or self.i == "your":
                    self.trans = "sinun"
                else:
                    self.trans = self.trans + self.case
                    
   
