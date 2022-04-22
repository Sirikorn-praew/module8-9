# inspired by the https://github.com/thomasahle/sunfish user inferface

import chess
import argparse
from chessAgent import ChessAgent


def start():
    """
    Start the command line user interface.
    """
    board = chess.Board(
        '4r1k1/5ppp/p7/2p5/P1q5/1n4Q1/BB3PPP/5RK1 b - - 0 1')  # rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
    user_side = (
        chess.WHITE if input(
            "Start as [w]hite or [b]lack:\n") == "w" else chess.BLACK
    )

    if user_side == board.turn:
        print(render(board))
        user_move = get_move(board)
        board.push(user_move)

    while not board.is_game_over():
        agent = ChessAgent(get_depth())
        move = agent.playMove(board, debug=True)
        print(move)
        board.push(move)
        print(render(board))
        if board.is_checkmate():
            print("Checkmate!")
            break
        elif board.is_check():
            print("check")
        elif board.is_stalemate():
            print("Stalemate")
        elif board.is_game_over():
            print("Game Over!")
        board.push(get_move(board))

    print(f"\nResult: [w] {board.result()} [b]")


def render(board: chess.Board) -> str:
    """
    Print a side-relative chess board with special chess characters.
    """
    board_string = list(str(board))
    uni_pieces = {
        "R": "♖",
        "N": "♘",
        "B": "♗",
        "Q": "♕",
        "K": "♔",
        "P": "♙",
        "r": "♜",
        "n": "♞",
        "b": "♝",
        "q": "♛",
        "k": "♚",
        "p": "♟",
        ".": "·",
    }
    for idx, char in enumerate(board_string):
        if char in uni_pieces:
            board_string[idx] = uni_pieces[char]
    ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
    display = []
    for rank in "".join(board_string).split("\n"):
        display.append(f"  {ranks.pop()} {rank}")
    if board.turn == chess.BLACK:
        display.reverse()
    display.append("    a b c d e f g h")
    return "\n" + "\n".join(display)


def get_move(board: chess.Board) -> chess.Move:
    """
    Try (and keep trying) to get a legal next move from the user.
    Play the move by mutating the game board.
    """
    move_uci = input(f"\nYour move (e.g. {list(board.legal_moves)[0]}):\n")

    # for legal_move in board.legal_moves:
    #     if move == str(legal_move):
    #         return legal_move
    try:
        move = chess.Move.from_uci(move_uci)
        if move in board.legal_moves:
            return move
        print("Can't move this move.")
    except:
        print(
            f"Please type the correct move. (e.g. {list(board.legal_moves)[0]})")
    return get_move(board)


def get_depth() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", default=5,
                        help="provide an integer (default: 5)")
    args = parser.parse_args()
    return max([1, int(args.depth)])


if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        pass
