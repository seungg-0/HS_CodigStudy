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




def play(turn):
    # print in every turn
    print_board()
    return play(turn)



init_board()
play(1)