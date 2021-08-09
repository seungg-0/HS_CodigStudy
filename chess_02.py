from enum import Enum


class Color(Enum):
    BLACK = "b"
    WHITE = "w"


class PieceType(Enum):
    KING = "K"
    QUEEN = "Q"
    BISHOP = "B"
    KNIGHT = "N"
    ROOK = "R"
    PAWN = "P"





board_size = 8
board = []

def left(loc : tuple):
    return loc[0], loc[1] - 1


def right(loc):
    return loc[0], loc[1] + 1


def up(loc):
    return loc[0] - 1, loc[1]


def down(loc):
    return loc[0] + 1, loc[1]


def init_board():
    wk = Color.WHITE, PieceType.KING
    wq = Color.WHITE, PieceType.QUEEN
    wb1 = Color.WHITE, PieceType.BISHOP
    wb2 = Color.WHITE, PieceType.BISHOP
    wr1 = Color.WHITE, PieceType.ROOK
    wr2 = Color.WHITE, PieceType.ROOK
    wn1 = Color.WHITE, PieceType.KNIGHT
    wn2 = Color.WHITE, PieceType.KNIGHT
    bk = Color.BLACK, PieceType.KING
    bq = Color.BLACK, PieceType.QUEEN
    bb1 = Color.BLACK, PieceType.BISHOP
    bb2 = Color.BLACK, PieceType.BISHOP
    br1 = Color.BLACK, PieceType.ROOK
    br2 = Color.BLACK, PieceType.ROOK
    bn1 = Color.BLACK, PieceType.KNIGHT
    bn2 = Color.BLACK, PieceType.KNIGHT
    white_pawn = [Color.WHITE, PieceType.PAWN, False]
    wp_row = [white_pawn[:] for _ in range(board_size)]
    black_pawn = [Color.BLACK, PieceType.PAWN, False]
    bp_row = [black_pawn[:] for _ in range(board_size)]
    black_row = [br1, bn1, bb1, bk, bq, bb2, bn2, br2]
    white_row = [wr1, wn2, wb1, wk, wq, wb2, wn2, wr2]
    board.append(black_row)
    board.append(bp_row)
    for i in range(4):
        board.append([None] * board_size)

    board.append(wp_row)
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

def validate_input(turn, l1, l2):
    # location should be in board boundary
    if in_boundary(l1) is False or in_boundary(l2) is False:
        print("boundary error")
        print(l1 + ", " + l2)
        return False
    # remain same spot is false
    if l1 == l2:
        print("same spot error")
        return False

    cur_piece = get_val(l1)
    # empty spot
    if cur_piece is None:
        print("empty spot error")
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

def in_boundary(loc):
    return check_value(loc[0]) and check_value(loc[1])

def check_value(val):
    return 0 <= val < board_size

def get_val(loc):
    return board[loc[0]][loc[1]]



def reachable(l1, l2) -> bool:
    p = get_val(l1)
    ptype = p[1]
    if ptype == PieceType.QUEEN:
        return recursive_reachable(left(l1), l2, left) or \
                recursive_reachable(down(l1), l2, down) or \
                recursive_reachable(up(l1), l2, up) or \
                recursive_reachable(right(l1), l2, right) or \
                recursive_reachable(up(right(l1)), l2, composite_function(up, right)) or \
                recursive_reachable(up(left(l1)), l2, composite_function(up, left)) or \
                recursive_reachable(down(right(l1)), l2, composite_function(down, right)) or \
                recursive_reachable(down(left(l1)), l2, composite_function(down, left))
    elif ptype == PieceType.KING:
        return king_reachable(l1, l2)
    elif ptype == PieceType.BISHOP:
        return recursive_reachable(up(right(l1)), l2, composite_function(up, right)) or \
                recursive_reachable(up(left(l1)), l2, composite_function(up, left)) or \
                recursive_reachable(down(right(l1)), l2, composite_function(down, right)) or \
                recursive_reachable(down(left(l1)), l2, composite_function(down, left))
    elif ptype == PieceType.ROOK:
        return recursive_reachable(left(l1), l2, left) or \
               recursive_reachable(down(l1), l2, down) or \
               recursive_reachable(up(l1), l2, up) or \
               recursive_reachable(right(l1), l2, right)
    elif ptype == PieceType.KNIGHT:
        return knight_reachable(l1, l2)
    elif ptype == PieceType.PAWN:
        return pawn_reachable(l1, l2)
    else:
        return False

def pawn_reachable(cur, dest):
    def small_reachable(func):
        if func(left(cur)) == dest and get_val(dest) is not None:
            return True
        elif func(right(cur)) == dest and get_val(dest) is not None:
            return True
        elif func(cur) == dest:
            return True
        elif func(func(cur)) == dest:
            return get_val(func(cur)) is None and get_val(cur)[2] is False

        return False
    if get_val(cur)[0] == Color.WHITE:
        return small_reachable(up)
    else:
        return small_reachable(down)

def play(turn):
    # print in every turn
    print_board()
    my_input = input()
    if my_input[0] == 'q':
        return
    in1, in2 = my_input.split(' ')
    col1 = ord(in1[0]) - ord('a')
    row1 = int(in1[1]) - 1
    col2 = ord(in2[0]) - ord('a')
    row2 = int(in2[1]) - 1
    l1 = row1, col1
    l2 = row2, col2
    if validate_input(turn, l1, l2) is False:
        print("Invalid input. Please reinput command.")
    else:
        if process_move(l1, l2) is True:
            return

        turn += 1
    return play(turn)

def process_move(l1, l2):
    piece1 = get_val(l1)
    piece2 = get_val(l2)
    if piece2 is not None and piece2[1] == PieceType.KING:
        print(str(piece1[0]) + " wins!\n")
        return True

    if piece1[1] == PieceType.PAWN:
        piece1[2] = True

    board[l2[0]][l2[1]] = piece1
    board[l1[0]][l1[1]] = None
    return False

init_board()
play(1)