class player:
    # construct a player object and set turn value
    def __init__(self, val):
        self.val = val


class gameboard:
    def __init__(self):
        self.GB = [0, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 0]

    def getGB(self):
        for n in self.GB:
            print(n)

    def getSum(self):
        total = 0
        for x in range(1, 7):
            total += self.GB[0][x]
        for z in range(0, 6):
            total += self.GB[1][z]
        if total > 0:
            return True
        else:
            return False

    def altMove(self, r, p):
        inHand = self.GB[r][p]
        pitCoord = p
        rowCoord = r
        self.GB[r][p] = 0

        # this if player one's turn
        if (rowCoord == 0 and inHand > 0):

            while inHand > 0:
                # switch sides
                if (pitCoord == 0 and rowCoord == 0):
                    pitCoord == 0
                    rowCoord = 1
                    self.GB[1][0] += 1
                    inHand -= 1

                # if in player's row
                if (rowCoord == 0):
                    pitCoord -= 1
                    self.GB[0][pitCoord] += 1
                    inHand -= 1
                # if in other player's row
                if (rowCoord == 1):
                    pitCoord += 1
                    self.GB[1][pitCoord] += 1
                    inHand -= 1

                # if you get to their mancala
                if (rowCoord == 1 and pitCoord == 5):
                    rowCoord == 0
                    pitCoord == 6
                    self.GB[0][6] += 1
                    inHand -= 1

                # mancala extra turn
                if pitCoord == 0 and rowCoord == 0 and inHand == 0:
                    print("MANCALA PLAYER ONE GO AGAIN")
                    self.getGB()
                    return True
                    quit()

                # Stealing beans
                if (self.GB[0][pitCoord] == 1 and inHand == 0 and pitCoord != 0):
                    self.GB[0][0] += (1 + self.GB[1][pitCoord])
                    self.GB[0][pitCoord] = 0
                    self.GB[1][pitCoord] = 0
                    print("player one stole pieces")

            self.getGB()
            return False

        # this is if player two's turn
        if (rowCoord == 1 and inHand > 0):
            while inHand > 0:

                # if you reach the end of players two's side (bottom row)
                if (pitCoord == 6 and rowCoord == 1):
                    pitCoord == 6
                    rowCoord = 0
                    self.GB[0][6] += 1
                    inHand -= 1
                # if in player 2 row
                if (rowCoord == 1):
                    pitCoord += 1
                    self.GB[1][pitCoord] += 1
                    inHand -= 1
                # if in other player's row
                if (rowCoord == 0):
                    pitCoord -= 1
                    self.GB[0][pitCoord] += 1
                    inHand -= 1
                # if you approach their mancala
                if (rowCoord == 0 and pitCoord == 1):
                    rowCoord == 1
                    pitCoord == 0
                    self.GB[1][0] += 1
                    inHand -= 1
                # GETTING A MANCALA
                if (rowCoord == 1 and pitCoord == 6 and inHand == 0):
                    print("MANCALA PLAYER TWO GO AGAIN")
                    self.getGB()
                    return True
                    quit()

                # Stealing beans
                if (self.GB[1][pitCoord] == 1 and inHand == 0 and pitCoord != 6):
                    self.GB[1][6] += (1 + self.GB[0][pitCoord])
                    self.GB[1][pitCoord] = 0
                    self.GB[0][pitCoord] = 0
                    print("player two stole pieces")

            self.getGB()
            return False


class game:
    def __init__(self, board1):
        self.gameBoard = board1

    def startGame(self, board1, p1, p2):
        print(board1.getGB())
        if board1.getSum():
            print("There are  pieces on the board")
        else:
            print("There are no pieces on the board and ")
        while board1.getSum():

            goAgainO = True
            while goAgainO == True:
                playerOnePit = int(input("Enter pit for player one indexes (1-6)inclusive, top row:"))
                playerOneRow = int(input("Enter '0' if player one:"))
                goAgainO = board1.altMove(playerOneRow, playerOnePit)

            goAgainT = True
            while goAgainT == True:
                playertwoPit = int(input("Enter pit for player two indexes (0-5 inclusive bottom row):"))
                playertwoRow = int(input("Enter '1' if player two:"))
                goAgainT = board1.altMove(playertwoRow, playertwoPit)

        if board1.GB[0][0] > board1.GB[1][6]:
            print("Player one wins")
        else:
            print("Player two wins")


boar1 = gameboard()
p1 = player(0)
p2 = player(0)
game1 = game(boar1)
game1.startGame(boar1, p1, p2)

