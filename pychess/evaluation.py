import chess

pieceValue = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

# Evaluating the board
pawnTable = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0]

knightTable = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]

bishopTable = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]

rookTable = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]

queenTable = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]

kingTable = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]

kingEndGameTable = [
    -50, -30, -30, -30, -30, -30, -30, -50,
    -30, -30,  0,  0,  0,  0, -30, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -20, -10,  0,  0, -10, -20, -30,
    -50, -40, -30, -20, -20, -30, -40, -50]


def moveValue(board, move, endgame):
    if move.promotion is not None:
        if board.turn == chess.BLACK:
            return -float("inf")
        else:
            return float("inf")

    piece = board.piece_at(move.from_square)
    if piece:
        from_value = evaluatePiece(piece, move.from_square, endgame)
        to_value = evaluatePiece(piece, move.to_square, endgame)
        position_change_value = to_value - from_value
    else:
        raise Exception(f"A piece was expected at {move.from_square}")

    capture_value = 0.0
    if board.is_capture(move):
        capture_value = evaluateCapture(board, move)

    move_value = capture_value + position_change_value
    if board.turn == chess.BLACK:
        move_value = -move_value

    return move_value


def evaluateCapture(board, move):
    if board.is_en_passant(move):
        return pieceValue[chess.PAWN]
    move_to = board.piece_at(move.to_square)
    move_from = board.piece_at(move.from_square)
    if move_to is None or move_from is None:
        raise Exception(
            f"Pieces were expected at _both_ {move.to_square} and {move.from_square}")
    return pieceValue[move_to.piece_type] - pieceValue[move_from.piece_type]


def evaluatePiece(piece, square, endgame):
    piece_type = piece.piece_type
    table = []
    if piece_type == chess.PAWN:
        table = pawnTable
    elif piece_type == chess.KNIGHT:
        table = knightTable
    elif piece_type == chess.BISHOP:
        table = bishopTable
    elif piece_type == chess.ROOK:
        table = rookTable
    elif piece_type == chess.QUEEN:
        table = queenTable
    elif piece_type == chess.KING:
        if endgame:
            table = kingEndGameTable
        else:
            table = kingTable
    if piece.color == chess.BLACK:
        table = list(reversed(table))

    return table[square]


def evaluateBoard(board):
    total = 0
    endgame = checkEndGame(board)

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue

        value = pieceValue[piece.piece_type] + \
            evaluatePiece(piece, square, endgame)
        if piece.color == chess.WHITE:
            total += value
        else:
            total -= value

    return total


def checkEndGame(board):
    queens = 0
    minors = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.piece_type == chess.QUEEN:
            queens += 1
        if piece and (piece.piece_type == chess.BISHOP or piece.piece_type == chess.KNIGHT):
            minors += 1

    if queens == 0 or (queens == 2 and minors <= 1):
        return True

    return False
