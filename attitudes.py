# Cooperates unconditionally 
class alwaysCooperate(object):
    def __init__(self, name):
        self.name = name 
        self.last = 0
    def makeMove(self, opp):
        return 0

# Defects unconditionally
class alwaysDefect(object):
    def __init__(self, name):
        self.name = name
        self.last = 1
    def makeMove(self, opp):
        return 1

# Starts by cooperating, then will copy opponents last move
class titForTat(object):
    def __init__(self, name):
        self.name = name
        self.last = 0
    def makeMove(self, opp):
        if(self.last == 0):
            self.last = opp
            return 0
        elif(self.last == 1):
            self.last = opp
            return 1

# Starts by defecting, then will copy opponents last move
class suspiciousTitForTat(object):
    def __init__(self, name):
        self.name = name
        self.last = 1
    def makeMove(self, opp):
        if(self.last == 0):
            self.last = opp
            return 0
        elif(self.last == 1):
            self.last = opp
            return 1

# Will cooperate until opponent defects. Then will defect forever
class grimTrigger(object):
    def __init__(self, name):
        self.name = name
        self.last = 0
    def makeMove(self, opp):
        if(self.last == 0):
            self.last = opp
            return 0
        elif(self.last == 1):
            self.last = 1
            return 1

# Starts by defecting, then will copy opponents last move
class titForTwoTats(object):
    def __init__(self, name):
        self.name = name
        self.last = 1
    def makeMove(self, opp):
        if(self.last == 0):
            self.last = opp
            return 0
        elif(self.last == 1):
            self.last = opp
            return 1