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
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import serial
import chess
import random

# GUI FILE
from app_modules import *

# CHESS FILE
import setting_chess
from pychess.board import ChessBoard
# from pychess.info import Info

# COMUNICATION
from Comunication import Serial_Comunication_ISUS


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.saved_game = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.board = ChessBoard(self)
        # self.info = Info()

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

        self.labelPic = QtWidgets.QLabel(self)
        self.labelPic.setGeometry(QtCore.QRect(0, 0, 120, 120))
        self.labelPic.setObjectName("labelPic")
        self.labelPic.setPixmap(self.duck)

        # Function
        # self.ui.btn_pos_drive_3.clicked.connect(self.setMaximumAng)
        # self.ui.btn_pos_drive_5.clicked.connect(self.goStation)
        # self.ui.btn_pos_drive_4.clicked.connect(self.setStation)

        # Function Page Game
        self.ui.btn_new_game.clicked.connect(self.chooseSide)
        self.ui.btn_out_game.clicked.connect(self.backHomeGame)
        self.ui.game_layout.addWidget(self.board)
        # self.ui.info_layout.addWidget(self.info)

        # Function Page New Game Select
        self.ui.btn_play_white.clicked.connect(
            lambda: self.newGame("w", False))
        self.ui.btn_play_black.clicked.connect(
            lambda: self.newGame("b", False))
        self.ui.btn_random.clicked.connect(
            lambda: self.newGame(random.choice(["w", "b"]), True))
        self.ui.btn_computer.clicked.connect(lambda: self.newGame(None, True))

        # Function Page Setup
        self.ui.duck_layout.addWidget(self.labelPic)
        self.ui.btn_send_startstop.clicked.connect(self.sendStartStop)
        self.ui.btn_send_joint.clicked.connect(self.sendJoint)

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

        # PAGE NEW USER
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

    # def setMaximumAng(self):
    #     self.maxAngular = int(self.ui.targetx_4.text())
    #     if self.ser.isOpen():
    #         print("setMaxAng")
    #         self.ui.targetx_5.setText(str(self.maxAngular))
    #         self.ser.write([148, self.maxAngular, 255])

    # def setStation(self):
    #     self.station.clear()
    #     self.station.append(int(self.ui.targetx_7.text()))
    #     if self.ser.isOpen():
    #         print("setStation")
    #         self.ser.write([150, self.station[0], 255])

    # def goStation(self):
    #     if self.ser.isOpen():
    #         print("goStation")
    #         self.ser.write([152, 255])
    #         self.ui.targetx_6.setText(str(self.station[0]))

    # def setnStation(self):
    #     self.station.clear()
    #     a = self.ui.targetx_8.text()
    #     b = a.split()
    #     for i in b:
    #         self.station.append(i)
    #     self.station = int(self.ui.targetx_7.text())

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
        # print(int(self.ui.checkBox_joint_1.isChecked()))
        ISUS_UART.StartStop_Move(
            startstop_1, startstop_2, startstop_3, startstop_4)

    def sendJoint(self):
        # self.AngulaJoint_1 = int(self.ui.value_angular_joint_1.text())
        # print(str(self.AngulaJoint_1))
        # if self.ui.checkBox_joint_1.isChecked():
        #     joint_1 = self.ui.value_angular_joint_1.value()
        #     # print("y")
        # if self.ui.checkBox_joint_2.isChecked():
        #     joint_2 = self.ui.value_angular_joint_2.value()
        # self.ui.feedback_angular_joint_1.setText(str(self.AngulaJoint_1))
        self.sendStartStop()
        joint_1 = self.ui.value_angular_joint_1.value()
        joint_2 = self.ui.value_angular_joint_2.value()
        joint_3 = self.ui.value_angular_joint_3.value()
        joint_4 = self.ui.value_angular_joint_4.value()
        ISUS_UART.Joint_Move(joint_1, joint_2, joint_3, joint_4)

    ## ==> END ##

    ########################################################################
    # START ==> CHESS FUNCTION
    ########################################################################

    def chooseSide(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_newgame_select)
        UIFunctions.labelPage(self, "Choose Side")

    def newGame(self, colour, agent_play):
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
    ISUS_UART = Serial_Comunication_ISUS.Uart_ISUS()
    ISUS_UART.setupUart()
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
