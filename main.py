import attitudes
import game

print("Welcome! This is a game which illistrautes the concept of differnt game theory attitudes!\n")

# 0 = cooperate
# 1 = defect


# def alwaysCooperate(opp):
#     return 0



def playSelect(x,y):
    return {
        1 : alwaysCooperate(y),
        2 : alwaysDefect(y),
        3 : copyCat(y)
    }.get(x, 'default case') 

def printAttitudes():
    print("Attitude 1: Always Cooperate")
    print("Attitude 2: Always Defect")
    print("Attitude 3: Copycat")



#Always Cooperate



if __name__ == "__main__":
    jack = attitudes.alwaysCooperate("bot1")
    omr = attitudes.alwaysDefect("bot2")
    cat = attitudes.titForTat("bot3")
    i = 0
    game1 = game.matchup()
    while(i<5):
        i+=1
        # game1.run(jack.makeMove(omr.last), omr.makeMove(jack.last))
        game1.run(cat.makeMove(omr.last), omr.makeMove(cat.last))
        game1.printScore()

    
    
    # printAttitudes()
    # player1 =  playSelect(input("Select Attitude 1: "),-1)
    # player2 =  playSelect(input("Select Attitude 2: "),-1)
    # x = 0

    


#Intro Text
# print("1. Sandbox\n2. Auto\n")
# gameMode = input("Sandbox or Auto?: ")
# if(gameMode == 1):
#     print("Sandbox it is!")
# elif(gameMode == 2):
#     print("Auto. Here we go!")
# else:
#     print("Please select another one!")

