class matchup(object):
    def __init__(self):
            self.oneScore = 0 
            self.twoScore = 0
    def run(self, player1, player2):
        #Both players defect
        if((player1+player2)==2):
            self.oneScore-=1
            self.twoScore-=1
        elif((player1+player2)==0):
            self.oneScore+=5
            self.twoScore+=5
        elif(player1==0):
            self.oneScore-=1
            self.twoScore+=3
        else:
            self.oneScore+=3
            self.twoScore-=1           
    

    def printScore(self):
        print("Player 1's Score: " + str(self.oneScore))
        print("Player 2's Score: " + str(self.twoScore))
        print("=======================================")
        return
