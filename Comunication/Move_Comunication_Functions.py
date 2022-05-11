import chess
# from Comunication import Serial_Comunication_ISUS


list_name = {chess.KING: 1, chess.QUEEN: 2, chess.ROOK: 3,
             chess.KNIGHT: 3, chess.BISHOP: 3, chess.PAWN: 4}


def normally_move(from_square, to_square, piece):
    rowi = from_square[0]
    columni = int(from_square[1])
    rowf = to_square[0]
    columnf = int(to_square[1])
    ISUS_UART.Chess_Pick(
        rowi, columni, rowf, columnf, list_name[piece])


def castling_move(from_square, to_square):
    rowiK = from_square[0]
    columniK = int(from_square[1])
    rowfK = to_square[0]
    columnfK = int(to_square[1])
    if to_square == "c1":
        rowiR = "a"
        columniR = 1
        rowfR = "d"
        columnfR = 1
    elif to_square == "g1":
        rowiR = "h"
        columniR = 1
        rowfR = "f"
        columnfR = 1
    elif to_square == "c8":
        rowiR = "a"
        columniR = 8
        rowfR = "d"
        columnfR = 8
    elif to_square == "g8":
        rowiR = "h"
        columniR = 8
        rowfR = "f"
        columnfR = 8
    ISUS_UART.Chess_Pick(rowiK, columniK, rowfK, columnfK, 1)
    ISUS_UART.Uart_Read()
    ISUS_UART.Chess_Pick(rowiR, columniR, rowfR, columnfR, 3)


def promotion_move(from_square, to_square):
    rowi = from_square[0]
    columni = int(from_square[1])
    rowf = to_square[0]
    columnf = int(to_square[1])
    ISUS_UART.Chess_Pick(rowi, columni, rowf, columnf, 4)


def capture_move(from_square, to_square, piece_move, piece_captured):
    rowi = from_square[0]
    columni = int(from_square[1])
    rowf = to_square[0]
    columnf = int(to_square[1])
    ISUS_UART.Chess_Drop(
        rowf, columnf, list_name[piece_captured])
    ISUS_UART.Uart_Read()
    ISUS_UART.Chess_Pick(
        rowi, columni, rowf, columnf, list_name[piece_move])


def en_passant_move(from_square, to_square, turn):
    rowi = from_square[0]
    columni = int(from_square[1])
    rowf = to_square[0]
    columnf = int(to_square[1])
    if turn == chess.WHITE:
        ISUS_UART.Chess_Drop(rowf, columnf+1, 4)
    else:
        ISUS_UART.Chess_Drop(rowf, columnf-1, 4)
    ISUS_UART.Uart_Read()
    ISUS_UART.Chess_Pick(rowi, columni, rowf, columnf, 4)
