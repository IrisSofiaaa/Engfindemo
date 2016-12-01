from prev import Prev
    
class Person(Prev):
    #looks at previous word to determine the person
    def __init__(self, p):
        self.prev = p.prev
        self.person = ""
        self.pers()
        
    def pers(self):
        if (self.prev == 'I'.lower() or self.prev == "I'm".lower() or 
               self.prev == 'me'):
            self.person = "1sg"
        elif (self.prev == 'You'.lower() or self.prev == "You're".lower() or 
               self.prev == 'Youre'.lower()):
            self.person = "2person"
        elif (self.prev == 'We'.lower() or self.prev == "We're".lower() or 
               self.prev == 'Were'.lower()):
            self.person = "1pl"
        elif (self.prev == 'They'.lower() or self.prev == "They're".lower() or 
               self.prev == 'Theyre'.lower()):
            self.person = "3pl"
        else:
            self.person = "3sg"

        





