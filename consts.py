import chess
from itertools import chain, combinations

PIECES = (W_PAWN,
          W_KNIGHT,
          W_BISHOP,
          W_ROOK,
          W_QUEEN,
          W_KING,
          B_PAWN,
          B_KNIGHT,
          B_BISHOP,
          B_ROOK,
          B_QUEEN,
          B_KING) = list(chain(range(1, 7), range(9, 15)))

NO_PIECE = 0
