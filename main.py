class player:
    # construct a player object and set turn value
    def __init__(self, val ):
        self.val = val





class gameboard:
    def __init__(self):
        self.r, self.c = (2, 7)
        self.GB = [[4] * self.c] * self.r
        self.GB[0][6] = 0
        self.GB[1][6] = 0
        self.col = 2
        self.row = 6

        self.GB = [0, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 0]

    def getSum(self):
        total = 0
        for x in self.GB[0]:
            total += x
        for y in self.GB[1]:
            total += y
        if total >= 0:
            return True
        else:
            return False


    def altMove(self, r, p):
        inHand = self.GB[r][p]

        #count downfirst array, keep the x value the same and count up the second array, keep x vlaue same then-->
        #if player 2, place in last bin of array2, if player one place in first bin of array1








    def Move(self, r, p):





        self.goal = 6
        self.row = r
        self.oRow = r
        self.pit = p + 1
        self.hBeans = self.GB[r][p]

        while self.hBeans > 0:
            if (self.pit > 6):
                self.pit = 0
                if (self.row == 1):
                    self.row = 0
                else:
                    self.row = 1

            if (self.hBeans == 1):
                if (self.oRow == self.row):
                    if (self.pit == 6):
                        self.GB[self.row][self.pit] += 1
                        return True
                    elif (self.GB[self.row][self.pit] == 0):
                        self.GB[self.oRow][6] = self.GB[self.row][self.pit + 1]  # figure out which the other row is
                        return False
            else:
                if (0 <= self.pit < 6):
                    self.GB[self.row][self.pit] += 1

            self.hBeans -= 1
            self.pit += 1

        self.getGB()

    def getGB(self):
        for n in self.GB:
            print(n)



class game:
    def __init__(self, p1, p2, board1):
        self.player1 = p1
        self.player2 = p2
        self.gameBoard = board1

    def startGame(self, p1, p2, board1):

        while board1.getSum():

                pitO = int(input("enter another pit value for player one: "))
                rowO = int(input("enter another row for player one:"))
                while board1.Move(rowO , pitO):
                    pitO = int(input("enter another pit value for player one: "))
                    rowO = int(input("enter another row for player one:"))
                    board1.Move(rowO, pitO)


                pitT = int(input("enter pit value for player two:"))
                rowT = int(input("enter row value for player two"))
                while board1.Move(pitT, rowT):
                    pitT = int(input("enter pit value for player two:"))
                    rowT = int(input("enter row value for player two"))
                    board1.Move(pitT , rowT)



p1 = player(True)
p2 = player(True)

boar1 = gameboard()

game1 = game(p1, p2, boar1)
game1.startGame(p1, p2, boar1)


