from enum import Enum
from typing import Tuple


class Color(Enum):
    def __str__(self):
        return self.value

    BLACK = "b"
    WHITE = "w"


class PieceType(Enum):
    def __str__(self):
        return self.value

    KING = "K"
    QUEEN = "Q"
    BISHOP = "B"
    KNIGHT = "N"
    ROOK = "R"
    PAWN = "P"


Piece = Tuple[Color, PieceType]

board_size = 8


def left(loc: tuple):
    return loc[0], loc[1] - 1


def right(loc):
    return loc[0], loc[1] + 1


def up(loc):
    return loc[0] - 1, loc[1]


def down(loc):
    return loc[0] + 1, loc[1]


board = []


def init_board():
    wk = Color.WHITE, PieceType.KING
    bk = Color.BLACK, PieceType.KING
    wq = Color.WHITE, PieceType.QUEEN
    bq = Color.BLACK, PieceType.QUEEN
    black_row = [bk, bq, None, None, None, None, None, None]
    white_row = [None, None, None, None, None, None, wq, wk]
    empty_row = [None] * 8
    board.append(black_row)
    for i in range(6):
        board.append(empty_row)
    board.append(white_row)


def print_board():
    for i in range(board_size):
        print(i + 1, end='\t')
        for j in range(board_size):
            p = board[i][j]
            if p is None:
                print('-', end='\t')
            else:
                print(str(p[0].value) + str(p[1].value), end='\t')
        print()
    colphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print("", end='\t')
    print(*colphabet, sep='\t')


init_board()
print_board()


def check_value(val):
    return 0 <= val < board_size


def in_boundary(loc: Tuple):
    print("in boundary func l = " + str(loc))
    return check_value(loc[0]) and check_value(loc[1])


def queen_reachable(cur, dest, func) -> bool:
    print("in queen_reachable, cur = " + str(cur))
    if cur == dest:
        return True
    if in_boundary(cur) is False or get_val(cur) is None:
        return False
    else:
        return queen_reachable(func(cur), dest, func)


def king_reachable(cur, dest):
    return abs(cur[0] - dest[1]) <= 1 and abs(cur.second - dest.second) <= 1


def get_val(loc: Tuple):
    val = board[loc[0]][loc[1]]
    if val is None:
        return None
    else:
        return val


def reachable(l1: Tuple, l2: Tuple) -> bool:
    p = get_val(l1)
    if p[1] == PieceType.QUEEN:
        return (queen_reachable(left(l1), l2, left) or
                queen_reachable(down(l1), l2, down) or
                queen_reachable(up(l1), l2, up) or
                queen_reachable(right(l1), l2, right) or
                queen_reachable(up(right(l1)), l2, up(right)) or
                queen_reachable(up(left(l1)), l2, up(left)) or
                queen_reachable(down(right(l1)), l2, down(right)) or
                queen_reachable(down(left(l1)), l2, down(left)))
    elif p[1] == PieceType.KING:
        return king_reachable(l1, l2)
    else:
        return False


def print_menu(turn):
    print("turn " + str(turn))
    print("press q to quit")
    print("input example : b1 h7")


# check if input is valid
# 1. l1 & l2 should be in boundary
# 2. turn & piece color should be matched.
def validate_input(turn, l1, l2):
    # location should be in board boundary
    if in_boundary(l1) is False or in_boundary(l2) is False:
        print("boundary error")
        print(l1 + ", " + l2)
        return False
    # remain same area is false
    if l1 == l2:
        print("same spot error")
        return False

    cur_piece = get_val(l1)
    # empty area
    if cur_piece is None:
        print("empty area error")
        return False
    # color error
    dest_piece = get_val(l2)
    if dest_piece is not None:
        if cur_piece[0] == dest_piece[0]:
            print("same color error")
            return False
    # even turn = black's turn
    if turn % 2 == 0:
        if cur_piece[0] == Color.WHITE:
            print("turn error")
            return False
        elif cur_piece[0] == Color.BLACK:
            # odd turn = white's turn
            print("turn error")
            return False
            # check if reachable
    if reachable(l1, l2) is False:
        print("unreachable error")
        return False

    return True


def process_move(l1, l2):
    print("process move")
    piece1 = get_val(l1)
    piece2 = get_val(l2)
    if piece2 is not None and piece2[1] == PieceType.KING:
        print(str(piece1[0]) + " wins!\n")
        return True

    board[l2[0]][l2[1]] = get_val(l1)
    board[l1[0]][l1[1]] = None
    return False


def play(turn):
    # print in every turn
    print_menu(turn)
    print_board()

    # input
    myinput = input()
    if myinput[0] == 'q':
        return
    in1, in2 = myinput.split(' ')
    print(in1)
    print(in2)
    col1 = ord(in1[0]) - ord('a')
    row1 = int(in1[1]) - 1
    col2 = ord(in2[0]) - ord('a')
    row2 = int(in2[1]) - 1
    l1 = row1, col1
    l2 = row2, col2
    print(l1, l2)
    if validate_input(turn, l1, l2) is False:
        print("Invalid input. Please reinput command.")
    else:
        if process_move(l1, l2) is True:
            return
        turn += 1
    return play(turn)


init_board()
play(1)
