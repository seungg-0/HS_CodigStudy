class Chess():
    def __init__(self):
        self.input_to_chessboard = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, '1': 7, '2': 6, '3': 5,'4': 4, '5': 3, '6': 2, '7': 1, '8': 0}

    def GameStart(self):
        self.dead = []
        print("Let's start !")
        self.chessboard = [["ㅁ"]*8 for _ in range(8)]
        self.chessboard[7][4] = "WK"
        self.chessboard[0][4] = "BK"
        self.chessboard[7][3] = "WQ"
        self.chessboard[0][3] = "BQ"
        self.chessboard[7][2] = "WLB"
        self.chessboard[0][2] = "BLB"
        self.chessboard[7][5] = "WRB"
        self.chessboard[0][5] = "BRB"
        self.WKrow = 7
        self.WKcolumn = 4
        self.BKrow = 0
        self.BKcolumn = 4
        self.WQrow = 7
        self.WQcolumn = 3
        self.BQrow = 0
        self.BQcolumn = 3
        self.WLBrow = 7
        self.WLBcolumn = 2
        self.BLBrow = 0
        self.BLBcolumn = 2
        self.WRBrow = 7
        self.WRBcolumn = 5
        self.BRBrow = 0
        self.BRBcolumn = 5

        #체스보드 2차원으로 출력
        i = 0
        while i < len(self.chessboard):  # 세로 크기
            j = 0
            while j < len(self.chessboard[i]):  # 가로 크기
                print(self.chessboard[i][j], end=' ')
                j += 1  # 가로 인덱스를 1 증가시킴
            print()
            i += 1  # 세로 인덱스를 1 증가시킴

        self.PrintFirst()

    def PrintFirst(self):
        print("Which color starts first? (W or B)")
        self.start = input()
        self.SelectFirst()

    def SelectFirst(self):
        if self.start == "W" or self.start == "B":
            self.Move()
        else:
            print("Select only W or B")
            self.PrintFirst()
            self.SelectFirst()

    def Move(self):
        #화이트 start case
        if self.start == "W":
            while(True):
                #화이트 턴
                self.WhiteInput = input()
                if len(self.WhiteInput) == 3:
                    if self.WhiteInput[0] == "K":
                        self.MoveKing("W")

                    elif self.WhiteInput[0] == "Q":
                        self.MoveQueen("W")
                else:
                    if self.WhiteInput[1] == "B":
                        self.MoveBishop("W")
                #블랙 턴
                self.BlackInput = input()
                if len(self.BlackInput) == 3:
                    if self.BlackInput[0] == "K":
                        self.MoveKing("B")

                    elif self.BlackInput[0] == "Q":
                        self.MoveQueen("B")
                else:
                    if self.BlackInput[1] == "B":
                        self.MoveBishop("B")
        #블랙 start case
        else:
            while(True):
                #블랙 턴
                self.BlackInput = input()
                if len(self.BlackInput) == 3:
                    if self.BlackInput[0] == "K":
                        self.MoveKing("B")

                    elif self.BlackInput[0] == "Q":
                        self.MoveKing("B")
                else:
                    if self.BlackInput[1] == "B":
                        self.MoveBishop("B")
                #화이트 턴
                self.WhiteInput = input()
                if len(self.WhiteInput) == 3:
                    if self.WhiteInput[0] == "K":
                        self.MoveKing("W")

                    elif self.WhiteInput[0] == "Q":
                        self.MoveKing("W")
                else:
                    if self.WhiteInput[1] == "B":
                        self.MoveBishop("W")

    def MoveQueen(self, colorQ):
        #화이트 퀸 move
        if colorQ == "W":
            self.WQrow = self.input_to_chessboard[self.WhiteInput[2]]
            self.WQcolumn = self.input_to_chessboard[self.WhiteInput[1]]
            if self.WQrow == self.BKrow and self.WQcolumn == self.BKcolumn:
                print("White Win !!!")
                return 0
            elif self.WQrow == self.BQrow and self.WQcolumn == self.BQcolumn:
                self.dead.append("BQ")
            elif self.WQrow == self.BLBrow and self.WQcolumn == self.BLBcolumn:
                self.dead.append("BLB")
            elif self.WQrow == self.BRBrow and self.WQcolumn == self.BRBcolumn:
                self.dead.append("BRB")
            self.chessboard = [["ㅁ"] * 8 for _ in range(8)]
            self.chessboard[self.WKrow][self.WKcolumn] = "WK"
            self.chessboard[self.BKrow][self.BKcolumn] = "BK"
            self.chessboard[self.WQrow][self.WQcolumn] = "WQ"
            self.chessboard[self.BQrow][self.BQcolumn] = "BQ"
            self.chessboard[self.WLBrow][self.WLBcolumn] = "WLB"
            self.chessboard[self.BLBrow][self.BLBcolumn] = "BLB"
            self.chessboard[self.WRBrow][self.WRBcolumn] = "WRB"
            self.chessboard[self.BRBrow][self.BRBcolumn] = "BRB"

            # 죽은 말 제외시키기
            for k in range(0, len(self.dead)):
                for i in range(0, 8):
                    for j in range(0, 8):
                        if self.chessboard[i][j] == self.dead[k]:
                            self.chessboard[i][j] = "ㅁ"
            self.chessboard[self.WQrow][self.WQcolumn] = "WQ"

            # 체스보드 2차원으로 출력
            i = 0
            while i < len(self.chessboard):  # 세로 크기
                j = 0
                while j < len(self.chessboard[i]):  # 가로 크기
                    print(self.chessboard[i][j], end=' ')
                    j += 1  # 가로 인덱스를 1 증가시킴
                print()
                i += 1  # 세로 인덱스를 1 증가시킴


        #블랙 퀸 move
        else:
            self.BQrow = self.input_to_chessboard[self.BlackInput[2]]
            self.BQcolumn = self.input_to_chessboard[self.BlackInput[1]]
            if self.BQrow == self.WKrow and self.BQcolumn == self.WKcolumn:
                print("Black Win !!!")
                return 0
            elif self.BQrow == self.WQrow and self.BQcolumn == self.WQcolumn:
                self.dead.append("WQ")
            elif self.BQrow == self.WLBrow and self.BQcolumn == self.WLBcolumn:
                self.dead.append("WLB")
            elif self.BQrow == self.WRBrow and self.BQcolumn == self.WRBcolumn:
                self.dead.append("WRB")
            self.chessboard = [["ㅁ"] * 8 for _ in range(8)]
            self.chessboard[self.WKrow][self.WKcolumn] = "WK"
            self.chessboard[self.BKrow][self.BKcolumn] = "BK"
            self.chessboard[self.WQrow][self.WQcolumn] = "WQ"
            self.chessboard[self.BQrow][self.BQcolumn] = "BQ"
            self.chessboard[self.WLBrow][self.WLBcolumn] = "WLB"
            self.chessboard[self.BLBrow][self.BLBcolumn] = "BLB"
            self.chessboard[self.WRBrow][self.WRBcolumn] = "WRB"
            self.chessboard[self.BRBrow][self.BRBcolumn] = "BRB"

            # 죽은 말 제외시키기
            for k in range(0, len(self.dead)):
                for i in range(0, 8):
                    for j in range(0, 8):
                        if self.chessboard[i][j] == self.dead[k]:
                            self.chessboard[i][j] = "ㅁ"
            self.chessboard[self.BQrow][self.BQcolumn] = "BQ"

            # 체스보드 2차원으로 출력
            i = 0
            while i < len(self.chessboard):  # 세로 크기
                j = 0
                while j < len(self.chessboard[i]):  # 가로 크기
                    print(self.chessboard[i][j], end=' ')
                    j += 1  # 가로 인덱스를 1 증가시킴
                print()
                i += 1  # 세로 인덱스를 1 증가시킴



    def MoveKing(self, colorK):
        # 화이트 킹 move
        if colorK == "W":
            self.WKrow = self.input_to_chessboard[self.WhiteInput[2]]
            self.WKcolumn = self.input_to_chessboard[self.WhiteInput[1]]
            if self.WKrow == self.BKrow and self.WKcolumn == self.BKcolumn:
                print("White Win !!!")
                return 0
            elif self.WKrow == self.BQrow and self.WKcolumn == self.BQcolumn:
                self.dead.append("BQ")
            elif self.WKrow == self.BLBrow and self.WKcolumn == self.BLBcolumn:
                self.dead.append("BLB")
            elif self.WKrow == self.BRBrow and self.WKcolumn == self.BRBcolumn:
                self.dead.append("BRB")
            self.chessboard = [["ㅁ"] * 8 for _ in range(8)]
            self.chessboard[self.WKrow][self.WKcolumn] = "WK"
            self.chessboard[self.BKrow][self.BKcolumn] = "BK"
            self.chessboard[self.WQrow][self.WQcolumn] = "WQ"
            self.chessboard[self.BQrow][self.BQcolumn] = "BQ"
            self.chessboard[self.WLBrow][self.WLBcolumn] = "WLB"
            self.chessboard[self.BLBrow][self.BLBcolumn] = "BLB"
            self.chessboard[self.WRBrow][self.WRBcolumn] = "WRB"
            self.chessboard[self.BRBrow][self.BRBcolumn] = "BRB"

            # 죽은 말 제외시키기
            for k in range(0, len(self.dead)):
                for i in range(0, 8):
                    for j in range(0, 8):
                        if self.chessboard[i][j] == self.dead[k]:
                            self.chessboard[i][j] = "ㅁ"
            self.chessboard[self.WKrow][self.WKcolumn] = "WK"

            # 체스보드 2차원으로 출력
            i = 0
            while i < len(self.chessboard):  # 세로 크기
                j = 0
                while j < len(self.chessboard[i]):  # 가로 크기
                    print(self.chessboard[i][j], end=' ')
                    j += 1  # 가로 인덱스를 1 증가시킴
                print()
                i += 1  # 세로 인덱스를 1 증가시킴


        # 블랙 킹 move
        else:
            self.BKrow = self.input_to_chessboard[self.BlackInput[2]]
            self.BKcolumn = self.input_to_chessboard[self.BlackInput[1]]
            if self.BKrow == self.WKrow and self.BKcolumn == self.WKcolumn:
                print("Black Win !!!")
                return 0
            elif self.BKrow == self.WQrow and self.BKcolumn == self.WQcolumn:
                self.dead.append("WQ")
            elif self.BKrow == self.WLBrow and self.BKcolumn == self.WLBcolumn:
                self.dead.append("WLB")
            elif self.BKrow == self.WRBrow and self.BKcolumn == self.WRBcolumn:
                self.dead.append("WRB")
            self.chessboard = [["ㅁ"] * 8 for _ in range(8)]
            self.chessboard[self.WKrow][self.WKcolumn] = "WK"
            self.chessboard[self.BKrow][self.BKcolumn] = "BK"
            self.chessboard[self.WQrow][self.WQcolumn] = "WQ"
            self.chessboard[self.BQrow][self.BQcolumn] = "BQ"
            self.chessboard[self.WLBrow][self.WLBcolumn] = "WLB"
            self.chessboard[self.BLBrow][self.BLBcolumn] = "BLB"
            self.chessboard[self.WRBrow][self.WRBcolumn] = "WRB"
            self.chessboard[self.BRBrow][self.BRBcolumn] = "BRB"

            # 죽은 말 제외시키기
            for k in range(0, len(self.dead)):
                for i in range(0, 8):
                    for j in range(0, 8):
                        if self.chessboard[i][j] == self.dead[k]:
                            self.chessboard[i][j] = "ㅁ"
            self.chessboard[self.BKrow][self.BKcolumn] = "BK"

            # 체스보드 2차원으로 출력
            i = 0
            while i < len(self.chessboard):  # 세로 크기
                j = 0
                while j < len(self.chessboard[i]):  # 가로 크기
                    print(self.chessboard[i][j], end=' ')
                    j += 1  # 가로 인덱스를 1 증가시킴
                print()
                i += 1  # 세로 인덱스를 1 증가시킴


    def MoveBishop(self, colorB):
        # 화이트 비숍 move
        if colorB == "W":
            if self.WhiteInput[0] == "L":
                self.WLBrow = self.input_to_chessboard[self.WhiteInput[3]]
                self.WLBcolumn = self.input_to_chessboard[self.WhiteInput[2]]
                if self.WLBrow == self.BKrow and self.WLBcolumn == self.BKcolumn:
                    print("White Win !!!")
                    return 0
                elif self.WLBrow == self.BQrow and self.WLBcolumn == self.BQcolumn:
                    self.dead.append("BQ")
                elif self.WLBrow == self.BLBrow and self.WLBcolumn == self.BLBcolumn:
                    self.dead.append("BLB")
                elif self.WLBrow == self.BRBrow and self.WLBcolumn == self.BRBcolumn:
                    self.dead.append("BRB")
                self.chessboard = [["ㅁ"] * 8 for _ in range(8)]
                self.chessboard[self.WKrow][self.WKcolumn] = "WK"
                self.chessboard[self.BKrow][self.BKcolumn] = "BK"
                self.chessboard[self.WQrow][self.WQcolumn] = "WQ"
                self.chessboard[self.BQrow][self.BQcolumn] = "BQ"
                self.chessboard[self.WLBrow][self.WLBcolumn] = "WLB"
                self.chessboard[self.BLBrow][self.BLBcolumn] = "BLB"
                self.chessboard[self.WRBrow][self.WRBcolumn] = "WRB"
                self.chessboard[self.BRBrow][self.BRBcolumn] = "BRB"

                # 죽은 말 제외시키기
                for k in range(0, len(self.dead)):
                    for i in range(0, 8):
                        for j in range(0, 8):
                            if self.chessboard[i][j] == self.dead[k]:
                                self.chessboard[i][j] = "ㅁ"
                self.chessboard[self.WLBrow][self.WLBcolumn] = "WLB"

                # 체스보드 2차원으로 출력
                i = 0
                while i < len(self.chessboard):  # 세로 크기
                    j = 0
                    while j < len(self.chessboard[i]):  # 가로 크기
                        print(self.chessboard[i][j], end=' ')
                        j += 1  # 가로 인덱스를 1 증가시킴
                    print()
                    i += 1  # 세로 인덱스를 1 증가시킴

            else:
                self.WRBrow = self.input_to_chessboard[self.WhiteInput[3]]
                self.WRBcolumn = self.input_to_chessboard[self.WhiteInput[2]]
                if self.WRBrow == self.BKrow and self.WRBcolumn == self.BKcolumn:
                    print("White Win !!!")
                    return 0
                elif self.WRBrow == self.BQrow and self.WRBcolumn == self.BQcolumn:
                    self.dead.append("BQ")
                elif self.WRBrow == self.BLBrow and self.WRBcolumn == self.BLBcolumn:
                    self.dead.append("BLB")
                elif self.WRBrow == self.BRBrow and self.WRBcolumn == self.BRBcolumn:
                    self.dead.append("BRB")
                self.chessboard = [["ㅁ"] * 8 for _ in range(8)]
                self.chessboard[self.WKrow][self.WKcolumn] = "WK"
                self.chessboard[self.BKrow][self.BKcolumn] = "BK"
                self.chessboard[self.WQrow][self.WQcolumn] = "WQ"
                self.chessboard[self.BQrow][self.BQcolumn] = "BQ"
                self.chessboard[self.WLBrow][self.WLBcolumn] = "WLB"
                self.chessboard[self.BLBrow][self.BLBcolumn] = "BLB"
                self.chessboard[self.WRBrow][self.WRBcolumn] = "WRB"
                self.chessboard[self.BRBrow][self.BRBcolumn] = "BRB"

                # 죽은 말 제외시키기
                for k in range(0, len(self.dead)):
                    for i in range(0, 8):
                        for j in range(0, 8):
                            if self.chessboard[i][j] == self.dead[k]:
                                self.chessboard[i][j] = "ㅁ"
                self.chessboard[self.WRBrow][self.WRBcolumn] = "WRB"

                # 체스보드 2차원으로 출력
                i = 0
                while i < len(self.chessboard):  # 세로 크기
                    j = 0
                    while j < len(self.chessboard[i]):  # 가로 크기
                        print(self.chessboard[i][j], end=' ')
                        j += 1  # 가로 인덱스를 1 증가시킴
                    print()
                    i += 1  # 세로 인덱스를 1 증가시킴

        # 블랙 비숍 move
        else:
            if self.BlackInput[0] == "L":
                self.BLBrow = self.input_to_chessboard[self.BlackInput[3]]
                self.BLBcolumn = self.input_to_chessboard[self.BlackInput[2]]
                if self.BLBrow == self.WKrow and self.BLBcolumn == self.WKcolumn:
                    print("Black Win !!!")
                    return 0
                elif self.BLBrow == self.WQrow and self.BLBcolumn == self.WQcolumn:
                    self.dead.append("WQ")
                elif self.BLBrow == self.WLBrow and self.BLBcolumn == self.WLBcolumn:
                    self.dead.append("WLB")
                elif self.BLBrow == self.WRBrow and self.BLBcolumn == self.WRBcolumn:
                    self.dead.append("WRB")
                self.chessboard = [["ㅁ"] * 8 for _ in range(8)]
                self.chessboard[self.WKrow][self.WKcolumn] = "WK"
                self.chessboard[self.BKrow][self.BKcolumn] = "BK"
                self.chessboard[self.WQrow][self.WQcolumn] = "WQ"
                self.chessboard[self.BQrow][self.BQcolumn] = "BQ"
                self.chessboard[self.WLBrow][self.WLBcolumn] = "WLB"
                self.chessboard[self.BLBrow][self.BLBcolumn] = "BLB"
                self.chessboard[self.WRBrow][self.WRBcolumn] = "WRB"
                self.chessboard[self.BRBrow][self.BRBcolumn] = "BRB"

                # 죽은 말 제외시키기
                for k in range(0, len(self.dead)):
                    for i in range(0, 8):
                        for j in range(0, 8):
                            if self.chessboard[i][j] == self.dead[k]:
                                self.chessboard[i][j] = "ㅁ"
                self.chessboard[self.BLBrow][self.BLBcolumn] = "BLB"

                # 체스보드 2차원으로 출력
                i = 0
                while i < len(self.chessboard):  # 세로 크기
                    j = 0
                    while j < len(self.chessboard[i]):  # 가로 크기
                        print(self.chessboard[i][j], end=' ')
                        j += 1  # 가로 인덱스를 1 증가시킴
                    print()
                    i += 1  # 세로 인덱스를 1 증가시킴

            else:
                self.BRBrow = self.input_to_chessboard[self.BlackInput[3]]
                self.BRBcolumn = self.input_to_chessboard[self.BlackInput[2]]
                if self.BRBrow == self.WKrow and self.BRBcolumn == self.WKcolumn:
                    print("Black Win !!!")
                    return 0
                elif self.BRBrow == self.WQrow and self.BRBcolumn == self.WQcolumn:
                    self.dead.append("WQ")
                elif self.BRBrow == self.WLBrow and self.BRBcolumn == self.WLBcolumn:
                    self.dead.append("WLB")
                elif self.BRBrow == self.WRBrow and self.BRBcolumn == self.WRBcolumn:
                    self.dead.append("WRB")
                self.chessboard = [["ㅁ"] * 8 for _ in range(8)]
                self.chessboard[self.WKrow][self.WKcolumn] = "WK"
                self.chessboard[self.BKrow][self.BKcolumn] = "BK"
                self.chessboard[self.WQrow][self.WQcolumn] = "WQ"
                self.chessboard[self.BQrow][self.BQcolumn] = "BQ"
                self.chessboard[self.WLBrow][self.WLBcolumn] = "WLB"
                self.chessboard[self.BLBrow][self.BLBcolumn] = "BLB"
                self.chessboard[self.WRBrow][self.WRBcolumn] = "WRB"
                self.chessboard[self.BRBrow][self.BRBcolumn] = "BRB"

                # 죽은 말 제외시키기
                for k in range(0, len(self.dead)):
                    for i in range(0, 8):
                        for j in range(0, 8):
                            if self.chessboard[i][j] == self.dead[k]:
                                self.chessboard[i][j] = "ㅁ"
                self.chessboard[self.BRBrow][self.BRBcolumn] = "BRB"

                # 체스보드 2차원으로 출력
                i = 0
                while i < len(self.chessboard):  # 세로 크기
                    j = 0
                    while j < len(self.chessboard[i]):  # 가로 크기
                        print(self.chessboard[i][j], end=' ')
                        j += 1  # 가로 인덱스를 1 증가시킴
                    print()
                    i += 1  # 세로 인덱스를 1 증가시킴



run = Chess()
game = run.GameStart()


# 가장자리에 위치하는 경우 예외처리, 체크메이트 알림 기능 추가, 기보 기록하는 함수 작성
# king 말고 다른 말들 추가해서 기능 완성하기
