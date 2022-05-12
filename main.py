################################################################################
##
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide2
# V: 1.0.0
##
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
##
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
##
# Command: pyside2-uic -o ui_main.py GUI_BASE.ui GUI_BASE_newSize.ui
# Command: pyinstaller --onefile main.py
##
################################################################################

import traceback
from Comunication import Serial_Comunication_ISUS
import re
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTimer, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QImage)
from PySide2.QtWidgets import *
from PySide2.QtTest import QTest

import cv2
import serial
import chess
import random
import numpy as np
import copy

# GUI FILE
from app_modules import *

# CHESS FILE
import setting_chess
from pychess.board import ChessBoard
from pychess.info import Info

# # DETECTION
# import tensorflow as tf
# from tensorflow.python.client import device_lib
import mediapipe as mp


from Detection.main_detection2 import *
from Detection import variable

# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
# device_lib.list_local_devices()


# COMUNICATION

list_name = {chess.KING: 1, chess.QUEEN: 2, chess.ROOK: 3,
             chess.KNIGHT: 3, chess.BISHOP: 3, chess.PAWN: 4}


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.saved_game = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stack_process = 0
        self.video_size = QSize(480, 270)
        self.isus = 0
        self.startstop = 0
        self.stackfen = ''

        self.board = ChessBoard(self)
        self.board.sqr_size = 720/8
        self.info = Info(self)

        self.board_process = ChessBoard(self)
        self.board_process.sqr_size = 360/8

        self.board_detect = ChessBoard(self)
        self.board_detect.sqr_size = 360/8

        # self.maxAngular = 18  # deg/sec
        # self.station = []  # 1-10

        # Serial
        self.port = "COM"
        # self.ser = serial.Serial(port='COM6', baudrate=512000)

        # PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' + platform.release())

        ########################################################################
        # START - WINDOW ATTRIBUTES
        ########################################################################

        # REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        # SET ==> WINDOW TITLE
        self.setWindowTitle('G1 Module8-9')
        self.setWindowIcon(QIcon('./icons/chessMenu/chessIcon.png'))
        UIFunctions.labelTitle(self, 'G1 Module8-9 UI')
        UIFunctions.labelDescription(self, 'Use in Module8-9 Only')
        ## ==> END ##

        # WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1200, 900)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        # ==> CREATE MENUS
        ########################################################################

        # ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        # ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home",
                               "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Chess Game", "btn_game",
                               "url(:/16x16/icons/16x16/cil-gamepad.png)", True)
        UIFunctions.addNewMenu(self, "Detect", "btn_detect",
                               "url(:/16x16/icons/16x16/cil-camera.png)", True)
        UIFunctions.addNewMenu(self, "Setup", "btn_setup",
                               "url(:/16x16/icons/16x16/cil-equalizer.png)", True)
        # UIFunctions.addNewMenu(self, "Custom Widgets", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", True)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        # ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        # USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "G1", "", True)
        ## ==> END ##

        # DUCK ICON
        self.duck = QPixmap('./icons/Duck_You_clear.png')

        self.labelPic = QLabel()
        self.labelPic.setGeometry(QRect(0, 0, 120, 120))
        self.labelPic.setObjectName("labelPic")
        self.labelPic.setPixmap(self.duck)

        # CAMERA LABLE
        self.no_sigal = QPixmap('./icons/No_signal_resize.jpg')
        self.cam1_process_label = QLabel()
        self.cam1_process_label.setFixedSize(self.video_size)
        self.cam1_process_label.setPixmap(self.no_sigal)
        self.cam1_process_label.setAlignment(Qt.AlignCenter)
        self.cam2_process_label = QLabel()
        self.cam2_process_label.setFixedSize(self.video_size)
        self.cam2_process_label.setPixmap(self.no_sigal)
        self.cam2_process_label.setAlignment(Qt.AlignCenter)
        self.cam1_detect_label = QLabel()
        self.cam1_detect_label.setFixedSize(self.video_size)
        self.cam1_detect_label.setPixmap(self.no_sigal)
        self.cam1_detect_label.setAlignment(Qt.AlignCenter)
        self.cam2_detect_label = QLabel()
        self.cam2_detect_label.setFixedSize(self.video_size)
        self.cam2_detect_label.setPixmap(self.no_sigal)
        self.cam2_detect_label.setAlignment(Qt.AlignCenter)
        self.cam_set_label = QLabel()
        self.cam_set_label.setFixedSize(self.video_size)
        self.cam_set_label.setPixmap(self.no_sigal)
        self.cam_set_label.setAlignment(Qt.AlignCenter)

        self.ui.btn_page_process.clicked.connect(self.pageSelectProcess)
        self.ui.btn_play_white_process.clicked.connect(
            lambda: self.newProcessGame("w", True))
        self.ui.btn_play_black_process.clicked.connect(
            lambda: self.newProcessGame("b", True))
        # Function Page Process #Edit
        self.ui.chessBoard_process_layout.addWidget(self.board_process)
        self.ui.camera1_process_layout.addWidget(self.cam1_process_label)
        self.ui.camera2_process_layout.addWidget(self.cam2_process_label)
        self.ui.btn_open_camera_process.clicked.connect(
            lambda: self.setup_camera1(self.cam1_process_label))
        self.ui.btn_close_camera_process.clicked.connect(
            lambda: self.close_camera(2, self.cam1_process_label))
        self.ui.btn_open_camera_process.clicked.connect(
            lambda: self.setup_camera2(self.cam2_process_label))
        self.ui.btn_close_camera_process.clicked.connect(
            lambda: self.close_camera(4, self.cam2_process_label))
        self.ui.btn_detect_process.clicked.connect(
            lambda: self.capture_camera('process', 1, 'process'))
        self.ui.btn_predict_process.clicked.connect(
            lambda: self.capture_camera('process', 0, 'process'))
        self.ui.btn_start_process.clicked.connect(self.startProcess)
        self.ui.status_turn_process.setText(self.showTurn())
        # self.ui.btn_reset_process.clicked.connect(
        #     self.board_detect.draw_squares)
        self.ui.btn_send_startstop_process.clicked.connect(
            self.sendStartStopProcess)
        self.ui.btn_send_home_process.clicked.connect(self.sendsetHome)
        self.ui.btn_send_chess_home_process.clicked.connect(
            self.sendChess_Home)
        self.ui.btn_send_zero_field_process.clicked.connect(
            self.sendField_zero)
        self.ui.btn_agent_play.clicked.connect(self.agentPlay)
        self.ui.btn_cancle_process.clicked.connect(
            self.board_process.refresh_from_state)
        self.ui.btn_undo_process.clicked.connect(self.undoMove)
        self.ui.btn_redo_process.clicked.connect(self.redoMove)

        # Function Page Game
        self.ui.btn_new_game.clicked.connect(self.chooseSide)
        self.ui.btn_new_game_isus.clicked.connect(self.chooseSideIsus)
        self.ui.btn_out_game.clicked.connect(self.backHomeGame)
        self.ui.game_layout.addWidget(self.board)
        self.ui.info_layout.addWidget(self.info)

        # Function Page New Game Select
        self.ui.btn_play_white.clicked.connect(
            lambda: self.newGame("w", False))  # if self.isus == 0 else True
        self.ui.btn_play_black.clicked.connect(
            lambda: self.newGame("b", False))
        self.ui.btn_random.clicked.connect(
            lambda: self.newGame(random.choice(["w", "b"]), False))
        # self.ui.btn_computer.clicked.connect(lambda: self.newGame(None, True))

        # Function Page Detect
        self.ui.chessBoard_detect_layout.addWidget(self.board_detect)
        self.ui.camera1_detect_layout.addWidget(self.cam1_detect_label)
        self.ui.camera2_detect_layout.addWidget(self.cam2_detect_label)
        self.ui.btn_open_camera_set.clicked.connect(
            lambda: self.setup_camera1(self.cam_set_label))
        self.ui.btn_close_camera_set.clicked.connect(
            lambda: self.close_camera(2, self.cam_set_label))
        self.ui.btn_open_camera_detect.clicked.connect(
            lambda: self.setup_camera1(self.cam1_detect_label))
        self.ui.btn_close_camera_detect.clicked.connect(
            lambda: self.close_camera(2, self.cam1_detect_label))
        self.ui.btn_open_camera_detect.clicked.connect(
            lambda: self.setup_camera2(self.cam2_detect_label))
        self.ui.btn_close_camera_detect.clicked.connect(
            lambda: self.close_camera(4, self.cam2_detect_label))
        self.ui.btn_detect_detect.clicked.connect(
            lambda: self.capture_camera('detect', 1, 'test detect'))
        self.ui.btn_predict_detect.clicked.connect(
            lambda: self.capture_camera('detect', 0, 'test detect'))
        self.ui.btn_reset_detect.clicked.connect(self.resetBoardDetect)

        # Function Page Setup
        self.ui.duck_layout.addWidget(self.labelPic)
        self.ui.camera_set_layout.addWidget(self.cam_set_label)
        self.ui.comboBox_piece.addItem("")
        self.ui.comboBox_piece.addItem("")
        self.ui.comboBox_piece.addItem("")
        self.ui.comboBox_piece.addItem("")
        self.ui.comboBox_piece.addItem("")
        self.ui.comboBox_piece.addItem("")
        self.ui.comboBox_piece.setItemText(0, "KING")
        # {"KING": 1, "QUEEN": 2, "ROOK": 3,"KNIGHT": 3, "BISHOP": 3, "PAWN": 4}
        self.ui.comboBox_piece.setItemText(1, "QUEEN")
        self.ui.comboBox_piece.setItemText(2, "ROOK")
        self.ui.comboBox_piece.setItemText(3, "KNIGHT")
        self.ui.comboBox_piece.setItemText(4, "BISHOP")
        self.ui.comboBox_piece.setItemText(5, "PAWN")
        self.ui.btn_send_startstop.clicked.connect(self.sendStartStop)
        self.ui.btn_send_home.clicked.connect(self.sendsetHome)
        self.ui.btn_send_joint.clicked.connect(self.sendJoint)
        self.ui.btn_send_xyz.clicked.connect(self.sendxyz)
        self.ui.btn_send_grip_open.clicked.connect(self.sendGripOpen)
        self.ui.btn_send_grip_close.clicked.connect(self.sendGripClose)
        self.ui.btn_send_chess_home.clicked.connect(self.sendChess_Home)
        self.ui.btn_send_zero_field.clicked.connect(self.sendField_zero)
        self.ui.btn_send_pick_place.clicked.connect(self.sendChess_Pick)

        self.ui.horizontalSlider_joint_1.valueChanged.connect(
            self.updateAngulaJoint_1_toText)
        self.ui.value_angular_joint_1.valueChanged.connect(
            self.updateAngulaJoint_1_toSilder)
        self.ui.horizontalSlider_joint_2.valueChanged.connect(
            self.updateAngulaJoint_2_toText)
        self.ui.value_angular_joint_2.valueChanged.connect(
            self.updateAngulaJoint_2_toSilder)
        self.ui.horizontalSlider_joint_3.valueChanged.connect(
            self.updateAngulaJoint_3_toText)
        self.ui.value_angular_joint_3.valueChanged.connect(
            self.updateAngulaJoint_3_toSilder)
        self.ui.horizontalSlider_joint_4.valueChanged.connect(
            self.updateAngulaJoint_4_toText)
        self.ui.value_angular_joint_4.valueChanged.connect(
            self.updateAngulaJoint_4_toSilder)
        self.ui.horizontalSlider_x.valueChanged.connect(
            self.update_x_toText)
        self.ui.value_x.valueChanged.connect(
            self.update_x_toSilder)
        self.ui.horizontalSlider_y.valueChanged.connect(
            self.update_y_toText)
        self.ui.value_y.valueChanged.connect(
            self.update_y_toSilder)
        self.ui.horizontalSlider_z.valueChanged.connect(
            self.update_z_toText)
        self.ui.value_z.valueChanged.connect(
            self.update_z_toSilder)

        # ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:  # CAN USE
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        # ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        # END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################

        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################

        # ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        ## ==> END ##

        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ########################################################################
    # MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            if self.stack_process == 0:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                UIFunctions.resetStyle(self, "btn_home")
                UIFunctions.labelPage(self, "Home")
                btnWidget.setStyleSheet(
                    UIFunctions.selectMenu(btnWidget.styleSheet()))
                # print(self.stack_process)
            else:
                self.ui.stackedWidget.setCurrentWidget(
                    self.ui.page_all_process)
                UIFunctions.labelPage(self, "On Process")
            # print(self.stack_process)

        # PAGE Main Game
        if btnWidget.objectName() == "btn_game":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_game)
            UIFunctions.resetStyle(self, "btn_game")
            UIFunctions.labelPage(self, "Chess Game")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))
        if btnWidget.objectName() == "btn_new_game":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_play_chess)
            UIFunctions.resetStyle(self, "btn_new_game")
            UIFunctions.labelPage(self, "Play Game")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE DETECT
        if btnWidget.objectName() == "btn_detect":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_detect)
            UIFunctions.resetStyle(self, "btn_detect")
            UIFunctions.labelPage(self, "Detection")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE SETUP
        if btnWidget.objectName() == "btn_setup":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_run)
            UIFunctions.resetStyle(self, "btn_setup")
            UIFunctions.labelPage(self, "New User")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        # if btnWidget.objectName() == "btn_widgets":
        #     self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
        #     UIFunctions.resetStyle(self, "btn_widgets")
        #     UIFunctions.labelPage(self, "Custom Widgets")
        #     btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    # START ==> PROCESS FUNCTION
    ########################################################################
    def showTurn(self):
        # print(self.board_process.gamestate.boardPlay.fen)
        try:
            return "White" if self.board_process.gamestate.boardPlay.turn == chess.WHITE else "Black"
        except:
            return "---"

    def get_move(self, board1, board2, who_moved):
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
            dst_square = move[2:4]
            dst_sqr_index = chess.parse_square(dst_square)
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

    def pageSelectProcess(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_select_process)
        UIFunctions.labelPage(self, "Select Side")

    def startProcess(self):
        self.capture_camera('detect_process', 1, 'set')
        self.board_process.start_game_process()

    def agentPlay(self):
        board_after = chess.Board(self.stackfen)
        move = self.get_move(
            self.board_process.gamestate.boardPlay, board_after, self.board_process.gamestate.boardPlay.turn)
        # move = chess.Move.from_uci(move_uci)
        self.board_process.player_move(move)

    def undoMove(self):
        if self.board_process.gamestate.undo_info:

            # Undo computer's move
            # Get move at the top of move stack
            move = self.board.gamestate.undo_info[-1]['move']
            # Move piece back to source square
            self.board_process.move_glide(move, True)
            self.board_process.gamestate.undo_move()  # Undo move in game state
            self.board_process.refresh_from_state()  # Refresh board
            self.board_process.undone_stack.append(move)

            # Undo player's move
            if self.board_process.gamestate.undo_info:
                # Get move at the top of move stack
                move = self.board_process.gamestate.undo_info[-1]['move']
                # Move piece back to source square
                self.board_process.move_glide(move, True)
                self.board_process.gamestate.undo_move()  # Undo move in game state
                self.board_process.refresh_from_state()  # Refresh board
                self.board_process.undone_stack.append(move)

            else:
                self.board_process.undone_stack.clear()
                self.board_process.search_thread.start()

    def redoMove(self):
        if self.board_process.undone_stack:

            move = self.board_process.undone_stack.pop()
            self.board_process.move_glide(move, False)
            self.board_process.gamestate.make_move(move)
            self.board_process.refresh_from_state()

            move = self.board_process.undone_stack.pop()
            self.board_process.move_glide(move, False)
            self.board_process.gamestate.make_move(move)
            self.board_process.refresh_from_state()

    ## ==> END ##

    ########################################################################
    # START ==> SETUP FUNCTION
    ########################################################################

    def updateAngulaJoint_1_toText(self, value):
        self.ui.value_angular_joint_1.setValue(value)

    def updateAngulaJoint_1_toSilder(self, value):
        self.ui.horizontalSlider_joint_1.setValue(value)

    def updateAngulaJoint_2_toText(self, value):
        self.ui.value_angular_joint_2.setValue(value)

    def updateAngulaJoint_2_toSilder(self, value):
        self.ui.horizontalSlider_joint_2.setValue(value)

    def updateAngulaJoint_3_toText(self, value):
        self.ui.value_angular_joint_3.setValue(value)

    def updateAngulaJoint_3_toSilder(self, value):
        self.ui.horizontalSlider_joint_3.setValue(value)

    def updateAngulaJoint_4_toText(self, value):
        self.ui.value_angular_joint_4.setValue(value)

    def updateAngulaJoint_4_toSilder(self, value):
        self.ui.horizontalSlider_joint_4.setValue(value)

    def update_x_toText(self, value):
        self.ui.value_x.setValue(value)

    def update_x_toSilder(self, value):
        self.ui.horizontalSlider_x.setValue(value)

    def update_y_toText(self, value):
        self.ui.value_y.setValue(value)

    def update_y_toSilder(self, value):
        self.ui.horizontalSlider_y.setValue(value)

    def update_z_toText(self, value):
        self.ui.value_z.setValue(value)

    def update_z_toSilder(self, value):
        self.ui.horizontalSlider_z.setValue(value)

    def sendStartStop(self):
        startstop_1 = int(self.ui.checkBox_joint_1.isChecked())
        startstop_2 = int(self.ui.checkBox_joint_2.isChecked())
        startstop_3 = int(self.ui.checkBox_joint_3.isChecked())
        startstop_4 = int(self.ui.checkBox_joint_4.isChecked())
        ISUS_UART.StartStop_Move(
            startstop_1, startstop_2, startstop_3, startstop_4, 1)

    def sendStartStopProcess(self):
        if self.startstop == 0:
            ISUS_UART.StartStop_Move(1, 1, 1, 1, 1)
            self.startstop = 1
        else:
            ISUS_UART.StartStop_Move(0, 0, 0, 0, 1)
            self.startstop = 0

    def sendsetHome(self):
        ISUS_UART.StartStop_Move(1, 1, 1, 1, 1)
        ISUS_UART.Home_Configulation(1, 1, 1, 1)

    def sendJoint(self):
        ISUS_UART.StartStop_Move(1, 1, 1, 1, 1)
        joint_1 = self.ui.value_angular_joint_1.value()
        joint_2 = self.ui.value_angular_joint_2.value()
        joint_3 = self.ui.value_angular_joint_3.value()
        joint_4 = self.ui.value_angular_joint_4.value()
        ISUS_UART.Joint_Move(joint_1, joint_2, joint_3, joint_4)

    def sendxyz(self):
        ISUS_UART.StartStop_Move(1, 1, 1, 1, 1)
        x = self.ui.value_x.value()
        y = self.ui.value_y.value()
        z = self.ui.value_z.value()
        ISUS_UART.XYZ_Move(x, y, z, 0)

    def sendGripOpen(self):
        ISUS_UART.Grip_Chess(0)

    def sendGripClose(self):
        ISUS_UART.Grip_Chess(55)

    def sendField_zero(self):
        ISUS_UART.Field_zero()

    def sendChess_Home(self):
        ISUS_UART.Chess_HOME()

    def sendChess_Pick(self):
        # try:
        rowi = (self.ui.value_pick.text())[0]
        print(rowi)
        columni = int((self.ui.value_pick.text())[1])
        print(columni)
        rowf = (self.ui.value_place.text())[0]
        print(rowf)
        columnf = int((self.ui.value_place.text())[1])
        print(columnf)
        piece = self.ui.comboBox_piece.currentIndex() + 1
        if piece in [3, 4, 5]:
            piece = 3
        elif piece == 6:
            piece = 4
        print(piece)
        ISUS_UART.Chess_Pick(rowi, columni, rowf, columnf, piece)
        # except:stack_process
        #     print("error")
        #
    ## ==> END ##

    ########################################################################
    # START ==> CHESS FUNCTION
    ########################################################################

    def chooseSide(self):
        self.isus = 0
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_newgame_select)
        UIFunctions.labelPage(self, "Choose Side")

    def chooseSideIsus(self):
        self.isus = 1
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_newgame_select)
        UIFunctions.labelPage(self, "Choose Side")

    def newProcessGame(self, colour, agent_play):
        self.stack_process = 1
        # self.board_process.set_fen(setting_chess.starting_fen)
        self.board_process.agent_play = agent_play
        self.board_process.user_is_white = True if colour == 'w' else False
        # self.board_process.start_game()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_all_process)
        UIFunctions.labelPage(self, "On Process")

    def newGame(self, colour, agent_play):
        self.info.move_frame.clear_moves()
        self.board.set_fen(setting_chess.starting_fen)
        self.board.agent_play = agent_play
        self.board.isus = self.isus
        print(self.board.isus)
        # if self.board.isus:
        #     # print("y")
        #     # print(colour)
        #     self.sendChess_Home()
        self.board.user_is_white = True if colour == 'w' else False
        self.board.start_game()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_play_chess)
        UIFunctions.labelPage(self, "Play Game")

    def playGame(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_play_chess)
        UIFunctions.labelPage(self, "Play Game")

    def backHomeGame(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_game)
        UIFunctions.labelPage(self, "Chess Game")

    ## ==> END ##

    ########################################################################
    # START ==> CAMERA SETTING
    ########################################################################

    def setup_camera1(self, label):
        """Initialize camera.
        """
        try:
            # set new dimensionns to cam object (not cap)

            self.capture1 = cv2.VideoCapture(2, cv2.CAP_DSHOW)
            self.capture1.set(3, 1280)
            self.capture1.set(4, 1024)
            _, self.image_side = copy.deepcopy(
                self.capture1.read())
            self.image_side = np.array(self.image_side)
            self.capture1.set(cv2.CAP_PROP_FRAME_WIDTH,
                              self.video_size.width())
            self.capture1.set(cv2.CAP_PROP_FRAME_HEIGHT,
                              self.video_size.height())

            self.timer1 = QTimer()
            self.timer1.timeout.connect(
                lambda: self.display_video_stream1(label))
            self.timer1.start(30)
        except:
            print(f"Cam 1 is invalid.")

    def setup_camera2(self, label):  # top หน้าจอ2
        """Initialize camera.
        """
        try:
            self.capture2 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            # set new dimensionns to cam object (not cap)
            self.capture2.set(3, 1280)
            self.capture2.set(4, 1024)
            _, self.image_top = copy.deepcopy(
                self.capture2.read())
            self.image_top = np.array(self.image_top)
            self.capture2.set(cv2.CAP_PROP_FRAME_WIDTH,
                              self.video_size.width())
            self.capture2.set(cv2.CAP_PROP_FRAME_HEIGHT,
                              self.video_size.height())

            self.timer2 = QTimer()
            self.timer2.timeout.connect(
                lambda: self.display_video_stream2(label))
            self.timer2.start(30)
        except:
            print(f"Cam 3 is invalid.")

    def display_video_stream1(self, label):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture1.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        label = label
        label.setPixmap(QPixmap.fromImage(image))

    def display_video_stream2(self, label):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture2.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        # self.image_side = frame
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        label = label
        label.setPixmap(QPixmap.fromImage(image))

    def close_camera(self, idx, label):
        try:
            self.capture1.release()
            label.setPixmap(self.no_sigal)
            self.timer1.stop()
        except:
            print(f"capture1 is invalid.")
        try:
            self.capture2.release()
            label.setPixmap(self.no_sigal)
            self.timer2.stop()
        except:
            print(f"capture2 is invalid.")

    def capture_camera(self, status, detect, page):
        self.ui.status_process.setText('Capturing and predicting')
        # self.setup_camera1(self.cam1_detect_label)
        # self.setup_camera2(self.cam2_detect_label)

        fen_before = self.board_process.gamestate.getFen()
        print(fen_before, detect)
        if page == 'test detect':
            self.setup_camera1(self.cam1_detect_label)
            self.setup_camera2(self.cam2_detect_label)
            print("evaluate chess pieces")
            cv2.imwrite('image_side.jpg', self.image_side)
            cv2.imwrite('image_top.jpg', self.image_top)

            fen = main_chess_piece(
                self.image_side, self.image_top, detect, modelE4, modelE4_top)
        elif page == 'set':
            fen = setting_chess.starting_fen
            self.board_process.set_fen(fen)
        else:
            self.setup_camera1(self.cam1_process_label)
            self.setup_camera2(self.cam2_process_label)
            print("evaluate chess pieces")
            cv2.imwrite('image_side.jpg', self.image_side)
            cv2.imwrite('image_top.jpg', self.image_top)

            user_is_black = 1 if self.board_process.user_is_white == False else 0
            fen = use_trackback(self.image_top, detect,
                                fen_before, user_is_black, modelE4_top)
            print("out", fen)

        # fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        # fen = '8/6P1/7k/4B3/4B2K/8/8/8 w - - 0 1'
        # fen = '8/6n1/pp4p1/4p1p1/6p1/8/8/R4r1r'
        # fen = None

        if fen != None:
            self.ui.status_fen_detect.setText(fen)
            self.ui.status_detect.setText('Detected!')
            self.ui.status_fen_process.setText(fen)
            self.ui.status_process.setText('Detected!')
        else:
            self.ui.status_fen_detect.setText('Value')
            self.ui.status_detect.setText('S A D')
            self.ui.status_fen_process.setText('Value')
            self.ui.status_process.setText('S A D')
        if status == 'detect':
            self.board_detect.set_fen(fen)
        # elif status == 'detect_process':
        #     self.board_process.set_fen(fen)  # setting_chess.starting_fen
        elif status == 'process':
            self.board_process.showfen(fen)
            self.stackfen = fen
            # board_after = chess.Board(fen)
            # move = self.get_move(
            #     self.board_process.gamestate.boardPlay, board_after, self.board_process.gamestate.boardPlay.turn)
            # # move = chess.Move.from_uci(move_uci)
            # self.board_process.player_move(move)

    def resetBoardDetect(self):
        fen = '8/8/8/8/8/8/8/8'  # w - - 0 1
        self.board_detect.set_fen(fen)
        self.ui.status_fen_detect.setText('Value')
        self.ui.status_detect.setText('Value')

    ## ==> END ##

    ########################################################################
    # START ==> MOVE COMMU
    ########################################################################
    def readFeedback(self):
        ISUS_UART.Uart_Read()

    def getStatus(self):
        return ISUS_UART.getStatus()

    def resetStatus(self):
        ISUS_UART.resetStatus()

    def waitFeedback(self, rowiR, columniR, rowfR, columnfR):
        ISUS_UART.Uart_Read()
        # print(ISUS_UART.getStatus())
        if ISUS_UART.getStatus() == 99:
            ISUS_UART.Chess_Pick(rowiR, columniR, rowfR, columnfR, 3)
            print("ft")
            # self.timer.stop()
            # self.timer.deleteLater()
            ISUS_UART.resetStatus()

    def normally_move(self, from_square, to_square, piece):
        rowi = from_square[0]
        print(rowi)
        columni = int(from_square[1])
        rowf = to_square[0]
        columnf = int(to_square[1])
        ISUS_UART.Chess_Pick(
            rowi, columni, rowf, columnf, list_name[piece])

    def castling_move(self, from_square, to_square):
        rowiK = from_square[0]
        columniK = int(from_square[1])
        rowfK = to_square[0]
        columnfK = int(to_square[1])
        if to_square == "c1":
            rowiR = "a"
            columniR = 1
            rowfR = "d"
            columnfR = 1
        elif to_square == "g1":
            rowiR = "h"
            columniR = 1
            rowfR = "f"
            columnfR = 1
        elif to_square == "c8":
            rowiR = "a"
            columniR = 8
            rowfR = "d"
            columnfR = 8
        elif to_square == "g8":
            rowiR = "h"
            columniR = 8
            rowfR = "f"
            columnfR = 8
        # self.timer = QTimer()
        # ISUS_UART.Chess_Pick(rowiK, columniK, rowfK, columnfK, 1)
        ISUS_UART.Chess_Pick2(rowiK, columniK, rowfK,
                              columnfK, rowiR, columniR, rowfR, columnfR, 1, 3)

        # lambda: self.waitFeedback(ISUS_UART.Chess_Pick(rowiR, columniR, rowfR, columnfR, 3))
        # self.timer.timeout.connect(lambda: self.waitFeedback(
        #     rowiR, columniR, rowfR, columnfR, 3))

        # self.timer.timeout.connect(lambda: waitFeedback(
        #     ft=ISUS_UART.Chess_Pick(rowiR, columniR, rowfR, columnfR, 3)))
        # QTimer.singleShot(200, lambda: ISUS_UART.Chess_Pick(
        #     rowiR, columniR, rowfR, columnfR, 3))

        # self.timer.start(2000)
        # ISUS_UART.Chess_Pick(rowiR, columniR, rowfR, columnfR, 3)

    def promotion_move(self, from_square, to_square):
        rowi = from_square[0]
        columni = int(from_square[1])
        rowf = to_square[0]
        columnf = int(to_square[1])
        ISUS_UART.Chess_Pick(rowi, columni, rowf, columnf, 4)

    def capture_move(self, from_square, to_square, piece_move, piece_captured):
        rowi = from_square[0]
        columni = int(from_square[1])
        rowf = to_square[0]
        columnf = int(to_square[1])
        ISUS_UART.Chess_Drop(rowi, columni, rowf, columnf, rowf,
                             columnf, list_name[piece_move], list_name[piece_captured])
        # ISUS_UART.Chess_Drop(
        #     rowf, columnf, list_name[piece_captured])
        # ISUS_UART.Uart_Read()
        # ISUS_UART.Chess_Pick(
        #     rowi, columni, rowf, columnf, list_name[piece_move])

    def en_passant_move(self, from_square, to_square, turn):
        rowi = from_square[0]
        columni = int(from_square[1])
        rowf = to_square[0]
        columnf = int(to_square[1])
        if turn == chess.WHITE:
            # ISUS_UART.Chess_Drop(rowf, columnf+1, 4)
            ISUS_UART.Chess_Drop(rowi, columni, rowf,
                                 columnf, rowf, columnf+1, 4, 4)

        else:
            # ISUS_UART.Chess_Drop(rowf, columnf-1, 4)
            ISUS_UART.Chess_Drop(rowi, columni, rowf,
                                 columnf, rowf, columnf-1, 4, 4)
        # ISUS_UART.Uart_Read()
        # ISUS_UART.Chess_Pick(rowi, columni, rowf, columnf, 4)

    ## ==> END ##

    ########################################################################
    # START ==> APP EVENTS
    ########################################################################

    ## ==> END ##

    # EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################

    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    # EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    # EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) +
              ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    # EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) +
              ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    # END ==> APP EVENTS
    ############################## ---/--/--- ##############################


if __name__ == "__main__":
    ISUS_UART = Serial_Comunication_ISUS.Uart_ISUS()
    ISUS_UART.setupUart()

    modelE4_top = EfficientNetModel(
        '.\Detection\checkpoint_top', (380, 380))
    modelE4 = EfficientNetModel(
        '.\Detection\checkpoint_demo', (380, 380))
    print('finish')

    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
