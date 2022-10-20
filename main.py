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
        self.GB[0][6] = 0
        self.GB[1][6] = 0
        self.col = 2
        self.row = 6
    def Move(self, r, p):
        self.row = r
        self.oRow = r
        self.pit = p + 1
        self.hBeans = self.GB[r, p]


        while self.hbeans > 0:

            if (self.pit > 6):
                self.pit = 0
                if (self.row == 1):
                    self.row = 0
                else:
                    self.row = 1
            if (0 <= self.pit < 6):
                self.GB[self.row, self.pit] += 1


            else:
                if (self.row == self.oRow):
                    self.GB[self.row, self.pit] += 1

            self.hbeans -= 1



    def getGB(self):
        print(self.GB)




class game:
    def __init__(self, p1, p2, board1):
        self.player1 = p1
        self.player2 = p2
        self.gameBoard = board1

    def startGame(self, p1, p2, board1):
        x = 1
        while (x > 0):

            if p1.getTurn() :

                # call method to gameboard class
                pitO = int(input("enter pit value for player one: "))
                rowO = int(input("enter row for player one:"))


                if board1.Move(rowO , pitO) == False:
                    p1.setTurn(False)
                else:
                    p1.setTurn(True)

            if p2.getTurn():

                # calls method to gameboard class

                pitT = int(input("enter pit value for player two:"))
                rowT = int(input("enter row value for player two"))

                if board1.Move(rowT , pitT) == False:
                    p2.setTurn(False)
                else:
                    p2.setTurn(True)


p1 = player(True)
p2 = player(True)

boar1 = gameboard()

game1 = game(p1, p2, boar1)
game1.startGame(p1, p2, boar1)

print(boar1)
