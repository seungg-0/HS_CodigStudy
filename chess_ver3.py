from enum import Enum
input_to_chessboard = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, '1': 7, '2': 6, '3': 5,'4': 4, '5': 3, '6': 2, '7': 1, '8': 0}

class Color(Enum):
    WHITE = 'w'
    BLACK = 'b'

class PieceType(Enum):
    KING = 'k'
    QUEEN = 'q'
    BISHOP = 'b'

BOARDSIZE = 8
board = []
def Board():
    wk = Color.WHITE, PieceType.KING
    bk = Color.BLACK, PieceType.KING
    wq = Color.WHITE, PieceType.QUEEN
    bq = Color.BLACK, PieceType.QUEEN
    wb1 = Color.WHITE, PieceType.BISHOP
    wb2 = Color.WHITE, PieceType.BISHOP
    bb1 = Color.BLACK, PieceType.BISHOP
    bb2 = Color.BLACK, PieceType.BISHOP
    black_row = [8, None, None, bb1, bq, bk, bb2, None, None]
    white_row = [1, None, None, wb1, wq, wk, wb2, None, None]
    row_alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    board.append(black_row)
    for i in range(7, 1, -1):
        list = []
        list.append(i)
        for j in range(0, BOARDSIZE):
            list.append(None)
        board.append(list)
    board.append(white_row)
    board.append(row_alphabet)

def print_board():
    i = 0
    while i < len(board):  # 세로 크기
        j = 0
        while j < len(board):  # 가로 크기
            p = board[i][j]
            if p is None:
                print('-', end='\t')
            elif len(str(p)) == 1:
                print(str(p), end='\t')
            else:
                print(str(p[0].value) + str(p[1].value), end='\t')
            j += 1  # 가로 인덱스를 1 증가시킴
        print()
        i += 1  # 세로 인덱스를 1 증가시킴

def check_inboard(val): # 통과 : true
    return (1 <= input_to_chessboard[val[1]]) and (8 >= input_to_chessboard[val[1]]) and (7 >= input_to_chessboard[val[0]]) and (0 <= input_to_chessboard[val[0]])

def same_location(before, after): # 통과 : False
    return (input_to_chessboard[before[0]] == input_to_chessboard[after[0]]) and (input_to_chessboard[before[1]] == input_to_chessboard[after[1]])

def check_turn(before, turn): # 통과 : True
    if turn % 2 == 0: # 짝수 -> black turn
        before = board[input_to_chessboard[before[1]]][input_to_chessboard[before[0]]]
        return before[0].value == 'b'
    else:
        before = board[input_to_chessboard[before[1]]][input_to_chessboard[before[0]]]
        return before[0].value == 'w'

def king_reachable(before, after): # 통과 : True
    row_gap = abs(input_to_chessboard[before[0]] - input_to_chessboard[after[0]])
    col_gap = abs(input_to_chessboard[after[1]] - input_to_chessboard[after[1]])
    return row_gap <= 1 and col_gap <= 1

def queen_reachable(before, after): # 통과 : True
    return ((abs(input_to_chessboard[before[0]] - input_to_chessboard[after[0]]) >= 1) and (input_to_chessboard[before[1]] == input_to_chessboard[after[1]])) or \
            ((abs(input_to_chessboard[before[1]] - input_to_chessboard[after[1]]) >= 1) and (input_to_chessboard[before[0]] == input_to_chessboard[after[0]])) or \
           (abs(input_to_chessboard[before[0]] - input_to_chessboard[after[0]]) == abs(input_to_chessboard[before[1]] - input_to_chessboard[after[1]]))

def bishop_reachable(before, after): # 통과 : True
    return (abs(input_to_chessboard[before[0]] - input_to_chessboard[after[0]]) == abs(input_to_chessboard[before[1]] - input_to_chessboard[after[1]]))



def print_menu(turn):
    print("turn " + str(turn))
    print("press q to quit")
    print("input example : b1 h7")

def validate_input(turn, before, after):
    ptype = board[input_to_chessboard[before[1]]][input_to_chessboard[before[0]]]
    ptype = ptype[1].value
    if check_inboard(after) == False:
        print("move inside the chessboard.")
        return False
    elif same_location(before, after) == True:
        print("The after location must be different from the before location.")
        return False
    elif check_turn(before, turn) == False:
        print("turn error.")
        return False
    elif ptype == "k":
        if king_reachable(before, after) == False:
            return False
    elif ptype == "q":
        if queen_reachable(before, after) == False:
            return False
    elif ptype == "b":
        if bishop_reachable(before, after) == False:
            return False
    else:
        return True


def move(before, after):
    before_board = board[input_to_chessboard[before[1]]][input_to_chessboard[before[0]]]
    after_board = board[input_to_chessboard[after[1]]][input_to_chessboard[after[0]]]

    if after_board is not None and after_board[1].value == "k":
        print(before_board[0].value, "win~~~~!\n")
        return True

    board[input_to_chessboard[after[1]]][input_to_chessboard[after[0]]] = before_board
    board[input_to_chessboard[before[1]]][input_to_chessboard[before[0]]] = None
    return False



def play(turn):
    print_menu(turn)
    print_board()
    Input = input()

    if Input[0] == 'q':
        return False

    before, after = Input.split(" ")
    if validate_input(turn, before, after) == False:
        print("Invalid input. Please reinput command.")
    else:
        if move(before, after) == True:
            return
        turn += 1
    return play(turn)

Board()
play(1)
