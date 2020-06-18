import random

class Player:
    players = []
    colours = ["Red", "Yellow","Green", "Pink"]

    def __init__(self, name):
        self.name = name
        self.playerColour = ""
        col = random.choice(self.colours)
        Player.colours.remove(col)
        self.playerColour = col
        Player.players.append(self)

    def getName(self):
        return self.name

    def getPlayerColour(self):
        return self.playerColour

    def getCurrentPlayer(self):
        return Player.players[0].getName()

    def nextPlayer(self):
        p = Player.players.pop(0)
        Player.players.append(p)        
        return p

p1 = Player("Phil")
p2 = Player("Player 2")
p3 = Player("Player 3")
#p4 = Player("Player 4")

ask = input(":")
while ask != "q":
    print(p1.getCurrentPlayer())
    p1.nextPlayer()
    ask = input()



#for each in Player.players:
#    print(each.getName())
 #   print(each.getPlayerColour())
