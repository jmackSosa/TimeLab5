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
        self.hBeans = self.GB[r][p]
        self.GB[r][p] = 0
        self.row = r
        self.pit = p + 1
        self.oRow = r

        if (self.oRow == 0):
            self.nRow = 1
            self.nGoal = 6
            self.goal = 0
        else:
            self.nRow = 0
            self.nGoal = 0
            self.goal = 6

        while self.hBeans > 0:
            if (self.row == 1):
                if (self.pit > 6):
                    self.row = 0
                    self.pit = 6
            else:
                if(self.pit == 0):
                    self.row = 1
                    self.pit = 0

            if self.row == self.oRow and self.hBeans == 1:
                if (self.pit == self.goal):
                    self.GB[self.row][self.goal] += 1
                    print(self.getGB())
                    return True
                elif (self.GB[self.row][self.pit] == 0):
                    self.GB[self.oRow][self.goal] += self.GB[self.row][self.pit] + self.GB[self.nRow][self.pit]
                    print(self.getGB())
                    return False


            elif self.row == self.nRow and self.pit == self.nGoal:
                continue
            else:
                self.GB[self.row][self.pit] += 1
                self.hBeans -= 1

            if (self.row == 1):
                self.pit += 1
            else:
                self.pit -= 1
        print(self.getGB)
        return False

    def getGB(self):
        for n in self.GB:
            print(n)



class game:
    def __init__(self, board1):
        self.gameBoard = board1

    def startGame(self, board1, p1 , p2):
        print(board1.getGB())
        while board1.getSum():
                self.goAgain = True
                while (self.goAgain):
                    pitO = int(input("enter pit value for player one: "))
                    rowO = int(input("enter row for player one:"))
                    self.goAgain = board1.Move(rowO, pitO)
                self.goAgain2 = True
                while (self.goAgain2):
                    pitT = int(input("enter pit value for player two:"))
                    rowT = int(input("enter row value for player two"))
                    self.goAgain2 = board1.Move(pitT , rowT)
                self.goAgain = True
                self.goAgain2 = True


boar1 = gameboard()
p1 = player(0)
p2 = player(0)
game1 = game(boar1)
game1.startGame(boar1, p1 , p2)


