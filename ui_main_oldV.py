# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE_newSize.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font5 = QFont()
        font5.setPointSize(8)
        self.stackedWidget.setFont(font5)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(40)
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.label_8 = QLabel(self.page_home)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_8)

        self.frame_17 = QFrame(self.page_home)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btn_page_process = QPushButton(self.frame_17)
        self.btn_page_process.setObjectName(u"btn_page_process")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_page_process.sizePolicy().hasHeightForWidth())
        self.btn_page_process.setSizePolicy(sizePolicy5)
        self.btn_page_process.setMinimumSize(QSize(240, 60))
        self.btn_page_process.setMaximumSize(QSize(300, 60))
        font7 = QFont()
        font7.setPointSize(18)
        self.btn_page_process.setFont(font7)
        self.btn_page_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_page_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_17.addWidget(self.btn_page_process)


        self.verticalLayout_10.addWidget(self.frame_17)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(14)
        self.label.setFont(font8)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.label_7 = QLabel(self.page_home)
        self.label_7.setObjectName(u"label_7")
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(15)
        self.label_7.setFont(font9)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_home)
        self.page_all_process = QWidget()
        self.page_all_process.setObjectName(u"page_all_process")
        self.horizontalLayout_20 = QHBoxLayout(self.page_all_process)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_18 = QFrame(self.page_all_process)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.chessBoard_detect_frame_2 = QFrame(self.frame_18)
        self.chessBoard_detect_frame_2.setObjectName(u"chessBoard_detect_frame_2")
        self.chessBoard_detect_frame_2.setGeometry(QRect(0, 0, 536, 758))
        self.chessBoard_detect_frame_2.setFrameShape(QFrame.StyledPanel)
        self.chessBoard_detect_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_7 = QWidget(self.chessBoard_detect_frame_2)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(0, 0, 531, 351))
        self.camera1_process_layout = QVBoxLayout(self.verticalLayoutWidget_7)
        self.camera1_process_layout.setObjectName(u"camera1_process_layout")
        self.camera1_process_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_10 = QWidget(self.chessBoard_detect_frame_2)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(60, 350, 371, 371))
        self.chessBoard_process_layout = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.chessBoard_process_layout.setObjectName(u"chessBoard_process_layout")
        self.chessBoard_process_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_11 = QWidget(self.chessBoard_detect_frame_2)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(60, 720, 371, 31))
        self.horizontalLayout_23 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_91 = QLabel(self.horizontalLayoutWidget_11)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setFont(font5)

        self.horizontalLayout_23.addWidget(self.label_91)

        self.label_92 = QLabel(self.horizontalLayoutWidget_11)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font5)

        self.horizontalLayout_23.addWidget(self.label_92)

        self.label_93 = QLabel(self.horizontalLayoutWidget_11)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font5)

        self.horizontalLayout_23.addWidget(self.label_93)

        self.label_94 = QLabel(self.horizontalLayoutWidget_11)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font5)

        self.horizontalLayout_23.addWidget(self.label_94)

        self.label_95 = QLabel(self.horizontalLayoutWidget_11)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setFont(font5)

        self.horizontalLayout_23.addWidget(self.label_95)

        self.label_96 = QLabel(self.horizontalLayoutWidget_11)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setFont(font5)

        self.horizontalLayout_23.addWidget(self.label_96)

        self.label_98 = QLabel(self.horizontalLayoutWidget_11)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setFont(font5)

        self.horizontalLayout_23.addWidget(self.label_98)

        self.label_99 = QLabel(self.horizontalLayoutWidget_11)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setFont(font5)

        self.horizontalLayout_23.addWidget(self.label_99)

        self.verticalLayoutWidget_8 = QWidget(self.chessBoard_detect_frame_2)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(30, 350, 31, 371))
        self.verticalLayout_26 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_100 = QLabel(self.verticalLayoutWidget_8)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setFont(font5)
        self.label_100.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_26.addWidget(self.label_100)

        self.label_101 = QLabel(self.verticalLayoutWidget_8)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setFont(font5)

        self.verticalLayout_26.addWidget(self.label_101)

        self.label_102 = QLabel(self.verticalLayoutWidget_8)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setFont(font5)

        self.verticalLayout_26.addWidget(self.label_102)

        self.label_103 = QLabel(self.verticalLayoutWidget_8)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setFont(font5)

        self.verticalLayout_26.addWidget(self.label_103)

        self.label_104 = QLabel(self.verticalLayoutWidget_8)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setFont(font5)

        self.verticalLayout_26.addWidget(self.label_104)

        self.label_105 = QLabel(self.verticalLayoutWidget_8)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setFont(font5)

        self.verticalLayout_26.addWidget(self.label_105)

        self.label_106 = QLabel(self.verticalLayoutWidget_8)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setFont(font5)

        self.verticalLayout_26.addWidget(self.label_106)

        self.label_107 = QLabel(self.verticalLayoutWidget_8)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setFont(font5)

        self.verticalLayout_26.addWidget(self.label_107)


        self.verticalLayout_24.addWidget(self.frame_18)


        self.horizontalLayout_20.addLayout(self.verticalLayout_24)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_19 = QFrame(self.page_all_process)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(5, 360, 521, 391))
        self.frame_20.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_4 = QFrame(self.frame_20)
        self.frame_title_wid_4.setObjectName(u"frame_title_wid_4")
        self.frame_title_wid_4.setGeometry(QRect(0, 0, 521, 35))
        self.frame_title_wid_4.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_4.setStyleSheet(u"background-color: rgb(30, 35, 40);")
        self.frame_title_wid_4.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_title_wid_4)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.labelBoxBlenderInstalation_4 = QLabel(self.frame_title_wid_4)
        self.labelBoxBlenderInstalation_4.setObjectName(u"labelBoxBlenderInstalation_4")
        self.labelBoxBlenderInstalation_4.setFont(font1)
        self.labelBoxBlenderInstalation_4.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.labelBoxBlenderInstalation_4)

        self.btn_send_grip_close_process = QPushButton(self.frame_20)
        self.btn_send_grip_close_process.setObjectName(u"btn_send_grip_close_process")
        self.btn_send_grip_close_process.setGeometry(QRect(180, 340, 160, 35))
        sizePolicy5.setHeightForWidth(self.btn_send_grip_close_process.sizePolicy().hasHeightForWidth())
        self.btn_send_grip_close_process.setSizePolicy(sizePolicy5)
        self.btn_send_grip_close_process.setMinimumSize(QSize(100, 20))
        self.btn_send_grip_close_process.setMaximumSize(QSize(300, 50))
        font10 = QFont()
        font10.setPointSize(9)
        self.btn_send_grip_close_process.setFont(font10)
        self.btn_send_grip_close_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_grip_close_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_send_grip_open_process = QPushButton(self.frame_20)
        self.btn_send_grip_open_process.setObjectName(u"btn_send_grip_open_process")
        self.btn_send_grip_open_process.setGeometry(QRect(10, 340, 160, 35))
        sizePolicy5.setHeightForWidth(self.btn_send_grip_open_process.sizePolicy().hasHeightForWidth())
        self.btn_send_grip_open_process.setSizePolicy(sizePolicy5)
        self.btn_send_grip_open_process.setMinimumSize(QSize(100, 20))
        self.btn_send_grip_open_process.setMaximumSize(QSize(300, 50))
        self.btn_send_grip_open_process.setFont(font10)
        self.btn_send_grip_open_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_grip_open_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_send_startstop_process = QPushButton(self.frame_20)
        self.btn_send_startstop_process.setObjectName(u"btn_send_startstop_process")
        self.btn_send_startstop_process.setGeometry(QRect(10, 240, 160, 35))
        sizePolicy5.setHeightForWidth(self.btn_send_startstop_process.sizePolicy().hasHeightForWidth())
        self.btn_send_startstop_process.setSizePolicy(sizePolicy5)
        self.btn_send_startstop_process.setMinimumSize(QSize(100, 20))
        self.btn_send_startstop_process.setMaximumSize(QSize(300, 50))
        self.btn_send_startstop_process.setFont(font10)
        self.btn_send_startstop_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_startstop_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_send_chess_home_process = QPushButton(self.frame_20)
        self.btn_send_chess_home_process.setObjectName(u"btn_send_chess_home_process")
        self.btn_send_chess_home_process.setGeometry(QRect(10, 290, 160, 35))
        sizePolicy5.setHeightForWidth(self.btn_send_chess_home_process.sizePolicy().hasHeightForWidth())
        self.btn_send_chess_home_process.setSizePolicy(sizePolicy5)
        self.btn_send_chess_home_process.setMinimumSize(QSize(100, 20))
        self.btn_send_chess_home_process.setMaximumSize(QSize(300, 50))
        self.btn_send_chess_home_process.setFont(font10)
        self.btn_send_chess_home_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_chess_home_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_send_home_process = QPushButton(self.frame_20)
        self.btn_send_home_process.setObjectName(u"btn_send_home_process")
        self.btn_send_home_process.setGeometry(QRect(180, 240, 160, 35))
        sizePolicy5.setHeightForWidth(self.btn_send_home_process.sizePolicy().hasHeightForWidth())
        self.btn_send_home_process.setSizePolicy(sizePolicy5)
        self.btn_send_home_process.setMinimumSize(QSize(100, 20))
        self.btn_send_home_process.setMaximumSize(QSize(300, 50))
        self.btn_send_home_process.setFont(font10)
        self.btn_send_home_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_home_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_send_zero_field_process = QPushButton(self.frame_20)
        self.btn_send_zero_field_process.setObjectName(u"btn_send_zero_field_process")
        self.btn_send_zero_field_process.setGeometry(QRect(180, 290, 160, 35))
        sizePolicy5.setHeightForWidth(self.btn_send_zero_field_process.sizePolicy().hasHeightForWidth())
        self.btn_send_zero_field_process.setSizePolicy(sizePolicy5)
        self.btn_send_zero_field_process.setMinimumSize(QSize(100, 20))
        self.btn_send_zero_field_process.setMaximumSize(QSize(300, 50))
        self.btn_send_zero_field_process.setFont(font10)
        self.btn_send_zero_field_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_zero_field_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_open_camera_process = QPushButton(self.frame_20)
        self.btn_open_camera_process.setObjectName(u"btn_open_camera_process")
        self.btn_open_camera_process.setGeometry(QRect(350, 240, 160, 35))
        sizePolicy5.setHeightForWidth(self.btn_open_camera_process.sizePolicy().hasHeightForWidth())
        self.btn_open_camera_process.setSizePolicy(sizePolicy5)
        self.btn_open_camera_process.setMinimumSize(QSize(100, 20))
        self.btn_open_camera_process.setMaximumSize(QSize(300, 50))
        self.btn_open_camera_process.setFont(font10)
        self.btn_open_camera_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_open_camera_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_close_camera_process = QPushButton(self.frame_20)
        self.btn_close_camera_process.setObjectName(u"btn_close_camera_process")
        self.btn_close_camera_process.setGeometry(QRect(350, 290, 160, 35))
        sizePolicy5.setHeightForWidth(self.btn_close_camera_process.sizePolicy().hasHeightForWidth())
        self.btn_close_camera_process.setSizePolicy(sizePolicy5)
        self.btn_close_camera_process.setMinimumSize(QSize(100, 20))
        self.btn_close_camera_process.setMaximumSize(QSize(300, 50))
        self.btn_close_camera_process.setFont(font10)
        self.btn_close_camera_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_close_camera_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.status_process = QLineEdit(self.frame_20)
        self.status_process.setObjectName(u"status_process")
        self.status_process.setGeometry(QRect(20, 70, 200, 35))
        self.status_process.setMinimumSize(QSize(0, 20))
        font11 = QFont()
        font11.setPointSize(10)
        self.status_process.setFont(font11)
        self.status_process.setLayoutDirection(Qt.LeftToRight)
        self.status_process.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.status_process.setInputMethodHints(Qt.ImhDigitsOnly)
        self.status_process.setCursorPosition(5)
        self.status_process.setAlignment(Qt.AlignCenter)
        self.status_process.setReadOnly(True)
        self.labelBoxBlenderInstalation_5 = QLabel(self.frame_20)
        self.labelBoxBlenderInstalation_5.setObjectName(u"labelBoxBlenderInstalation_5")
        self.labelBoxBlenderInstalation_5.setGeometry(QRect(20, 40, 100, 30))
        self.labelBoxBlenderInstalation_5.setFont(font1)
        self.labelBoxBlenderInstalation_5.setStyleSheet(u"")
        self.btn_capture_process = QPushButton(self.frame_20)
        self.btn_capture_process.setObjectName(u"btn_capture_process")
        self.btn_capture_process.setGeometry(QRect(350, 340, 160, 35))
        sizePolicy5.setHeightForWidth(self.btn_capture_process.sizePolicy().hasHeightForWidth())
        self.btn_capture_process.setSizePolicy(sizePolicy5)
        self.btn_capture_process.setMinimumSize(QSize(100, 20))
        self.btn_capture_process.setMaximumSize(QSize(300, 50))
        self.btn_capture_process.setFont(font10)
        self.btn_capture_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_capture_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.labelBoxBlenderInstalation_9 = QLabel(self.frame_20)
        self.labelBoxBlenderInstalation_9.setObjectName(u"labelBoxBlenderInstalation_9")
        self.labelBoxBlenderInstalation_9.setGeometry(QRect(20, 110, 100, 30))
        self.labelBoxBlenderInstalation_9.setFont(font1)
        self.labelBoxBlenderInstalation_9.setStyleSheet(u"")
        self.status_fen_process = QLineEdit(self.frame_20)
        self.status_fen_process.setObjectName(u"status_fen_process")
        self.status_fen_process.setGeometry(QRect(20, 140, 450, 40))
        self.status_fen_process.setMinimumSize(QSize(0, 20))
        self.status_fen_process.setFont(font11)
        self.status_fen_process.setLayoutDirection(Qt.LeftToRight)
        self.status_fen_process.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.status_fen_process.setInputMethodHints(Qt.ImhDigitsOnly)
        self.status_fen_process.setCursorPosition(5)
        self.status_fen_process.setAlignment(Qt.AlignCenter)
        self.status_fen_process.setReadOnly(True)
        self.status_turn_process = QLineEdit(self.frame_20)
        self.status_turn_process.setObjectName(u"status_turn_process")
        self.status_turn_process.setGeometry(QRect(230, 70, 131, 35))
        self.status_turn_process.setMinimumSize(QSize(0, 20))
        self.status_turn_process.setFont(font11)
        self.status_turn_process.setLayoutDirection(Qt.LeftToRight)
        self.status_turn_process.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.status_turn_process.setInputMethodHints(Qt.ImhDigitsOnly)
        self.status_turn_process.setCursorPosition(5)
        self.status_turn_process.setAlignment(Qt.AlignCenter)
        self.status_turn_process.setReadOnly(True)
        self.labelBoxBlenderInstalation_10 = QLabel(self.frame_20)
        self.labelBoxBlenderInstalation_10.setObjectName(u"labelBoxBlenderInstalation_10")
        self.labelBoxBlenderInstalation_10.setGeometry(QRect(230, 40, 100, 30))
        self.labelBoxBlenderInstalation_10.setFont(font1)
        self.labelBoxBlenderInstalation_10.setStyleSheet(u"")
        self.btn_reset_process = QPushButton(self.frame_20)
        self.btn_reset_process.setObjectName(u"btn_reset_process")
        self.btn_reset_process.setGeometry(QRect(180, 190, 120, 30))
        sizePolicy5.setHeightForWidth(self.btn_reset_process.sizePolicy().hasHeightForWidth())
        self.btn_reset_process.setSizePolicy(sizePolicy5)
        self.btn_reset_process.setMinimumSize(QSize(100, 20))
        self.btn_reset_process.setMaximumSize(QSize(300, 50))
        self.btn_reset_process.setFont(font5)
        self.btn_reset_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_reset_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.labelBoxBlenderInstalation_11 = QLabel(self.frame_20)
        self.labelBoxBlenderInstalation_11.setObjectName(u"labelBoxBlenderInstalation_11")
        self.labelBoxBlenderInstalation_11.setGeometry(QRect(370, 40, 120, 30))
        self.labelBoxBlenderInstalation_11.setFont(font1)
        self.labelBoxBlenderInstalation_11.setStyleSheet(u"")
        self.status_time_process = QLineEdit(self.frame_20)
        self.status_time_process.setObjectName(u"status_time_process")
        self.status_time_process.setGeometry(QRect(370, 70, 131, 35))
        self.status_time_process.setMinimumSize(QSize(0, 20))
        self.status_time_process.setFont(font11)
        self.status_time_process.setLayoutDirection(Qt.LeftToRight)
        self.status_time_process.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.status_time_process.setInputMethodHints(Qt.ImhDigitsOnly)
        self.status_time_process.setCursorPosition(5)
        self.status_time_process.setAlignment(Qt.AlignCenter)
        self.status_time_process.setReadOnly(True)
        self.btn_start_process = QPushButton(self.frame_20)
        self.btn_start_process.setObjectName(u"btn_start_process")
        self.btn_start_process.setGeometry(QRect(10, 190, 160, 35))
        sizePolicy5.setHeightForWidth(self.btn_start_process.sizePolicy().hasHeightForWidth())
        self.btn_start_process.setSizePolicy(sizePolicy5)
        self.btn_start_process.setMinimumSize(QSize(100, 20))
        self.btn_start_process.setMaximumSize(QSize(300, 50))
        self.btn_start_process.setFont(font10)
        self.btn_start_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_start_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.frame_title_wid_4.raise_()
        self.btn_send_grip_close_process.raise_()
        self.btn_send_grip_open_process.raise_()
        self.btn_send_startstop_process.raise_()
        self.btn_send_chess_home_process.raise_()
        self.btn_send_home_process.raise_()
        self.btn_send_zero_field_process.raise_()
        self.btn_open_camera_process.raise_()
        self.btn_close_camera_process.raise_()
        self.labelBoxBlenderInstalation_5.raise_()
        self.status_process.raise_()
        self.btn_capture_process.raise_()
        self.labelBoxBlenderInstalation_9.raise_()
        self.status_fen_process.raise_()
        self.status_turn_process.raise_()
        self.labelBoxBlenderInstalation_10.raise_()
        self.btn_reset_process.raise_()
        self.labelBoxBlenderInstalation_11.raise_()
        self.status_time_process.raise_()
        self.btn_start_process.raise_()
        self.verticalLayoutWidget_9 = QWidget(self.frame_19)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(0, 0, 531, 351))
        self.camera2_process_layout = QVBoxLayout(self.verticalLayoutWidget_9)
        self.camera2_process_layout.setObjectName(u"camera2_process_layout")
        self.camera2_process_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_19.addWidget(self.frame_19)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_19)

        self.stackedWidget.addWidget(self.page_all_process)
        self.page_select_process = QWidget()
        self.page_select_process.setObjectName(u"page_select_process")
        self.verticalLayout_30 = QVBoxLayout(self.page_select_process)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_75 = QLabel(self.page_select_process)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMaximumSize(QSize(16777215, 150))
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(32)
        self.label_75.setFont(font12)
        self.label_75.setStyleSheet(u"")
        self.label_75.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_75)

        self.frame_21 = QFrame(self.page_select_process)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_21)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 150))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.btn_play_white_process = QPushButton(self.frame_23)
        self.btn_play_white_process.setObjectName(u"btn_play_white_process")
        sizePolicy5.setHeightForWidth(self.btn_play_white_process.sizePolicy().hasHeightForWidth())
        self.btn_play_white_process.setSizePolicy(sizePolicy5)
        self.btn_play_white_process.setMinimumSize(QSize(100, 50))
        self.btn_play_white_process.setMaximumSize(QSize(300, 80))
        font13 = QFont()
        font13.setPointSize(16)
        self.btn_play_white_process.setFont(font13)
        self.btn_play_white_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_play_white_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/chessMenu/chess-white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play_white_process.setIcon(icon3)
        self.btn_play_white_process.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.btn_play_white_process)

        self.btn_play_black_process = QPushButton(self.frame_23)
        self.btn_play_black_process.setObjectName(u"btn_play_black_process")
        sizePolicy5.setHeightForWidth(self.btn_play_black_process.sizePolicy().hasHeightForWidth())
        self.btn_play_black_process.setSizePolicy(sizePolicy5)
        self.btn_play_black_process.setMinimumSize(QSize(100, 50))
        self.btn_play_black_process.setMaximumSize(QSize(300, 80))
        self.btn_play_black_process.setFont(font13)
        self.btn_play_black_process.setLayoutDirection(Qt.LeftToRight)
        self.btn_play_black_process.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/chessMenu/chess-black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play_black_process.setIcon(icon4)
        self.btn_play_black_process.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.btn_play_black_process)


        self.verticalLayout_25.addWidget(self.frame_23)


        self.verticalLayout_30.addWidget(self.frame_21)

        self.stackedWidget.addWidget(self.page_select_process)
        self.page_game = QWidget()
        self.page_game.setObjectName(u"page_game")
        self.verticalLayout_18 = QVBoxLayout(self.page_game)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_9 = QLabel(self.page_game)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 150))
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_9)

        self.frame_10 = QFrame(self.page_game)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_15 = QFrame(self.frame_10)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_15)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.btn_new_game = QPushButton(self.frame_15)
        self.btn_new_game.setObjectName(u"btn_new_game")
        sizePolicy5.setHeightForWidth(self.btn_new_game.sizePolicy().hasHeightForWidth())
        self.btn_new_game.setSizePolicy(sizePolicy5)
        self.btn_new_game.setMinimumSize(QSize(240, 60))
        self.btn_new_game.setMaximumSize(QSize(300, 60))
        self.btn_new_game.setFont(font7)
        self.btn_new_game.setLayoutDirection(Qt.LeftToRight)
        self.btn_new_game.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.verticalLayout_23.addWidget(self.btn_new_game)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 50))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_23.addWidget(self.frame_16)


        self.verticalLayout_22.addWidget(self.frame_15, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_18.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.page_game)
        self.page_newgame_select = QWidget()
        self.page_newgame_select.setObjectName(u"page_newgame_select")
        self.verticalLayout_19 = QVBoxLayout(self.page_newgame_select)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_10 = QLabel(self.page_newgame_select)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 150))
        self.label_10.setFont(font12)
        self.label_10.setStyleSheet(u"")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_10)

        self.frame_11 = QFrame(self.page_newgame_select)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_11)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 150))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_play_white = QPushButton(self.frame_12)
        self.btn_play_white.setObjectName(u"btn_play_white")
        sizePolicy5.setHeightForWidth(self.btn_play_white.sizePolicy().hasHeightForWidth())
        self.btn_play_white.setSizePolicy(sizePolicy5)
        self.btn_play_white.setMinimumSize(QSize(100, 50))
        self.btn_play_white.setMaximumSize(QSize(200, 60))
        self.btn_play_white.setFont(font13)
        self.btn_play_white.setLayoutDirection(Qt.LeftToRight)
        self.btn_play_white.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_play_white.setIcon(icon3)
        self.btn_play_white.setIconSize(QSize(32, 32))

        self.horizontalLayout_13.addWidget(self.btn_play_white)

        self.btn_play_black = QPushButton(self.frame_12)
        self.btn_play_black.setObjectName(u"btn_play_black")
        sizePolicy5.setHeightForWidth(self.btn_play_black.sizePolicy().hasHeightForWidth())
        self.btn_play_black.setSizePolicy(sizePolicy5)
        self.btn_play_black.setMinimumSize(QSize(100, 50))
        self.btn_play_black.setMaximumSize(QSize(200, 60))
        self.btn_play_black.setFont(font13)
        self.btn_play_black.setLayoutDirection(Qt.LeftToRight)
        self.btn_play_black.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_play_black.setIcon(icon4)
        self.btn_play_black.setIconSize(QSize(32, 32))

        self.horizontalLayout_13.addWidget(self.btn_play_black)


        self.verticalLayout_20.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_13)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.btn_random = QPushButton(self.frame_13)
        self.btn_random.setObjectName(u"btn_random")
        sizePolicy5.setHeightForWidth(self.btn_random.sizePolicy().hasHeightForWidth())
        self.btn_random.setSizePolicy(sizePolicy5)
        self.btn_random.setMinimumSize(QSize(400, 60))
        self.btn_random.setMaximumSize(QSize(400, 60))
        self.btn_random.setFont(font13)
        self.btn_random.setLayoutDirection(Qt.LeftToRight)
        self.btn_random.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/chessMenu/chess-random.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_random.setIcon(icon5)
        self.btn_random.setIconSize(QSize(32, 32))

        self.verticalLayout_21.addWidget(self.btn_random)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 50))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_21.addWidget(self.frame_14)


        self.verticalLayout_20.addWidget(self.frame_13, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_19.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.page_newgame_select)
        self.page_play_chess = QWidget()
        self.page_play_chess.setObjectName(u"page_play_chess")
        self.frame_5 = QFrame(self.page_play_chess)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 10, 1071, 761))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame_5)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(39, -1, 721, 721))
        self.game_layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.game_layout.setObjectName(u"game_layout")
        self.game_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget = QWidget(self.frame_5)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, -1, 41, 721))
        self.verticalLayout_14 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font11)
        self.label_12.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_14.addWidget(self.label_12)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_14.addWidget(self.label_11)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_14.addWidget(self.label_5)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_14.addWidget(self.label_4)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_14.addWidget(self.label_3)

        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_14.addWidget(self.label_14)

        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_14.addWidget(self.label_13)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_14.addWidget(self.label_2)

        self.horizontalLayoutWidget_5 = QWidget(self.frame_5)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(40, 720, 721, 41))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.horizontalLayoutWidget_5)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_16.addWidget(self.label_16)

        self.label_22 = QLabel(self.horizontalLayoutWidget_5)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_16.addWidget(self.label_22)

        self.label_21 = QLabel(self.horizontalLayoutWidget_5)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_16.addWidget(self.label_21)

        self.label_20 = QLabel(self.horizontalLayoutWidget_5)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_16.addWidget(self.label_20)

        self.label_19 = QLabel(self.horizontalLayoutWidget_5)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_16.addWidget(self.label_19)

        self.label_18 = QLabel(self.horizontalLayoutWidget_5)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_16.addWidget(self.label_18)

        self.label_17 = QLabel(self.horizontalLayoutWidget_5)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_16.addWidget(self.label_17)

        self.label_15 = QLabel(self.horizontalLayoutWidget_5)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_16.addWidget(self.label_15)

        self.frame_6 = QFrame(self.page_play_chess)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(780, 10, 301, 761))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget_2 = QWidget(self.frame_6)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 29, 301, 731))
        self.info_layout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.info_layout.setObjectName(u"info_layout")
        self.info_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_out_game = QPushButton(self.frame_6)
        self.btn_out_game.setObjectName(u"btn_out_game")
        self.btn_out_game.setGeometry(QRect(0, 0, 100, 20))
        sizePolicy5.setHeightForWidth(self.btn_out_game.sizePolicy().hasHeightForWidth())
        self.btn_out_game.setSizePolicy(sizePolicy5)
        self.btn_out_game.setMinimumSize(QSize(100, 20))
        self.btn_out_game.setMaximumSize(QSize(150, 20))
        self.btn_out_game.setLayoutDirection(Qt.LeftToRight)
        self.btn_out_game.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/16x16/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_out_game.setIcon(icon6)
        self.stackedWidget.addWidget(self.page_play_chess)
        self.page_detect = QWidget()
        self.page_detect.setObjectName(u"page_detect")
        self.horizontalLayout_15 = QHBoxLayout(self.page_detect)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.chessBoard_detect_frame = QFrame(self.page_detect)
        self.chessBoard_detect_frame.setObjectName(u"chessBoard_detect_frame")
        self.chessBoard_detect_frame.setFrameShape(QFrame.StyledPanel)
        self.chessBoard_detect_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_4 = QWidget(self.chessBoard_detect_frame)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 0, 531, 351))
        self.camera1_detect_layout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.camera1_detect_layout.setObjectName(u"camera1_detect_layout")
        self.camera1_detect_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_6 = QWidget(self.chessBoard_detect_frame)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(60, 350, 371, 371))
        self.chessBoard_detect_layout = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.chessBoard_detect_layout.setObjectName(u"chessBoard_detect_layout")
        self.chessBoard_detect_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_7 = QWidget(self.chessBoard_detect_frame)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(60, 720, 371, 31))
        self.horizontalLayout_18 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.horizontalLayoutWidget_7)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_35)

        self.label_36 = QLabel(self.horizontalLayoutWidget_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_36)

        self.label_37 = QLabel(self.horizontalLayoutWidget_7)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_37)

        self.label_38 = QLabel(self.horizontalLayoutWidget_7)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_38)

        self.label_39 = QLabel(self.horizontalLayoutWidget_7)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_39)

        self.label_40 = QLabel(self.horizontalLayoutWidget_7)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_40)

        self.label_41 = QLabel(self.horizontalLayoutWidget_7)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_41)

        self.label_42 = QLabel(self.horizontalLayoutWidget_7)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_42)

        self.verticalLayoutWidget_2 = QWidget(self.chessBoard_detect_frame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(30, 350, 31, 371))
        self.verticalLayout_16 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.verticalLayoutWidget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font5)
        self.label_23.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_16.addWidget(self.label_23)

        self.label_24 = QLabel(self.verticalLayoutWidget_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font5)

        self.verticalLayout_16.addWidget(self.label_24)

        self.label_25 = QLabel(self.verticalLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font5)

        self.verticalLayout_16.addWidget(self.label_25)

        self.label_27 = QLabel(self.verticalLayoutWidget_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font5)

        self.verticalLayout_16.addWidget(self.label_27)

        self.label_28 = QLabel(self.verticalLayoutWidget_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font5)

        self.verticalLayout_16.addWidget(self.label_28)

        self.label_30 = QLabel(self.verticalLayoutWidget_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font5)

        self.verticalLayout_16.addWidget(self.label_30)

        self.label_33 = QLabel(self.verticalLayoutWidget_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font5)

        self.verticalLayout_16.addWidget(self.label_33)

        self.label_34 = QLabel(self.verticalLayoutWidget_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font5)

        self.verticalLayout_16.addWidget(self.label_34)


        self.horizontalLayout_15.addWidget(self.chessBoard_detect_frame)

        self.camera_detect_layout = QVBoxLayout()
        self.camera_detect_layout.setObjectName(u"camera_detect_layout")
        self.verticalLayout_17 = QFrame(self.page_detect)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_17.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_3 = QWidget(self.verticalLayout_17)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 531, 351))
        self.camera2_detect_layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.camera2_detect_layout.setObjectName(u"camera2_detect_layout")
        self.camera2_detect_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.verticalLayout_17)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(20, 360, 496, 391))
        self.frame_22.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_5 = QFrame(self.frame_22)
        self.frame_title_wid_5.setObjectName(u"frame_title_wid_5")
        self.frame_title_wid_5.setGeometry(QRect(0, 0, 496, 35))
        self.frame_title_wid_5.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_5.setStyleSheet(u"background-color: rgb(30, 35, 40);")
        self.frame_title_wid_5.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_title_wid_5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.labelBoxBlenderInstalation_6 = QLabel(self.frame_title_wid_5)
        self.labelBoxBlenderInstalation_6.setObjectName(u"labelBoxBlenderInstalation_6")
        self.labelBoxBlenderInstalation_6.setFont(font1)
        self.labelBoxBlenderInstalation_6.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.labelBoxBlenderInstalation_6)

        self.status_detect = QLineEdit(self.frame_22)
        self.status_detect.setObjectName(u"status_detect")
        self.status_detect.setGeometry(QRect(50, 80, 200, 35))
        self.status_detect.setMinimumSize(QSize(0, 20))
        self.status_detect.setFont(font11)
        self.status_detect.setLayoutDirection(Qt.LeftToRight)
        self.status_detect.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.status_detect.setInputMethodHints(Qt.ImhDigitsOnly)
        self.status_detect.setCursorPosition(5)
        self.status_detect.setAlignment(Qt.AlignCenter)
        self.status_detect.setReadOnly(True)
        self.labelBoxBlenderInstalation_7 = QLabel(self.frame_22)
        self.labelBoxBlenderInstalation_7.setObjectName(u"labelBoxBlenderInstalation_7")
        self.labelBoxBlenderInstalation_7.setGeometry(QRect(50, 50, 100, 30))
        self.labelBoxBlenderInstalation_7.setFont(font1)
        self.labelBoxBlenderInstalation_7.setStyleSheet(u"")
        self.btn_open_camera_detect = QPushButton(self.frame_22)
        self.btn_open_camera_detect.setObjectName(u"btn_open_camera_detect")
        self.btn_open_camera_detect.setGeometry(QRect(300, 60, 160, 40))
        sizePolicy5.setHeightForWidth(self.btn_open_camera_detect.sizePolicy().hasHeightForWidth())
        self.btn_open_camera_detect.setSizePolicy(sizePolicy5)
        self.btn_open_camera_detect.setMinimumSize(QSize(160, 40))
        self.btn_open_camera_detect.setMaximumSize(QSize(300, 50))
        self.btn_open_camera_detect.setFont(font11)
        self.btn_open_camera_detect.setLayoutDirection(Qt.LeftToRight)
        self.btn_open_camera_detect.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_capture_detect = QPushButton(self.frame_22)
        self.btn_capture_detect.setObjectName(u"btn_capture_detect")
        self.btn_capture_detect.setGeometry(QRect(70, 130, 160, 40))
        sizePolicy5.setHeightForWidth(self.btn_capture_detect.sizePolicy().hasHeightForWidth())
        self.btn_capture_detect.setSizePolicy(sizePolicy5)
        self.btn_capture_detect.setMinimumSize(QSize(160, 40))
        self.btn_capture_detect.setMaximumSize(QSize(300, 50))
        self.btn_capture_detect.setFont(font11)
        self.btn_capture_detect.setLayoutDirection(Qt.LeftToRight)
        self.btn_capture_detect.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_close_camera_detect = QPushButton(self.frame_22)
        self.btn_close_camera_detect.setObjectName(u"btn_close_camera_detect")
        self.btn_close_camera_detect.setGeometry(QRect(300, 120, 160, 40))
        sizePolicy5.setHeightForWidth(self.btn_close_camera_detect.sizePolicy().hasHeightForWidth())
        self.btn_close_camera_detect.setSizePolicy(sizePolicy5)
        self.btn_close_camera_detect.setMinimumSize(QSize(160, 40))
        self.btn_close_camera_detect.setMaximumSize(QSize(300, 50))
        self.btn_close_camera_detect.setFont(font11)
        self.btn_close_camera_detect.setLayoutDirection(Qt.LeftToRight)
        self.btn_close_camera_detect.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.status_fen_detect = QLineEdit(self.frame_22)
        self.status_fen_detect.setObjectName(u"status_fen_detect")
        self.status_fen_detect.setGeometry(QRect(50, 250, 400, 40))
        self.status_fen_detect.setMinimumSize(QSize(0, 20))
        self.status_fen_detect.setFont(font11)
        self.status_fen_detect.setLayoutDirection(Qt.LeftToRight)
        self.status_fen_detect.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.status_fen_detect.setInputMethodHints(Qt.ImhDigitsOnly)
        self.status_fen_detect.setCursorPosition(5)
        self.status_fen_detect.setAlignment(Qt.AlignCenter)
        self.status_fen_detect.setReadOnly(True)
        self.labelBoxBlenderInstalation_8 = QLabel(self.frame_22)
        self.labelBoxBlenderInstalation_8.setObjectName(u"labelBoxBlenderInstalation_8")
        self.labelBoxBlenderInstalation_8.setGeometry(QRect(50, 220, 100, 30))
        self.labelBoxBlenderInstalation_8.setFont(font1)
        self.labelBoxBlenderInstalation_8.setStyleSheet(u"")
        self.btn_reset_detect = QPushButton(self.frame_22)
        self.btn_reset_detect.setObjectName(u"btn_reset_detect")
        self.btn_reset_detect.setGeometry(QRect(50, 300, 120, 30))
        sizePolicy5.setHeightForWidth(self.btn_reset_detect.sizePolicy().hasHeightForWidth())
        self.btn_reset_detect.setSizePolicy(sizePolicy5)
        self.btn_reset_detect.setMinimumSize(QSize(100, 20))
        self.btn_reset_detect.setMaximumSize(QSize(300, 50))
        self.btn_reset_detect.setFont(font5)
        self.btn_reset_detect.setLayoutDirection(Qt.LeftToRight)
        self.btn_reset_detect.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.camera_detect_layout.addWidget(self.verticalLayout_17)


        self.horizontalLayout_15.addLayout(self.camera_detect_layout)

        self.stackedWidget.addWidget(self.page_detect)
        self.page_run = QWidget()
        self.page_run.setObjectName(u"page_run")
        self.horizontalLayout_14 = QHBoxLayout(self.page_run)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_4 = QFrame(self.page_run)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(30, 30, 496, 711))
        self.frame_9.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_3 = QFrame(self.frame_9)
        self.frame_title_wid_3.setObjectName(u"frame_title_wid_3")
        self.frame_title_wid_3.setGeometry(QRect(0, 0, 496, 35))
        self.frame_title_wid_3.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_3.setStyleSheet(u"background-color: rgb(30, 35, 40);")
        self.frame_title_wid_3.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_title_wid_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.labelBoxBlenderInstalation_3 = QLabel(self.frame_title_wid_3)
        self.labelBoxBlenderInstalation_3.setObjectName(u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setFont(font1)
        self.labelBoxBlenderInstalation_3.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.labelBoxBlenderInstalation_3)

        self.label_26 = QLabel(self.frame_9)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 80, 40, 16))
        self.label_26.setFont(font5)
        self.btn_send_grip_close = QPushButton(self.frame_9)
        self.btn_send_grip_close.setObjectName(u"btn_send_grip_close")
        self.btn_send_grip_close.setGeometry(QRect(280, 650, 160, 40))
        sizePolicy5.setHeightForWidth(self.btn_send_grip_close.sizePolicy().hasHeightForWidth())
        self.btn_send_grip_close.setSizePolicy(sizePolicy5)
        self.btn_send_grip_close.setMinimumSize(QSize(160, 40))
        self.btn_send_grip_close.setMaximumSize(QSize(300, 50))
        self.btn_send_grip_close.setFont(font11)
        self.btn_send_grip_close.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_grip_close.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_send_grip_open = QPushButton(self.frame_9)
        self.btn_send_grip_open.setObjectName(u"btn_send_grip_open")
        self.btn_send_grip_open.setGeometry(QRect(70, 650, 160, 40))
        sizePolicy5.setHeightForWidth(self.btn_send_grip_open.sizePolicy().hasHeightForWidth())
        self.btn_send_grip_open.setSizePolicy(sizePolicy5)
        self.btn_send_grip_open.setMinimumSize(QSize(160, 40))
        self.btn_send_grip_open.setMaximumSize(QSize(300, 50))
        self.btn_send_grip_open.setFont(font11)
        self.btn_send_grip_open.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_grip_open.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.horizontalSlider_joint_1 = QSlider(self.frame_9)
        self.horizontalSlider_joint_1.setObjectName(u"horizontalSlider_joint_1")
        self.horizontalSlider_joint_1.setGeometry(QRect(260, 82, 180, 14))
        self.horizontalSlider_joint_1.setStyleSheet(u"/*QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove *\n"
"    border-radius: 3px;\n"
"}*/\n"
"QSlider::handle:horizontal {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	width: 10px;\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.horizontalSlider_joint_1.setMinimum(-180)
        self.horizontalSlider_joint_1.setMaximum(180)
        self.horizontalSlider_joint_1.setPageStep(10)
        self.horizontalSlider_joint_1.setOrientation(Qt.Horizontal)
        self.label_29 = QLabel(self.frame_9)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 120, 40, 16))
        self.label_29.setFont(font5)
        self.horizontalSlider_joint_2 = QSlider(self.frame_9)
        self.horizontalSlider_joint_2.setObjectName(u"horizontalSlider_joint_2")
        self.horizontalSlider_joint_2.setGeometry(QRect(260, 122, 180, 14))
        self.horizontalSlider_joint_2.setStyleSheet(u"/*QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove *\n"
"    border-radius: 3px;\n"
"}*/\n"
"QSlider::handle:horizontal {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	width: 10px;\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.horizontalSlider_joint_2.setMinimum(-180)
        self.horizontalSlider_joint_2.setMaximum(180)
        self.horizontalSlider_joint_2.setPageStep(10)
        self.horizontalSlider_joint_2.setOrientation(Qt.Horizontal)
        self.label_43 = QLabel(self.frame_9)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(20, 160, 40, 16))
        self.label_43.setFont(font5)
        self.label_44 = QLabel(self.frame_9)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(220, 80, 30, 16))
        self.label_44.setFont(font5)
        self.label_45 = QLabel(self.frame_9)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(450, 80, 25, 16))
        self.label_45.setFont(font5)
        self.label_46 = QLabel(self.frame_9)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(220, 120, 30, 16))
        self.label_46.setFont(font5)
        self.label_47 = QLabel(self.frame_9)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(450, 120, 25, 16))
        self.label_47.setFont(font5)
        self.checkBox_joint_1 = QCheckBox(self.frame_9)
        self.checkBox_joint_1.setObjectName(u"checkBox_joint_1")
        self.checkBox_joint_1.setGeometry(QRect(80, 78, 25, 22))
        self.checkBox_joint_2 = QCheckBox(self.frame_9)
        self.checkBox_joint_2.setObjectName(u"checkBox_joint_2")
        self.checkBox_joint_2.setGeometry(QRect(80, 118, 25, 22))
        self.label_48 = QLabel(self.frame_9)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(70, 50, 60, 16))
        self.checkBox_joint_3 = QCheckBox(self.frame_9)
        self.checkBox_joint_3.setObjectName(u"checkBox_joint_3")
        self.checkBox_joint_3.setGeometry(QRect(80, 158, 25, 22))
        self.label_49 = QLabel(self.frame_9)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(220, 160, 30, 16))
        self.label_49.setFont(font5)
        self.horizontalSlider_joint_3 = QSlider(self.frame_9)
        self.horizontalSlider_joint_3.setObjectName(u"horizontalSlider_joint_3")
        self.horizontalSlider_joint_3.setGeometry(QRect(260, 162, 180, 14))
        self.horizontalSlider_joint_3.setStyleSheet(u"/*QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove *\n"
"    border-radius: 3px;\n"
"}*/\n"
"QSlider::handle:horizontal {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	width: 10px;\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.horizontalSlider_joint_3.setMinimum(-180)
        self.horizontalSlider_joint_3.setMaximum(180)
        self.horizontalSlider_joint_3.setPageStep(10)
        self.horizontalSlider_joint_3.setOrientation(Qt.Horizontal)
        self.label_50 = QLabel(self.frame_9)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(450, 160, 25, 16))
        self.label_50.setFont(font5)
        self.label_51 = QLabel(self.frame_9)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(20, 200, 40, 16))
        self.label_51.setFont(font5)
        self.checkBox_joint_4 = QCheckBox(self.frame_9)
        self.checkBox_joint_4.setObjectName(u"checkBox_joint_4")
        self.checkBox_joint_4.setGeometry(QRect(80, 198, 25, 22))
        self.label_52 = QLabel(self.frame_9)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(220, 200, 30, 16))
        self.label_52.setFont(font5)
        self.horizontalSlider_joint_4 = QSlider(self.frame_9)
        self.horizontalSlider_joint_4.setObjectName(u"horizontalSlider_joint_4")
        self.horizontalSlider_joint_4.setGeometry(QRect(260, 202, 180, 14))
        self.horizontalSlider_joint_4.setStyleSheet(u"/*QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove *\n"
"    border-radius: 3px;\n"
"}*/\n"
"QSlider::handle:horizontal {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	width: 10px;\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.horizontalSlider_joint_4.setMinimum(-180)
        self.horizontalSlider_joint_4.setMaximum(180)
        self.horizontalSlider_joint_4.setPageStep(10)
        self.horizontalSlider_joint_4.setOrientation(Qt.Horizontal)
        self.label_53 = QLabel(self.frame_9)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(450, 200, 25, 16))
        self.label_53.setFont(font5)
        self.label_54 = QLabel(self.frame_9)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(30, 270, 40, 20))
        self.label_54.setFont(font11)
        self.horizontalSlider_x = QSlider(self.frame_9)
        self.horizontalSlider_x.setObjectName(u"horizontalSlider_x")
        self.horizontalSlider_x.setGeometry(QRect(240, 272, 200, 14))
        self.horizontalSlider_x.setStyleSheet(u"/*QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove *\n"
"    border-radius: 3px;\n"
"}*/\n"
"QSlider::handle:horizontal {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	width: 10px;\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.horizontalSlider_x.setMinimum(0)
        self.horizontalSlider_x.setMaximum(200)
        self.horizontalSlider_x.setPageStep(10)
        self.horizontalSlider_x.setOrientation(Qt.Horizontal)
        self.label_55 = QLabel(self.frame_9)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(220, 270, 15, 16))
        self.label_55.setFont(font5)
        self.label_56 = QLabel(self.frame_9)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(450, 270, 25, 16))
        self.label_56.setFont(font5)
        self.label_57 = QLabel(self.frame_9)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(140, 50, 60, 16))
        self.label_58 = QLabel(self.frame_9)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(150, 240, 50, 16))
        self.label_59 = QLabel(self.frame_9)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(30, 310, 40, 20))
        self.label_59.setFont(font11)
        self.label_60 = QLabel(self.frame_9)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(220, 310, 15, 16))
        self.label_60.setFont(font5)
        self.horizontalSlider_y = QSlider(self.frame_9)
        self.horizontalSlider_y.setObjectName(u"horizontalSlider_y")
        self.horizontalSlider_y.setGeometry(QRect(240, 312, 200, 14))
        self.horizontalSlider_y.setStyleSheet(u"/*QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove *\n"
"    border-radius: 3px;\n"
"}*/\n"
"QSlider::handle:horizontal {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	width: 10px;\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.horizontalSlider_y.setMinimum(0)
        self.horizontalSlider_y.setMaximum(200)
        self.horizontalSlider_y.setPageStep(10)
        self.horizontalSlider_y.setOrientation(Qt.Horizontal)
        self.label_61 = QLabel(self.frame_9)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(450, 310, 25, 16))
        self.label_61.setFont(font5)
        self.label_62 = QLabel(self.frame_9)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(30, 350, 40, 20))
        self.label_62.setFont(font11)
        self.label_63 = QLabel(self.frame_9)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(220, 350, 15, 16))
        self.label_63.setFont(font5)
        self.horizontalSlider_z = QSlider(self.frame_9)
        self.horizontalSlider_z.setObjectName(u"horizontalSlider_z")
        self.horizontalSlider_z.setGeometry(QRect(240, 352, 200, 14))
        self.horizontalSlider_z.setStyleSheet(u"/*QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove *\n"
"    border-radius: 3px;\n"
"}*/\n"
"QSlider::handle:horizontal {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	width: 10px;\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QSlider::handle:horizontal:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.horizontalSlider_z.setMinimum(0)
        self.horizontalSlider_z.setMaximum(200)
        self.horizontalSlider_z.setPageStep(10)
        self.horizontalSlider_z.setOrientation(Qt.Horizontal)
        self.label_64 = QLabel(self.frame_9)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(450, 350, 25, 16))
        self.label_64.setFont(font5)
        self.btn_send_startstop = QPushButton(self.frame_9)
        self.btn_send_startstop.setObjectName(u"btn_send_startstop")
        self.btn_send_startstop.setGeometry(QRect(70, 550, 160, 40))
        sizePolicy5.setHeightForWidth(self.btn_send_startstop.sizePolicy().hasHeightForWidth())
        self.btn_send_startstop.setSizePolicy(sizePolicy5)
        self.btn_send_startstop.setMinimumSize(QSize(160, 40))
        self.btn_send_startstop.setMaximumSize(QSize(300, 50))
        self.btn_send_startstop.setFont(font11)
        self.btn_send_startstop.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_startstop.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_send_joint = QPushButton(self.frame_9)
        self.btn_send_joint.setObjectName(u"btn_send_joint")
        self.btn_send_joint.setGeometry(QRect(70, 600, 160, 40))
        sizePolicy5.setHeightForWidth(self.btn_send_joint.sizePolicy().hasHeightForWidth())
        self.btn_send_joint.setSizePolicy(sizePolicy5)
        self.btn_send_joint.setMinimumSize(QSize(160, 40))
        self.btn_send_joint.setMaximumSize(QSize(300, 50))
        self.btn_send_joint.setFont(font11)
        self.btn_send_joint.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_joint.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_send_home = QPushButton(self.frame_9)
        self.btn_send_home.setObjectName(u"btn_send_home")
        self.btn_send_home.setGeometry(QRect(280, 550, 160, 40))
        sizePolicy5.setHeightForWidth(self.btn_send_home.sizePolicy().hasHeightForWidth())
        self.btn_send_home.setSizePolicy(sizePolicy5)
        self.btn_send_home.setMinimumSize(QSize(160, 40))
        self.btn_send_home.setMaximumSize(QSize(300, 50))
        self.btn_send_home.setFont(font11)
        self.btn_send_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_home.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_send_xyz = QPushButton(self.frame_9)
        self.btn_send_xyz.setObjectName(u"btn_send_xyz")
        self.btn_send_xyz.setGeometry(QRect(280, 600, 160, 40))
        sizePolicy5.setHeightForWidth(self.btn_send_xyz.sizePolicy().hasHeightForWidth())
        self.btn_send_xyz.setSizePolicy(sizePolicy5)
        self.btn_send_xyz.setMinimumSize(QSize(160, 40))
        self.btn_send_xyz.setMaximumSize(QSize(300, 50))
        self.btn_send_xyz.setFont(font11)
        self.btn_send_xyz.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_xyz.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.label_65 = QLabel(self.frame_9)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(70, 500, 120, 20))
        self.label_65.setFont(font11)
        self.value_angular_joint_1 = QDoubleSpinBox(self.frame_9)
        self.value_angular_joint_1.setObjectName(u"value_angular_joint_1")
        self.value_angular_joint_1.setGeometry(QRect(130, 80, 62, 22))
        self.value_angular_joint_1.setStyleSheet(u"QDoubleSpinBox {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QDoubleSpinBox:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.value_angular_joint_1.setDecimals(0)
        self.value_angular_joint_1.setMinimum(-180.000000000000000)
        self.value_angular_joint_1.setMaximum(360.000000000000000)
        self.value_angular_joint_2 = QDoubleSpinBox(self.frame_9)
        self.value_angular_joint_2.setObjectName(u"value_angular_joint_2")
        self.value_angular_joint_2.setGeometry(QRect(130, 120, 62, 22))
        self.value_angular_joint_2.setStyleSheet(u"QDoubleSpinBox {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QDoubleSpinBox:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.value_angular_joint_2.setDecimals(0)
        self.value_angular_joint_2.setMinimum(-180.000000000000000)
        self.value_angular_joint_2.setMaximum(360.000000000000000)
        self.value_angular_joint_3 = QDoubleSpinBox(self.frame_9)
        self.value_angular_joint_3.setObjectName(u"value_angular_joint_3")
        self.value_angular_joint_3.setGeometry(QRect(130, 160, 62, 22))
        self.value_angular_joint_3.setStyleSheet(u"QDoubleSpinBox {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QDoubleSpinBox:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.value_angular_joint_3.setDecimals(0)
        self.value_angular_joint_3.setMinimum(-180.000000000000000)
        self.value_angular_joint_3.setMaximum(360.000000000000000)
        self.value_angular_joint_4 = QDoubleSpinBox(self.frame_9)
        self.value_angular_joint_4.setObjectName(u"value_angular_joint_4")
        self.value_angular_joint_4.setGeometry(QRect(130, 200, 62, 22))
        self.value_angular_joint_4.setStyleSheet(u"QDoubleSpinBox {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QDoubleSpinBox:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.value_angular_joint_4.setDecimals(0)
        self.value_angular_joint_4.setMinimum(-180.000000000000000)
        self.value_angular_joint_4.setMaximum(360.000000000000000)
        self.value_x = QDoubleSpinBox(self.frame_9)
        self.value_x.setObjectName(u"value_x")
        self.value_x.setGeometry(QRect(130, 270, 62, 22))
        self.value_x.setStyleSheet(u"QDoubleSpinBox {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QDoubleSpinBox:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.value_x.setDecimals(0)
        self.value_x.setMinimum(-180.000000000000000)
        self.value_x.setMaximum(360.000000000000000)
        self.value_y = QDoubleSpinBox(self.frame_9)
        self.value_y.setObjectName(u"value_y")
        self.value_y.setGeometry(QRect(130, 310, 62, 22))
        self.value_y.setStyleSheet(u"QDoubleSpinBox {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QDoubleSpinBox:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.value_y.setDecimals(0)
        self.value_y.setMinimum(-180.000000000000000)
        self.value_y.setMaximum(360.000000000000000)
        self.value_z = QDoubleSpinBox(self.frame_9)
        self.value_z.setObjectName(u"value_z")
        self.value_z.setGeometry(QRect(130, 350, 62, 22))
        self.value_z.setStyleSheet(u"QDoubleSpinBox {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QDoubleSpinBox:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.value_z.setDecimals(0)
        self.value_z.setMinimum(-180.000000000000000)
        self.value_z.setMaximum(360.000000000000000)
        self.value_pick = QLineEdit(self.frame_9)
        self.value_pick.setObjectName(u"value_pick")
        self.value_pick.setEnabled(True)
        self.value_pick.setGeometry(QRect(130, 410, 80, 22))
        self.value_pick.setMinimumSize(QSize(0, 20))
        self.value_pick.setLayoutDirection(Qt.LeftToRight)
        self.value_pick.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.value_pick.setInputMethodHints(Qt.ImhDigitsOnly)
        self.value_pick.setCursorPosition(5)
        self.value_pick.setAlignment(Qt.AlignCenter)
        self.value_pick.setReadOnly(False)
        self.value_place = QLineEdit(self.frame_9)
        self.value_place.setObjectName(u"value_place")
        self.value_place.setEnabled(True)
        self.value_place.setGeometry(QRect(130, 450, 80, 22))
        self.value_place.setMinimumSize(QSize(0, 20))
        self.value_place.setLayoutDirection(Qt.LeftToRight)
        self.value_place.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.value_place.setInputMethodHints(Qt.ImhDigitsOnly)
        self.value_place.setCursorPosition(5)
        self.value_place.setAlignment(Qt.AlignCenter)
        self.value_place.setReadOnly(False)
        self.label_68 = QLabel(self.frame_9)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(40, 410, 40, 20))
        self.label_68.setFont(font11)
        self.label_70 = QLabel(self.frame_9)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(40, 450, 40, 20))
        self.label_70.setFont(font11)
        self.btn_send_pick_place = QPushButton(self.frame_9)
        self.btn_send_pick_place.setObjectName(u"btn_send_pick_place")
        self.btn_send_pick_place.setGeometry(QRect(290, 410, 150, 25))
        sizePolicy5.setHeightForWidth(self.btn_send_pick_place.sizePolicy().hasHeightForWidth())
        self.btn_send_pick_place.setSizePolicy(sizePolicy5)
        self.btn_send_pick_place.setMinimumSize(QSize(100, 20))
        self.btn_send_pick_place.setMaximumSize(QSize(300, 50))
        self.btn_send_pick_place.setFont(font10)
        self.btn_send_pick_place.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_pick_place.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_send_zero_field = QPushButton(self.frame_9)
        self.btn_send_zero_field.setObjectName(u"btn_send_zero_field")
        self.btn_send_zero_field.setGeometry(QRect(200, 500, 120, 30))
        sizePolicy5.setHeightForWidth(self.btn_send_zero_field.sizePolicy().hasHeightForWidth())
        self.btn_send_zero_field.setSizePolicy(sizePolicy5)
        self.btn_send_zero_field.setMinimumSize(QSize(100, 20))
        self.btn_send_zero_field.setMaximumSize(QSize(300, 50))
        self.btn_send_zero_field.setFont(font10)
        self.btn_send_zero_field.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_zero_field.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_send_chess_home = QPushButton(self.frame_9)
        self.btn_send_chess_home.setObjectName(u"btn_send_chess_home")
        self.btn_send_chess_home.setGeometry(QRect(340, 500, 120, 30))
        sizePolicy5.setHeightForWidth(self.btn_send_chess_home.sizePolicy().hasHeightForWidth())
        self.btn_send_chess_home.setSizePolicy(sizePolicy5)
        self.btn_send_chess_home.setMinimumSize(QSize(100, 20))
        self.btn_send_chess_home.setMaximumSize(QSize(300, 50))
        self.btn_send_chess_home.setFont(font11)
        self.btn_send_chess_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_chess_home.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.label_76 = QLabel(self.frame_9)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(240, 450, 40, 20))
        self.label_76.setFont(font11)
        self.comboBox_piece = QComboBox(self.frame_9)
        self.comboBox_piece.setObjectName(u"comboBox_piece")
        self.comboBox_piece.setGeometry(QRect(290, 440, 100, 30))

        self.horizontalLayout_14.addWidget(self.frame_4)

        self.frame_7 = QFrame(self.page_run)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(20, 30, 495, 390))
        self.frame_8.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_2 = QFrame(self.frame_8)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setEnabled(True)
        self.frame_title_wid_2.setGeometry(QRect(0, 0, 495, 35))
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setStyleSheet(u"background-color: rgb(30, 35, 40);")
        self.frame_title_wid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setFont(font1)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.labelBoxBlenderInstalation_2)

        self.feedback_angular_joint_2 = QLineEdit(self.frame_8)
        self.feedback_angular_joint_2.setObjectName(u"feedback_angular_joint_2")
        self.feedback_angular_joint_2.setGeometry(QRect(100, 120, 91, 21))
        self.feedback_angular_joint_2.setMinimumSize(QSize(0, 20))
        self.feedback_angular_joint_2.setLayoutDirection(Qt.LeftToRight)
        self.feedback_angular_joint_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.feedback_angular_joint_2.setInputMethodHints(Qt.ImhDigitsOnly)
        self.feedback_angular_joint_2.setCursorPosition(5)
        self.feedback_angular_joint_2.setAlignment(Qt.AlignCenter)
        self.feedback_angular_joint_2.setReadOnly(True)
        self.feedback_angular_joint_4 = QLineEdit(self.frame_8)
        self.feedback_angular_joint_4.setObjectName(u"feedback_angular_joint_4")
        self.feedback_angular_joint_4.setGeometry(QRect(100, 200, 91, 21))
        self.feedback_angular_joint_4.setMinimumSize(QSize(0, 20))
        self.feedback_angular_joint_4.setLayoutDirection(Qt.LeftToRight)
        self.feedback_angular_joint_4.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.feedback_angular_joint_4.setInputMethodHints(Qt.ImhDigitsOnly)
        self.feedback_angular_joint_4.setCursorPosition(5)
        self.feedback_angular_joint_4.setAlignment(Qt.AlignCenter)
        self.feedback_angular_joint_4.setReadOnly(True)
        self.feedback_angular_joint_3 = QLineEdit(self.frame_8)
        self.feedback_angular_joint_3.setObjectName(u"feedback_angular_joint_3")
        self.feedback_angular_joint_3.setEnabled(True)
        self.feedback_angular_joint_3.setGeometry(QRect(100, 160, 91, 21))
        self.feedback_angular_joint_3.setMinimumSize(QSize(0, 20))
        self.feedback_angular_joint_3.setLayoutDirection(Qt.LeftToRight)
        self.feedback_angular_joint_3.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.feedback_angular_joint_3.setInputMethodHints(Qt.ImhDigitsOnly)
        self.feedback_angular_joint_3.setCursorPosition(5)
        self.feedback_angular_joint_3.setAlignment(Qt.AlignCenter)
        self.feedback_angular_joint_3.setReadOnly(True)
        self.feedback_x = QLineEdit(self.frame_8)
        self.feedback_x.setObjectName(u"feedback_x")
        self.feedback_x.setEnabled(True)
        self.feedback_x.setGeometry(QRect(100, 270, 91, 21))
        self.feedback_x.setMinimumSize(QSize(0, 20))
        self.feedback_x.setLayoutDirection(Qt.LeftToRight)
        self.feedback_x.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.feedback_x.setInputMethodHints(Qt.ImhDigitsOnly)
        self.feedback_x.setCursorPosition(5)
        self.feedback_x.setAlignment(Qt.AlignCenter)
        self.feedback_x.setReadOnly(True)
        self.feedback_y = QLineEdit(self.frame_8)
        self.feedback_y.setObjectName(u"feedback_y")
        self.feedback_y.setGeometry(QRect(100, 310, 91, 21))
        self.feedback_y.setMinimumSize(QSize(0, 20))
        self.feedback_y.setLayoutDirection(Qt.LeftToRight)
        self.feedback_y.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.feedback_y.setInputMethodHints(Qt.ImhDigitsOnly)
        self.feedback_y.setCursorPosition(5)
        self.feedback_y.setAlignment(Qt.AlignCenter)
        self.feedback_y.setReadOnly(True)
        self.feedback_z = QLineEdit(self.frame_8)
        self.feedback_z.setObjectName(u"feedback_z")
        self.feedback_z.setEnabled(True)
        self.feedback_z.setGeometry(QRect(100, 350, 91, 21))
        self.feedback_z.setMinimumSize(QSize(0, 20))
        self.feedback_z.setLayoutDirection(Qt.LeftToRight)
        self.feedback_z.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.feedback_z.setInputMethodHints(Qt.ImhDigitsOnly)
        self.feedback_z.setCursorPosition(5)
        self.feedback_z.setAlignment(Qt.AlignCenter)
        self.feedback_z.setReadOnly(True)
        self.label_31 = QLabel(self.frame_8)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(40, 80, 40, 16))
        self.label_31.setFont(font5)
        self.label_32 = QLabel(self.frame_8)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(40, 120, 40, 16))
        self.label_32.setFont(font5)
        self.label_67 = QLabel(self.frame_8)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(120, 50, 60, 16))
        self.label_69 = QLabel(self.frame_8)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(40, 160, 40, 16))
        self.label_69.setFont(font5)
        self.label_71 = QLabel(self.frame_8)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(40, 200, 40, 16))
        self.label_71.setFont(font5)
        self.label_72 = QLabel(self.frame_8)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(50, 270, 40, 20))
        self.label_72.setFont(font11)
        self.label_73 = QLabel(self.frame_8)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(50, 310, 40, 20))
        self.label_73.setFont(font11)
        self.label_74 = QLabel(self.frame_8)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(50, 350, 40, 20))
        self.label_74.setFont(font11)
        self.label_66 = QLabel(self.frame_8)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(130, 240, 50, 16))
        self.horizontalLayoutWidget_3 = QWidget(self.frame_8)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(290, 140, 121, 121))
        self.duck_layout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.duck_layout.setObjectName(u"duck_layout")
        self.duck_layout.setContentsMargins(0, 0, 0, 0)
        self.feedback_angular_joint_1 = QLineEdit(self.frame_8)
        self.feedback_angular_joint_1.setObjectName(u"feedback_angular_joint_1")
        self.feedback_angular_joint_1.setGeometry(QRect(100, 80, 91, 21))
        self.feedback_angular_joint_1.setMinimumSize(QSize(0, 20))
        self.feedback_angular_joint_1.setLayoutDirection(Qt.LeftToRight)
        self.feedback_angular_joint_1.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.feedback_angular_joint_1.setInputMethodHints(Qt.ImhDigitsOnly)
        self.feedback_angular_joint_1.setCursorPosition(5)
        self.feedback_angular_joint_1.setAlignment(Qt.AlignCenter)
        self.feedback_angular_joint_1.setReadOnly(True)
        self.btn_open_camera_set = QPushButton(self.frame_8)
        self.btn_open_camera_set.setObjectName(u"btn_open_camera_set")
        self.btn_open_camera_set.setGeometry(QRect(270, 290, 160, 40))
        sizePolicy5.setHeightForWidth(self.btn_open_camera_set.sizePolicy().hasHeightForWidth())
        self.btn_open_camera_set.setSizePolicy(sizePolicy5)
        self.btn_open_camera_set.setMinimumSize(QSize(160, 40))
        self.btn_open_camera_set.setMaximumSize(QSize(300, 50))
        self.btn_open_camera_set.setFont(font11)
        self.btn_open_camera_set.setLayoutDirection(Qt.LeftToRight)
        self.btn_open_camera_set.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(199, 84, 80);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(199, 84, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 84, 80);\n"
