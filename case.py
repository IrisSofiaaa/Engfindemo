from person import Person

class Case(Person):
    def __init__(self, p):
        self.prev = p.prev
        self.case = ""
        self.casing()

    def casing(self):
        if self.prev == "in":
            self.case = "ssa"
        elif self.prev == "into":
            self.case = "iin"
        elif self.prev == "on":
            self.case = "lla"
        elif self.prev == "at":
            self.case = "lla"
        elif self.prev == "as":
            self.case = "na"
        elif self.prev == "of":
            self.case = "än"
        else:
            self.case = ""
