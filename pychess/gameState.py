import chess


class GameState:

    def __init__(self, fen):


        self.boardPlay = chess.Board(fen)

        self.colour = True if self.boardPlay.turn == chess.BLACK else False

    def make_move(self, move):
        self.boardPlay.push(move)

    def is_castling(self, move):
        return self.boardPlay.is_castling(move)

    def is_game_over(self):
        return self.boardPlay.is_game_over()
