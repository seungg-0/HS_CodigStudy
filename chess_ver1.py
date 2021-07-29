class Chess():
    def __init__(self):
        self.input_to_chessboard = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, '1': 7, '2': 6, '3': 5,'4': 4, '5': 3, '6': 2, '7': 1, '8': 0}

    def GameStart(self):
        print("Let's start !")
        self.chessboard = [["ㅁ"]*8 for _ in range(8)]
        self.chessboard[7][4] = "WK"
        self.chessboard[0][4] = "BK"

        #체스보드 2차원으로 출력
        i = 0
        while i < len(self.chessboard):  # 세로 크기
            j = 0
            while j < len(self.chessboard[i]):  # 가로 크기
                print(self.chessboard[i][j], end=' ')
                j += 1  # 가로 인덱스를 1 증가시킴
            print()
            i += 1  # 세로 인덱스를 1 증가시킴

        # BeforeMove is the variable that 'before move'
        self.BeforeMoveWhite = "e1"
        self.BeforeMoveBlack = "e8"
        self.PrintFirst()


    def PrintFirst(self):
        print("Which color starts first? (W or B)")
        self.start = input()
        self.SelectFirst()

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
        self.Wrow = self.WhiteInput[2]
        self.Wcolumn = self.WhiteInput[1]
        if self.Wrow == self.BeforeMoveBlack[1] and self.Wcolumn == self.BeforeMoveBlack[0]:
            print("White Win !!!")
            return 0
        else:
            self.WhitePrint()
        self.BlackInput = input()
        self.BlackMove()

    def BlackMove(self):
        self.Brow = self.BlackInput[2]
        self.Bcolumn = self.BlackInput[1]
        if self.Brow == self.BeforeMoveWhite[1] and self.Bcolumn == self.BeforeMoveWhite[0]:
            print("Black Win !!!")
            return 0
        else:
            self.BlackPrint()
        self.WhiteInput = input()
        self.WhiteMove()

    def WhitePrint(self):
        self.Brow = self.BeforeMoveBlack[1]
        self.Bcolumn = self.BeforeMoveBlack[0]
        self.chessboard = [["ㅁ"] * 8 for _ in range(8)]
        self.chessboard[self.input_to_chessboard[self.Wrow]][self.input_to_chessboard[self.Wcolumn]] = "WK"
        self.chessboard[self.input_to_chessboard[self.Brow]][self.input_to_chessboard[self.Bcolumn]] = "BK"

        #체스보드 2차원으로 출력
        i = 0
        while i < len(self.chessboard):  # 세로 크기
            j = 0
            while j < len(self.chessboard[i]):  # 가로 크기
                print(self.chessboard[i][j], end=' ')
                j += 1  # 가로 인덱스를 1 증가시킴
            print()
            i += 1  # 세로 인덱스를 1 증가시킴

        self.BeforeMoveWhite = self.Wcolumn + self.Wrow

    def BlackPrint(self):
        self.Wrow = self.BeforeMoveWhite[1]
        self.Wcolumn = self.BeforeMoveWhite[0]
        self.chessboard = [["ㅁ"] * 8 for _ in range(8)]
        self.chessboard[self.input_to_chessboard[self.Wrow]][self.input_to_chessboard[self.Wcolumn]] = "WK"
        self.chessboard[self.input_to_chessboard[self.Brow]][self.input_to_chessboard[self.Bcolumn]] = "BK"

        #체스보드 2차원으로 출력
        i = 0
        while i < len(self.chessboard):  # 세로 크기
            j = 0
            while j < len(self.chessboard[i]):  # 가로 크기
                print(self.chessboard[i][j], end=' ')
                j += 1  # 가로 인덱스를 1 증가시킴
            print()
            i += 1  # 세로 인덱스를 1 증가시킴

        self.BeforeMoveBlack = self.Bcolumn + self.Brow


run = Chess()
game = run.GameStart()


# 가장자리에 위치하는 경우 예외처리, 체크메이트 알림 기능 추가, 기보 기록하는 함수 작성
# king 말고 다른 말들 추가해서 기능 완성하기
