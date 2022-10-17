class player:
    # construct a player object and set turn value
    def __init__(self, turn):
        self.playerValue = turn

    # accesor method for turn value true or false
    def getTurn(self):
        return self.playerValue

    # change the turn value of the player
    def setTurn(self, turnVal):
        self.playerValue = turnVal


class gameboard:
    def __init__(self):
        self.r, self.c = (2, 7)
        self.GB = [[4] * self.c] * self.r
        self.GB[0, 0] = 0
        self.GB[1, 6] = 0
        self.col = 2
        self.row = 6
    def Move(self, pit):
        self.mvmnt = pit
        if (0 < pit < 7):
            row1 = True
            self.hBeans = self.GB[0, pit]
            for x in range(self.hBeans):
               if(self.mvmnt > 7)

                self.GB[0, pit]

        else:
            self.hBeans = self.GB[1, pit]
            row1 = False
        #print(" player", , "move at pit " + str(pit))




    def getGB(self)
        print(self.GB)







class game:
    self.p1
    def __init__(self, p1, p2, board1):
        self.player1 = p1
        self.player2 = p2
        self.gameBoard = board1

    def startGame(self, p1, p2, board1):
        x = 1
        while (x > 0):

            if p1.getTurn() == True:

                # call method to gameboard class
                pitO = int(input("enter value for player one: "))

                if board1.Move(pitO) == False:
                    p1.setTurn(False)
                else:
                    p1.setTurn(True)

            if p2.getTurn():

                # calls method to gameboard class

                pitT = int(input("enter value for player two:"))

                if board1.Move(pitT) == False:
                    p2.setTurn(False)
                else:
                    p2.setTurn(True)


p1 = player(True)
p2 = player(True)

boar1 = gameboard(10)

game1 = game(p1, p2, boar1)

game1.startGame(p1, p2, boar1)