"	border: 2px solid rgb(240, 84, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_close_camera_set = QPushButton(self.frame_8)
        self.btn_close_camera_set.setObjectName(u"btn_close_camera_set")
        self.btn_close_camera_set.setGeometry(QRect(270, 340, 160, 40))
        sizePolicy5.setHeightForWidth(self.btn_close_camera_set.sizePolicy().hasHeightForWidth())
        self.btn_close_camera_set.setSizePolicy(sizePolicy5)
        self.btn_close_camera_set.setMinimumSize(QSize(160, 40))
        self.btn_close_camera_set.setMaximumSize(QSize(300, 50))
        self.btn_close_camera_set.setFont(font11)
        self.btn_close_camera_set.setLayoutDirection(Qt.LeftToRight)
        self.btn_close_camera_set.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.horizontalLayoutWidget_4 = QWidget(self.frame_7)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(20, 430, 491, 311))
        self.camera_set_layout = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.camera_set_layout.setObjectName(u"camera_set_layout")
        self.camera_set_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_14.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_run)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        font14 = QFont()
        font14.setFamily(u"Segoe UI")
        font14.setPointSize(9)
        self.pushButton.setFont(font14)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon7)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.frame_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 323, 222))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font14)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy6)
        self.horizontalScrollBar.setStyleSheet(u"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.frame_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon8)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.frame_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.tableWidget.setPalette(palette1)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.verticalSlider)
        QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.commandLinkButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"G1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Robotics Studio", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Module 8-9 Group 1", None))
        self.btn_page_process.setText(QCoreApplication.translate("MainWindow", u"Start Process", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"----------------------------------------", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"click menu icon on the left", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">a</span></p></body></html>", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">b</span></p></body></html>", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">c</span></p></body></html>", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">d</span></p></body></html>", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">e</span></p></body></html>", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">f</span></p></body></html>", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">g</span></p></body></html>", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">h</span></p></body></html>", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">8</span></p></body></html>", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">7</span></p></body></html>", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">6</span></p></body></html>", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">5</span></p></body></html>", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">4</span></p></body></html>", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">3</span></p></body></html>", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">2</span></p></body></html>", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">1</span></p></body></html>", None))
        self.labelBoxBlenderInstalation_4.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.btn_send_grip_close_process.setText(QCoreApplication.translate("MainWindow", u"Gripper Close", None))
        self.btn_send_grip_open_process.setText(QCoreApplication.translate("MainWindow", u"Gripper Open", None))
        self.btn_send_startstop_process.setText(QCoreApplication.translate("MainWindow", u"Start/Stop", None))
        self.btn_send_chess_home_process.setText(QCoreApplication.translate("MainWindow", u"Chess Home", None))
        self.btn_send_home_process.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_send_zero_field_process.setText(QCoreApplication.translate("MainWindow", u"Set Zero Field", None))
        self.btn_open_camera_process.setText(QCoreApplication.translate("MainWindow", u"Open Camera", None))
        self.btn_close_camera_process.setText(QCoreApplication.translate("MainWindow", u"Close Camera", None))
        self.status_process.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.status_process.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.labelBoxBlenderInstalation_5.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.btn_capture_process.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.labelBoxBlenderInstalation_9.setText(QCoreApplication.translate("MainWindow", u"FEN", None))
        self.status_fen_process.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.status_fen_process.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.status_turn_process.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.status_turn_process.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.labelBoxBlenderInstalation_10.setText(QCoreApplication.translate("MainWindow", u"TURN", None))
        self.btn_reset_process.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.labelBoxBlenderInstalation_11.setText(QCoreApplication.translate("MainWindow", u"TIME PROCESS", None))
        self.status_time_process.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.status_time_process.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.btn_start_process.setText(QCoreApplication.translate("MainWindow", u"Start Process", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Choose side you want to play", None))
        self.btn_play_white_process.setText(QCoreApplication.translate("MainWindow", u" White", None))
        self.btn_play_black_process.setText(QCoreApplication.translate("MainWindow", u" Black", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Game Chess AI", None))
        self.btn_new_game.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Choose side you want to play", None))
        self.btn_play_white.setText(QCoreApplication.translate("MainWindow", u" White", None))
        self.btn_play_black.setText(QCoreApplication.translate("MainWindow", u" Black", None))
        self.btn_random.setText(QCoreApplication.translate("MainWindow", u" Random", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">8</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">7</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">6</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">5</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">4</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">3</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">2</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">1</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">a</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">b</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">c</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">d</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">e</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">f</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">g</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">h</span></p></body></html>", None))
        self.btn_out_game.setText(QCoreApplication.translate("MainWindow", u"back", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">a</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">b</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">c</span></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">d</span></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">e</span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">f</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">g</span></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">h</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">8</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">7</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">6</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">5</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">4</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">3</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">2</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">1</span></p></body></html>", None))
        self.labelBoxBlenderInstalation_6.setText(QCoreApplication.translate("MainWindow", u"SETUP & STATUS", None))
        self.status_detect.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.status_detect.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.labelBoxBlenderInstalation_7.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.btn_open_camera_detect.setText(QCoreApplication.translate("MainWindow", u"Open Camera", None))
        self.btn_capture_detect.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.btn_close_camera_detect.setText(QCoreApplication.translate("MainWindow", u"Close Camera", None))
        self.status_fen_detect.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.status_fen_detect.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.labelBoxBlenderInstalation_8.setText(QCoreApplication.translate("MainWindow", u"FEN", None))
        self.btn_reset_detect.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.labelBoxBlenderInstalation_3.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Joint 1", None))
        self.btn_send_grip_close.setText(QCoreApplication.translate("MainWindow", u"Gripper Close", None))
        self.btn_send_grip_open.setText(QCoreApplication.translate("MainWindow", u"Gripper Open", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Joint 2", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Joint 3", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"-180", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"360", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"-180", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"360", None))
        self.checkBox_joint_1.setText("")
        self.checkBox_joint_2.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Start/Stop", None))
        self.checkBox_joint_3.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"-180", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"360", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Joint 4", None))
        self.checkBox_joint_4.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"-180", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"360", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Degree", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"z", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.btn_send_startstop.setText(QCoreApplication.translate("MainWindow", u"Start/Stop", None))
        self.btn_send_joint.setText(QCoreApplication.translate("MainWindow", u"Joint ", None))
        self.btn_send_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_send_xyz.setText(QCoreApplication.translate("MainWindow", u"xyz", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Send Command", None))
        self.value_pick.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.value_pick.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.value_place.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.value_place.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Pick", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Place", None))
        self.btn_send_pick_place.setText(QCoreApplication.translate("MainWindow", u"PICK & PLACE", None))
        self.btn_send_zero_field.setText(QCoreApplication.translate("MainWindow", u"Set Zero Field", None))
        self.btn_send_chess_home.setText(QCoreApplication.translate("MainWindow", u"Chess Home", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Piece", None))
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.feedback_angular_joint_2.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.feedback_angular_joint_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.feedback_angular_joint_4.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.feedback_angular_joint_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.feedback_angular_joint_3.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.feedback_angular_joint_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.feedback_x.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.feedback_x.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.feedback_y.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.feedback_y.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.feedback_z.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.feedback_z.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Joint 1", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Joint 2", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Degree", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Joint 3", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Joint 4", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"z", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.feedback_angular_joint_1.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.feedback_angular_joint_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.btn_open_camera_set.setText(QCoreApplication.translate("MainWindow", u"Open Camera", None))
        self.btn_close_camera_set.setText(QCoreApplication.translate("MainWindow", u"Close Camera", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"BLENDER INSTALLATION", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Blender", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Ex: C:Program FilesBlender FoundationBlender 2.82 blender.exe", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Open External Link", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Registered by: G1 Module8-9", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v0.0.1", None))
    # retranslateUi

