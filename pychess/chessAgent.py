import multiprocessing
import chess
import chess.polyglot
import os
import time
from multiprocessing import Pool
from itertools import repeat
from collections import OrderedDict
from pychess.evaluation import evaluateBoard, moveValue, checkEndGame


class ChessAgent:

    def __init__(self, gameState, max_depth=3):
        self.debug_info = {}

        self.gamestate = gameState
        self.t_start = 0
        self.max_depth = max_depth
        self.mate_Score = 1000000000
        self.mate_Threshold = 999000000
        # self.size_table = 1e6
        # self.tt_table = OrderedDict()

    def playMove(self, debug=True):

        self.debug_info.clear()
        self.t_start = time.time()
        board = self.gamestate.boardPlay

        move = self.minimax_root(self.max_depth, board)

        self.debug_info["time"] = time.time() - self.t_start
        if debug == True:
            print(f"info {self.debug_info}")

        return move

    def get_ordered_moves(self, board):

        end_game = checkEndGame(board)

        def orderer(move):
            return moveValue(board, move, end_game)

        in_order = sorted(
            board.legal_moves, key=orderer, reverse=(board.turn == chess.WHITE)
        )
        return list(in_order)

    def minimax_root(self, depth, board):
        # check zobrist hash key
        key = chess.polyglot.zobrist_hash(board)
        # if key in self.tt_table:
        #     print("Have key in TT_table")
        #     move = self.tt_table.get(key)
        #     print(move)
        #     # move = chess.Move.from_uci(move_uci)
        #     return move

        # White always wants to maximize and black to minimize
        # the board score according to evaluateBoard()
        maximize = board.turn == chess.WHITE
        best_move = -float("inf")
        if not maximize:
            best_move = float("inf")

        moves = self.get_ordered_moves(board)
        best_move_found = chess.Move.null()

        # print(multiprocessing.cpu_count())
        pool = Pool(8)  # os.cpu_count()
        value = pool.starmap(self.multiProcessMinimax, zip(
            repeat(depth), repeat(board), moves))

        if maximize and max(value) >= best_move:
            best_move = max(value)
            index_valueBest = [index for index, item in enumerate(
                value) if item == max(value)][-1]
            best_move_found = moves[index_valueBest]
        elif not maximize and min(value) <= best_move:
            best_move = min(value)
            index_valueBest = [index for index, item in enumerate(
                value) if item == min(value)][-1]
            best_move_found = moves[index_valueBest]

        # save zobrist hash key in TT table
        # if (len(self.tt_table) > self.size_table):
        #     self.tt_table.popitem(last=False)
        # self.tt_table[key] = best_move_found

        return best_move_found

    def multiProcessMinimax(self, depth, board, move):

        maximize = board.turn == chess.WHITE

        board.push(move)
        if board.can_claim_draw():
            value = 0.0
        else:
            value = self.minimax(depth - 1, board, -float("inf"),
                                 float("inf"), not maximize)
        board.pop()

        return value

    def minimax(self, depth, board, alpha, beta, is_maximising_player):

        # key = chess.polyglot.zobrist_hash(board) # zobrist_hash_key
        # print(depth, None, key)

        if board.is_checkmate():
            # The previous move resulted in checkmate
            if is_maximising_player:
                return -self.mate_Score
            else:
                return self.mate_Score
        # When the game is over and it's not a checkmate it's a draw
        # In this case, don't evaluate. Just return a neutral result: zero
        elif board.is_game_over():
            return 0

        if (time.time() - self.t_start) > 110 or (depth == 0):
            return evaluateBoard(board)

        if is_maximising_player:
            best_move = -float("inf")
            moves = self.get_ordered_moves(board)
            for move in moves:
                board.push(move)
                curr_move = self.minimax(depth - 1, board, alpha,
                                         beta, not is_maximising_player)
                # Each ply after a checkmate is slower, so they get ranked slightly less
                # We want the fastest mate!
                if curr_move > self.mate_Threshold:
                    curr_move -= 1
                elif curr_move < -self.mate_Threshold:
                    curr_move += 1
                best_move = max(
                    best_move,
                    curr_move,
                )
                board.pop()
                alpha = max(alpha, best_move)
                if beta <= alpha:
                    return best_move
            return best_move
        else:
            best_move = float("inf")
            moves = self.get_ordered_moves(board)
            for move in moves:
                board.push(move)
                curr_move = self.minimax(depth - 1, board, alpha,
                                         beta, not is_maximising_player)
                if curr_move > self.mate_Threshold:
                    curr_move -= 1
                elif curr_move < -self.mate_Threshold:
                    curr_move += 1
                best_move = min(
                    best_move,
                    curr_move,
                )
                board.pop()
                beta = min(beta, best_move)
                if beta <= alpha:
                    return best_move
            return best_move
