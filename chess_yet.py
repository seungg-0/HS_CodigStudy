class Chess():
    input_to_chessboard = {'a':0, 'b':1, 'c': 2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, '1':7, '2':6, '3':5, '4':4, '5':3, '6':2, '7':1, '8':0}
    def __init__(self):
        print("Let's start !")
        self.chessboard = [["ㅁ"]*8 for _ in range(8)]
        self.chessboard[8][4] = "WK"
        self.chessboard[0][4] = "BK"
        print(self.chessboard)
        # BeforeMove is the variable that 'before move'
        self.BeforeMoveWhite = "e1"
        self.BeforeMoveBlack = "e8"
        self.PrintFirst()
        self.SelectFirst()

    def PrintFirst(self):
        print("Which color starts first? (W or B)")
        self.start = input()

    def SelectFirst(self):
        if self.start == "W":
            self.PlayWhiteFirst()
        elif self.start == "B":
            self.PlayBlackFirst()
        else:
            print("Select only W or B")
            self.PrintFirst()
            self.SelectFirst()

    def PlayWhiteFirst(self):
        self.WhiteInput = input()
        self.BeforeMoveWhite = self.WhiteInput[1:3]
        self.WhiteMove()

    def PlayBlackFirst(self):
        self.BlackInput = input()
        self.BeforeMoveBlack = self.BlackInput[1:3]
        self.BlackMove()

    def WhiteMove(self):
        if self.WhiteInput[1] == self.beforeMoveWhite[0]:
            if int(self.WhiteInput[2]) == 1:
                self.MoveUp()
            elif int(self.WhiteInput[2]) == 8:
                self.MoveDown()
            if int(self.WhieInput[2]) == (int(self.beforeMoveWhite[1]) - 1):
        elif self.WihteInput[1] == self.beforeMoveWhite[0] - 1

    def BlackMove(self):

    def MoveUp(self):

    def MoveDown(self):

    def MoveLeft(self):

    def MoveRight(self):

    def MoveLeftUp(self):

    def MoveRightUp(self):

    def MoveLeftDown(self):

    def MoveRightDow(self):
