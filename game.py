class matchup(object):
    def __init__(self, player1, player2):
            self.player1 = player1
            self.player2 = player2
            self.oneScore = 0 
            self.twoScore = 0
    def run(self):
        res1 = self.player1.makeMove(self.player2.last) 
        res2 = self.player2.makeMove(self.player1.last)
        #Both players defect
        if((res1+res2)==2):
            self.oneScore-=1
            self.twoScore-=1
        elif((res1+res2)==0):
            self.oneScore+=5
            self.twoScore+=5
        elif(res1==0):
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
