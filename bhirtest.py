# import tensorflow as tf
# from tensorflow.python.client import device_lib

# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
# device_lib.list_local_devices()

# import chess

# fen = "rn2kbnr/ppq1p2p/2ppb1p1/8/4p2P/3P2P1/PPP1KP2/RNBQ1BNR"

# board = chess.Board(fen)


# print(board.turn)

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

import cv2
print(cv2.__version__)
width = 1280
height = 720
cam = cv2.VideoCapture(2, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
