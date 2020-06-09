class alwaysCooperate(object):
    def __init__(self, name):
        self.name = name 
        self.next = 0
        self.last = 0
    def makeMove(self, opp):
        #This logic is trivial for the attitudes that always make the same move
        #however this is the structure that should be 
        if(self.next == 1):
            self.next == opp
            self.last = 0
            return 0
        elif(self.next == 0):
            self.next == opp
            self.last = 0
            return 0


class alwaysDefect(object):
    def __init__(self, name):
        self.name = name
        self.last = 1
        self.next = 1
    def makeMove(self, opp):
        if(self.next == 1):
            self.next == opp
            self.last = 1
            return 1
        elif(self.next == 0):
            self.next == opp
            self.last = 1
            return 1

class copyCat(object):
    def __init__(self, name):
        self.name = name
        self.last =0
    def makeMove(self, opp):
        if(self.last == 1):
            self.last = opp
            return 1
        elif(self.last == 0):
            self.last = opp
            return 0