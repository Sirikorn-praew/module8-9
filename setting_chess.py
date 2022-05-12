import chess
import re
from consts import (W_PAWN, W_KNIGHT, W_BISHOP, W_ROOK, W_QUEEN, W_KING, B_PAWN, B_KNIGHT, B_BISHOP, B_ROOK,
                    B_QUEEN, B_KING)
# starting_fen = '8/8/8/8/8/8/8/8'
starting_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
# starting_fen = 'rnbqk2r/pppp1ppp/5n2/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 1' #cas
# starting_fen = 'rnbqk2r/p1pp2pp/1p3p2/2b1p2n/2B1P3/2NP1N2/PPPBQPPP/R3K2R w KQkq - 0 1' #cas
# starting_fen = "rnbqk2r/p1pp2pp/1p3p2/2b1p2n/2B1P3/2NP1N2/PPPBQPPP/R3K2R w KQkq - 0 1"  # 2cas
# starting_fen = '4k3/8/8/p7/1p6/8/PP6/5K2 w - - 0 1'  # en p
# starting_fen = '8/6P1/7k/4B3/4B2K/8/8/8 w - - 0 1'  # pro
# starting_fen = '8/8/8/4b2k/4b3/7K/6p1/8 b - - 0 1' #pro
# starting_fen = '8/8/5b2/5b1k/8/7K/6p1/8 b - - 0 1' #pro
regex_square = re.compile(r'[a-h][1-8]')

piece_string_to_int = {'P': W_PAWN,
                       'N': W_KNIGHT,
                       'B': W_BISHOP,
                       'R': W_ROOK,
                       'Q': W_QUEEN,
                       'K': W_KING,
                       'p': B_PAWN,
                       'n': B_KNIGHT,
                       'b': B_BISHOP,
                       'r': B_ROOK,
                       'q': B_QUEEN,
                       'k': B_KING}

piece_int_to_string = {W_PAWN: 'P',
                       W_KNIGHT: 'N',
                       W_BISHOP: 'B',
                       W_ROOK: 'R',
                       W_QUEEN: 'Q',
                       W_KING: 'K',
                       B_PAWN: 'p',
                       B_KNIGHT: 'n',
                       B_BISHOP: 'b',
                       B_ROOK: 'r',
                       B_QUEEN: 'q',
                       B_KING: 'k'}

square_to_coords = {}
for row, rank in enumerate('87654321'):
    for col, file in enumerate('abcdefgh'):
        square_to_coords[file + rank] = (col, row)
