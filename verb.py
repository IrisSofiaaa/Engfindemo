from person import Person

class Verb(Person):
    def __init__(self, rest, d, p, i):
        self.rest = rest
        self.d = d
        self.trans = ""
        self.person = p.person
        self.i = i
        
    def verb(self):
        """applies grammar to words with the a tag that starts with VB"""
        verb = self.d.dictionary.get(self.i)
        
        try:
            self.trans = verb[2]
        except IndexError:
            self.trans = verb[0]
        except TypeError:
            self.trans = "- "
        
        if self.rest[self.i] == "VBZ" or self.rest[self.i] == "VBP" or self.rest[self.i] == "VBN":
            #for verbs in present tense
            if self.trans.endswith(("nä", "la")):
                if self.person == "3sg":
                    self.trans = self.trans
                else:
                    self.trans = self.trans[:-2] + "e"
            elif self.trans.endswith("ta"):
                self.trans = self.trans[:-2] + "a"
            elif self.trans.endswith(("da", "dä")):
                if self.person == "3sg":
                    self.trans = self.trans
                else:
                    self.trans = self.trans[:-2]
            elif self.trans.endswith(("iä", "ia")):
                if self.person == "3sg":
                    self.trans = self.trans[:-1] + "i"
                else:
                    self.trans = self.trans[:-1]
            elif self.trans.endswith(("ttaa", "ttua", "ttää", "ttyä")):
                if self.person == "3sg":
                    self.trans = self.trans
                else:
                    self.trans = self.trans[:-3]
            elif self.trans.endswith(("data", "dota")):
                if self.person == "3sg":
                    self.trans = self.trans
                else:
                    self.trans = self.trans[:-4] + "ta"
            elif self.trans.endswith("ötyä"):
                if self.person == "3sg":
                    self.trans = self.trans
                else:
                    self.trans = self.trans[:-3] + "dy"
            elif self.trans.endswith(("ttu", "ton", "tty")):
                self.trans = self.trans
            else:
                self.trans = self.trans[:-1]

        elif self.rest[self.i] == "VBD":
            #for verbs in past tense
            if self.trans.endswith(("nä", "la", "laa", "taa", "tää", "lla", "llä")):
                self.trans = self.trans[:-2] + "i"
            elif self.trans.endswith("ta"):
                self.trans = self.trans[:-2] + "si"
            elif self.trans.endswith(("uoda")):
                self.trans = self.trans[:-4] + "oi"
            elif self.trans.endswith(("yödä")):
                self.trans = self.trans[:-4] + "öi"
            elif self.trans.endswith(("hdä")):
                self.trans = self.trans[:-3] + "i"
            elif self.trans.endswith(("da")):
                self.trans = self.trans[:-2]
            elif self.trans.endswith(("iä", "ia")):
                self.trans = self.trans[:-1]
            elif self.trans.endswith(("ttaa", "ttua", "ttää", "ttyä")):
                self.trans = self.trans[:-3] + "i"
            elif self.trans.endswith(("data", "dota")):
                self.trans = self.trans[:-4]+"tasi"
            elif self.trans.endswith(("ttu", "ton", "tty")):
                self.trans = self.trans
            else:
                self.trans = self.trans[:-1] + "i"
            
    def pers(self):

        if self.person == "1sg":
            self.trans = self.trans + "n"
        elif self.person == "1pl":
            self.trans = self.trans + "mme"
        elif self.person == "2person":
            self.trans = self.trans + "t"
        elif self.person == "3pl":
            self.trans = self.trans + "vat"
        elif self.person == "3sg":
            self.trans = self.trans
        elif self.person == "3sg" and self.trans == "ole":
            self.trans = "on"
        else:
            self.trans = self.trans
