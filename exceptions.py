class Exceptions():
    """ a class to handle all exceptions I found in the stories, mostly
    small fixes but they help a lot""" 
    def __init__(self, prev, next_, trans):
        self.prev = prev.prev
        self.next_ = next_.next_
        self.trans = trans
        self.exes()

    def exes(self):
        if self.next_ == "becomes":
            if self.trans.endswith("nen"):
                self.trans = self.trans[:-3] + "sesta"
            else:
                self.trans = self.trans[:-1] + "sta"
        elif self.next_.endswith("s"):
            if self.trans.endswith("nen"):
                self.trans = self.trans[:-3] + "set"
            else:
                self.trans = self.trans + "t"
        elif self.prev == "before" or self.prev == "more":
            if self.trans.endswith(("a", "i", "u", "o")):
                self.trans = self.trans + "a"
            elif self.trans.endswith("e"):
                self.trans = self.trans + "tta"
            elif self.trans.endswith(("ä", "ö", "y")):
                self.trans = self.trans + "ttä"
            elif self.trans.endswith(("l", "t")):
                self.trans = self.trans[:-2] + "iä"
            else:
                self.trans = self.trans
        elif self.prev.endswith(("1", "2","3", "4", "5", "6","7", "8", "9", "0")) or self.prev == "one" or self.prev == "two" or self.prev == "three" or self.prev.startswith("thirt")or self.prev.startswith("four") or self.prev.startswith("forty") or self.prev.startswith("five")or self.prev.startswith("fift") or self.prev.startswith("six") or self.prev.startswith("seven")or self.prev.startswith("eight") or self.prev.startswith("nine") or self.prev == "ten":
            """for numerals! sorry for the long code"""
            if self.trans.endswith(("a", "i", "u", "o")):
                self.trans = self.trans + "a"
            elif self.trans.endswith("e"):
                self.trans = self.trans + "tta"
            elif self.trans.endswith(("ä", "ö", "y")):
                self.trans = self.trans + "ttä"
            elif self.trans.endswith(("l", "t")):
                self.trans = self.trans[:-2] + "iä"
            elif self.trans.endswith("m"):
                self.trans = self.trans + "oa"
            else:
                self.trans = self.trans
        elif self.trans == "o":
            self.trans = "on"
        elif self.trans == "muuttunui":
            self.trans = "muutti"
        elif self.next_ == "better":
            self.trans = self.trans[:-1] + "sta"
        elif self.trans == "myydä":
            self.trans = "myydään"
        elif self.next_.endswith("s"):
            if self.trans.endswith("nen"):
                self.trans = self.trans[:-3] + "set"
            else:
                self.trans = self.trans + "t"
        elif self.next_ == "had":
            if self.trans == "minä" or self.trans == "sinä":
                self.trans = self.trans[:-1] + "ulla"
            else:
                self.trans = self.trans[:-1] + "ellä"
        else:
            self.trans = self.trans
        
         #These can be handy even with more data
