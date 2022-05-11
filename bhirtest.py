# import tensorflow as tf
# from tensorflow.python.client import device_lib

# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
# device_lib.list_local_devices()

import chess

# fen1 = "rn2kbnr/ppq1p2p/2ppb1p1/8/4p2P/3P2P1/PPP1KP2/RNBQ1BNR"
# fen1 = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" #start
# fen2 = "rnbqkbnr/pppppppp/8/8/8/2N5/PPPPPPPP/R1BQKBNR w KQkq - 0 1" #b1c3
# fen1 = "rnbqk2r/pppp1ppp/5n2/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 1"  # befor cas
# fen2 = "rnbqk2r/pppp1ppp/5n2/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQ1RK1 w kq - 0 1"  # cas
fen1 = "rnbqk2r/p1pp2pp/1p3p2/2b1p2n/2B1P3/2NP1N2/PPPBQPPP/R3K2R w KQkq - 0 1"  # befor cas
fen2 = "rnbqk2r/p1pp2pp/1p3p2/2b1p2n/2B1P3/2NP1N2/PPPBQPPP/R4RK1 w kq - 0 1"  # cas
# fen2 = "rnbqk2r/p1pp2pp/1p3p2/2b1p2n/2B1P3/2NP1N2/PPPBQPPP/2KR3R w kq - 0 1"  # cas

# fen1 = '4k3/8/8/p7/1p6/8/PP6/5K2 w - - 0 1'
# fen2 = '4k3/8/8/p7/8/p7/1P6/5K2 w - - 0 1' # en
# fen1 = '8/6P1/7k/4B3/4B2K/8/8/8'
# fen2 = '6N1/8/7k/4B3/4B2K/8/8/8' #pro
# fen1 = 'r2q2k1/2p2npp/1p2p3/pP3p2/1P1Q3B/P3P2P/5PP1/2R3K1'
# fen2 = 'r2B2k1/2p2npp/1p2p3/pP3p2/1P1Q4/P3P2P/5PP1/2R3K1' #cap

board1 = chess.Board(fen1)
# move1 = chess.Move.from_uci("a2a4")
# board1.push(move1)
board2 = chess.Board(fen2)

# listBoard1 = [str(board1)]
# listBoard2 = [str(board2)]
# # print(listBoard1)
# print(type(str(board1.fen)))

# p = (set(listBoard1) - set(listBoard2))

# print(p)

# print(board)
# print(board.turn)

# move = "a2a4"
# print(move[:2])

# fen1 = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
# fen2 = 'rnbqkbnr/pppppppp/8/8/5P2/8/PPPPP1PP/RNBQKBNR w KQkq - 0 1'


def get_move(board1, board2, who_moved):
    nums = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}
    str_board = str(board1).split("\n")
    str_board2 = str(board2).split("\n")
    move = ""
    flip = False
    if who_moved == chess.WHITE:
        for i in range(8)[::-1]:
            for x in range(15)[::-1]:
                if str_board[i][x] != str_board2[i][x]:
                    if str_board[i][x] == "." and move == "":
                        flip = True
                    move += str(nums.get(round(x/2)+1))+str(9-(i+1))
    else:
        for i in range(8):
            for x in range(15):
                if str_board[i][x] != str_board2[i][x]:
                    if str_board[i][x] == "." and move == "":
                        flip = True
                    move += str(nums.get(round(x/2)+1))+str(9-(i+1))
    if flip:
        move = move[2]+move[3]+move[0]+move[1]
    print(move)
    if len(move) > 4:
        if who_moved == chess.WHITE:
            if "e1" in move and "h1" in move:
                move = board1.find_move(4, 6)
            elif "e1" in move and "a1" in move:
                move = board1.find_move(4, 2)
        else:
            if "e8" in move and "h8" in move:
                move = board1.find_move(60, 63)
            elif "e8" in move and "a8" in move:
                move = board1.find_move(60, 58)
    else:
        src_square = move[:2]
        src_sqr_index = chess.parse_square(src_square)
        # print(src_square, src_sqr_index)
        dst_square = move[2:4]
        dst_sqr_index = chess.parse_square(dst_square)
        # print(dst_square, dst_sqr_index)
        if not board1.piece_at(dst_sqr_index) and board1.piece_at(src_sqr_index).piece_type == chess.PAWN and (board1.piece_at(src_sqr_index) != board2.piece_at(dst_sqr_index)):
            print(who_moved == chess.WHITE, dst_square[1])
            if who_moved == chess.WHITE and dst_square[1] == '8':
                move = board1.find_move(
                    src_sqr_index, dst_sqr_index, board2.piece_at(dst_sqr_index).piece_type)
            elif who_moved == chess.BLACK and dst_square[1] == '1':
                move = board1.find_move(
                    src_sqr_index, dst_sqr_index, board2.piece_at(dst_sqr_index).piece_type)
            else:
                move = None
        else:
            try:
                move = board1.find_move(src_sqr_index, dst_sqr_index)
            except:
                move = None
    legal_moves = board1.legal_moves
    print(legal_moves)
    if move not in legal_moves:
        print('move not in legal_moves')
        move = None

    return move


print(get_move(board1, board2, chess.WHITE))
# print(board1.is_castling(get_move(board1, board2, "w")))
# move = board1.find_move(4, 2)
# print()

# fen = '4k3/8/8/4pP2/8/8/8/4K3 w - - 0 1'
# fen1 = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
# fen2 = 'rnbqkbnr/pppppppp/8/8/5P2/8/PPPPP1PP/RNBQKBNR w KQkq - 0 1'

# board = chess.Board(fen1)
# print(board.set_fen(fen2))
# print(board.pop())

# starting_fen = 'rnbqk2r/pppp1ppp/5n2/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 1'
# board = chess.Board(starting_fen)
# print(board.legal_moves)

# import cv2

# def list_ports():
#     """Test the ports and returns a tuple with the available ports and the ones that are working."""
#     is_working = True
#     dev_port = 0
#     working_ports = []
#     available_ports = []
#     while is_working:
#         camera = cv2.VideoCapture(dev_port)
#         if not camera.isOpened():
#             is_working = False
#             print("Port %s is not working." % dev_port)
#         else:
#             is_reading, img = camera.read()
#             w = camera.get(3)
#             h = camera.get(4)
#             if is_reading:
#                 print("Port %s is working and reads images (%s x %s)" %
#                       (dev_port, h, w))
#                 working_ports.append(dev_port)
#             else:
#                 print("Port %s for camera ( %s x %s) is present but does not reads." % (
#                     dev_port, h, w))
#                 available_ports.append(dev_port)
#         dev_port += 1
#     return available_ports, working_ports


# print(list_ports())

# def testDevice(source):
#     cap = cv2.VideoCapture(source)
#     if cap is None or not cap.isOpened():
#         print('Warning: unable to open video source: ', source)


# # testDevice(0)  # no printout
# # testDevice(1)
# # testDevice(2)
# # testDevice(3)
# testDevice(5)

# import cv2
# print(cv2.__version__)
# width = 1280
# height = 720
# cam = cv2.VideoCapture(2, cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
# while True:
#     ignore,  frame = cam.read()
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam', 0, 0)
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
# cam.release()
