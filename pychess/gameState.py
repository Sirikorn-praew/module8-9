import chess


class GameState:

    def __init__(self, fen):

        # if user_play:
        #     self.user_side = user_play

        self.boardPlay = chess.Board(fen)

        self.user_is_white = True
