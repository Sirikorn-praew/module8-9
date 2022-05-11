import chess
from collections import deque
import setting_chess


class GameState:

    def __init__(self, fen):

        # if user_play:
        #     self.user_side = user_play

        self.boardPlay = chess.Board(fen)

        # self.colour = True if self.boardPlay.turn == chess.BLACK else False

        # self.user_is_white = True

        # Initialise stacks for undoing moves and detecting repetitions
        self.undo_info = deque()

    def colour(self):
        return True if self.boardPlay.turn == chess.BLACK else False

    def is_castling(self, move):
        return self.boardPlay.is_castling(move)

    def is_promotion(self, move):
        return True if move.promotion is not None else False

    def is_capture(self, move):
        return self.boardPlay.is_capture(move)

    def is_en_passant(self, move):
        return self.boardPlay.is_en_passant(move)

    def is_game_over(self):
        return self.boardPlay.is_game_over()

    def make_move(self, move):

        src_index = move.from_square
        dst_index = move.to_square

        src_piece = self.boardPlay.piece_at(src_index)
        captured = self.boardPlay.piece_at(dst_index)

        self.undo_info.append({'move': move,
                               'captured': captured})

        self.boardPlay.push(move)

    def undo_move(self):

        prev_state_info = self.undo_info.pop()

        move = prev_state_info['move']
        captured = prev_state_info['captured']

        self.boardPlay.pop()

    def move_to_san(self, move):
        # src_index = (move >> 6) & 0x3F
        # dst_index = move & 0x3F
        src_index = move.from_square
        dst_index = move.to_square

        # move_type = move & (0x3 << 14)
        # piece_type = self.squares[src_index] & 7
        piece = self.boardPlay.piece_at(src_index)
        pieceType = piece.piece_type

        is_capture = True if self.boardPlay.is_capture(move) else False
        is_promotion = True if move.promotion is not None else False
        is_castle = True if self.boardPlay.is_castling(move) else False

        if is_castle:
            if dst_index > src_index:  # Kingside
                return "0-0"
            else:  # Queenside
                return "0-0-0"

        san = ""
        if pieceType == chess.PAWN:
            if is_capture:
                san += chr(97 + (src_index & 7))
        else:
            san += str(piece)
        if is_capture:
            san += "x"
        san += chess.square_name(dst_index)

        if is_promotion:
            san += "="
            san += str(piece)

        if self.boardPlay.is_check():
            self.make_move(move)
            if self.boardPlay.is_checkmate():
                san += "#"
            else:
                san += "+"
            self.undo_move()
        return san
