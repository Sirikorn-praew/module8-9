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

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTimer, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QImage)
from PySide2.QtWidgets import *

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

# DETECTION
from Detection import main_detection

# COMUNICATION
from Comunication import Serial_Comunication_ISUS


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.saved_game = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.video_size = QSize(480, 270)

        self.board = ChessBoard(self)
        self.board.sqr_size = 720/8
        self.info = Info(self)

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

        self.ui.btn_start_process.clicked.connect(self.pageProcess)
        # Function Page Process

        # Function Page Game
        self.ui.btn_new_game.clicked.connect(self.chooseSide)
        self.ui.btn_out_game.clicked.connect(self.backHomeGame)
        self.ui.game_layout.addWidget(self.board)
        self.ui.info_layout.addWidget(self.info)

        # Function Page New Game Select
        self.ui.btn_play_white.clicked.connect(
            lambda: self.newGame("w", False))
        self.ui.btn_play_black.clicked.connect(
            lambda: self.newGame("b", False))
        self.ui.btn_random.clicked.connect(
            lambda: self.newGame(random.choice(["w", "b"]), True))
        self.ui.btn_computer.clicked.connect(lambda: self.newGame(None, True))

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
        self.ui.btn_capture_detect.clicked.connect(self.capture_camera)

        # Function Page Setup
        self.ui.duck_layout.addWidget(self.labelPic)
        self.ui.camera_set_layout.addWidget(self.cam_set_label)
        self.ui.btn_send_startstop.clicked.connect(self.sendStartStop)
        self.ui.btn_send_home.clicked.connect(self.sendsetHome)
        self.ui.btn_send_joint.clicked.connect(self.sendJoint)
        self.ui.btn_send_xyz.clicked.connect(self.sendxyz)
        self.ui.btn_send_grip_open.clicked.connect(self.sendGripOpen)
        self.ui.btn_send_grip_close.clicked.connect(self.sendGripClose)
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
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))

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

    def pageProcess(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_all_process)
        UIFunctions.labelPage(self, "On Process")

    ## ==> END ##

    ########################################################################
    # START ==> SETUP FUNCTION
    ########################################################################
    def updateAngulaJoint_1_toText(self, value):
        self.ui.value_angular_joint_1.setValue(value)
        # print(type(value))

    def updateAngulaJoint_1_toSilder(self, value):
        self.ui.horizontalSlider_joint_1.setValue(value)
        # print(type(self.ui.value_angular_joint_1.value()))
        # self.AngulaJoint_1 = int(self.ui.value_angular_joint_1.text())
        # self.ui.horizontalSlider_joint_1.setValue(self.AngulaJoint_1)

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
            startstop_1, startstop_2, startstop_3, startstop_4)

    def sendsetHome(self):
        ISUS_UART.Home_Configulation(1, 1, 1, 1)

    def sendJoint(self):
        self.sendStartStop()
        joint_1 = self.ui.value_angular_joint_1.value()
        joint_2 = self.ui.value_angular_joint_2.value()
        joint_3 = self.ui.value_angular_joint_3.value()
        joint_4 = self.ui.value_angular_joint_4.value()
        ISUS_UART.Joint_Move(joint_1, joint_2, joint_3, joint_4)

    def sendxyz(self):
        self.sendStartStop()
        x = self.ui.value_x.value()
        y = self.ui.value_y.value()
        z = self.ui.value_z.value()
        ISUS_UART.XYZ_Move(x, y, z, 0)

    def sendGripOpen(self):
        ISUS_UART.Grip_Chess(55)

    def sendGripClose(self):
        ISUS_UART.Grip_Chess(0)

    def sendChess_Pick(self):
        rowi = (self.ui.value_pick.text())[0]
        print(rowi)
        columni = int((self.ui.value_pick.text())[1])
        print(columni)
        rowf = (self.ui.value_place.text())[0]
        print(rowf)
        columnf = int((self.ui.value_place.text())[1])
        print(columnf)
        # ISUS_UART.Chess_Pick(self, rowi, columni, rowf, columnf, name)

    ## ==> END ##

    ########################################################################
    # START ==> CHESS FUNCTION
    ########################################################################

    def chooseSide(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_newgame_select)
        UIFunctions.labelPage(self, "Choose Side")

    def newGame(self, colour, agent_play):
        self.info.move_frame.clear_moves()
        self.board.set_fen(setting_chess.starting_fen)
        self.board.agent_play = agent_play
        if self.board.agent_play:
            print("y")
            print(colour)
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
            _, self.image_top = copy.deepcopy(
                self.capture1.read())
            self.image_top = np.array(self.image_top)
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
            _, self.image_side = copy.deepcopy(
                self.capture2.read())
            self.image_side = np.array(self.image_side)
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

    def capture_camera(self):
        # self.setup_camera1(self.cam1_detect_label)
        # self.setup_camera2(self.cam2_detect_label)
        # print("evaluate chess pieces")
        # print(self.image_side)
        # cv2.imwrite('image_side.jpg', self.image_side)
        # cv2.imwrite('image_top.jpg', self.image_top)
        # fen = main_detection.main_chess_piece(self.image_top, self.image_side)
        # fen = '8/6n1/pp4p1/4p1p1/6p1/8/8/R4r1r'
        fen = None
        if fen != None:
            self.ui.status_fen_detect.setText(fen)
            self.ui.status_detect.setText('Detected!')
        else:
            self.ui.status_fen_detect.setText('Value')
            self.ui.status_detect.setText('sad')
        print(fen)
        self.board_detect.set_fen(fen)

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
    app = QApplication(sys.argv)
    # ISUS_UART = Serial_Comunication_ISUS.Uart_ISUS()
    # ISUS_UART.setupUart()
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
