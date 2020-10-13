# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.defi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from sign_in import create_db
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation

from netaddr import *

import sqlite3
from database import IP_DB



class Ui_IPSEARCH_window(object):        
        
        
#------------------import delle funzioni esterne----------------------------
    from whois_tool import whois_ip
    from abuse_tool import IPabuse
    from radar_tool import IP_geo
    from database import database_public_ip, database_private_ip, search_db_tool, IP_DB
    from sendresults import sendresults_whois, sendresults_abuse, sendresults_geo, message_send, sendresults_hunt
    from hunt import scan, whois_hunt, IPabuse_hunt, class_def, host_name, insert_publicdata, insert_data, look_vendor
    from sendhelp import send_dilemma, message_send_help
    from sign_in import login, sendmail, code_generator, verify,  register, already_exist, msgerror, sendmail_reset, reset_password, create_db
    
#--------------------------------------------------------------------------    
    
    def setupUi(self, IPSEARCH_window):
        IPSEARCH_window.setObjectName("IPSEARCH_window")
        IPSEARCH_window.resize(1220, 783)
        IPSEARCH_window.setMinimumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(IPSEARCH_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bar_up = QtWidgets.QFrame(self.centralwidget)
        self.bar_up.setMaximumSize(QtCore.QSize(16777215, 50))
        self.bar_up.setStyleSheet("background-color: rgb(42, 13, 48);")
        self.bar_up.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bar_up.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bar_up.setObjectName("bar_up")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bar_up)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.contein_button_menu = QtWidgets.QFrame(self.bar_up)
        self.contein_button_menu.setMinimumSize(QtCore.QSize(90, 0))
        self.contein_button_menu.setMaximumSize(QtCore.QSize(90, 50))
        self.contein_button_menu.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.contein_button_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_button_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_button_menu.setObjectName("contein_button_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.contein_button_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Menu_Button = QtWidgets.QPushButton(self.contein_button_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Menu_Button.sizePolicy().hasHeightForWidth())
        self.Menu_Button.setSizePolicy(sizePolicy)
        self.Menu_Button.setStyleSheet("\n"
"QFrame{\n"
"background-color : #000;\n"
"}\n"
"QPushButton{\n"
"    padding:20px 10px;\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: #000;\n"
"    \n"
"    background-position: center left;\n"
"    color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Menu_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Menu_Button.setIcon(icon)
        self.Menu_Button.setIconSize(QtCore.QSize(40, 50))
        self.Menu_Button.setObjectName("Menu_Button")
        self.verticalLayout_2.addWidget(self.Menu_Button)
        self.horizontalLayout.addWidget(self.contein_button_menu)
        #move bar menu
        #self.Menu_Button.hide()
        self.Menu_Button.clicked.connect(self.menu_appear)
        self.contein_IPHUNTER = QtWidgets.QFrame(self.bar_up)
        self.contein_IPHUNTER.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.contein_IPHUNTER.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_IPHUNTER.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_IPHUNTER.setObjectName("contein_IPHUNTER")
        self.IP_HUNTER_tittle = QtWidgets.QLabel(self.contein_IPHUNTER)
        self.IP_HUNTER_tittle.setGeometry(QtCore.QRect(0, 0, 800, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.IP_HUNTER_tittle.setFont(font)
        self.IP_HUNTER_tittle.setStyleSheet("color: rgb(136, 136, 136);")
        self.IP_HUNTER_tittle.setObjectName("IP_HUNTER_tittle")
        self.horizontalLayout.addWidget(self.contein_IPHUNTER)
        self.verticalLayout.addWidget(self.bar_up)
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.contein_left_menu = QtWidgets.QFrame(self.body)
        self.contein_left_menu.setMinimumSize(QtCore.QSize(40, 0))
        self.contein_left_menu.setMaximumSize(QtCore.QSize(40, 16777215))
        self.contein_left_menu.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.contein_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_left_menu.setObjectName("contein_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.contein_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.contein_left_menu_butttons = QtWidgets.QFrame(self.contein_left_menu)
        self.contein_left_menu_butttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contein_left_menu_butttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_left_menu_butttons.setObjectName("contein_left_menu_butttons")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.contein_left_menu_butttons)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.LOG_IN = QtWidgets.QPushButton(self.contein_left_menu_butttons)
        self.LOG_IN.setMinimumSize(QtCore.QSize(40, 40))
        self.LOG_IN.setStyleSheet("QFrame{\n"
"background-color : #000;\n"
"}\n"
"QPushButton{\n"
"    padding:20px 10px;\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: #000;\n"
"    padding-left:60px  ;\n"
"    background-position: center left;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(54, 3, 119);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/hexagonwhite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LOG_IN.setIcon(icon1)
        self.LOG_IN.setIconSize(QtCore.QSize(30, 20))
        self.LOG_IN.setObjectName("LOG_IN")
        self.verticalLayout_4.addWidget(self.LOG_IN)
        
        self.LOG_IN.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.LOG_IN_2))
        
        self.Home_IP_HUNTER = QtWidgets.QPushButton(self.contein_left_menu_butttons)
        self.Home_IP_HUNTER.setMinimumSize(QtCore.QSize(69, 40))
        self.Home_IP_HUNTER.setStyleSheet("QFrame{\n"
"background-color : #000;\n"
"}\n"
"QPushButton{\n"
"    padding:20px 10px;\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: #000;\n"
"    padding-left:25px  ;\n"
"    \n"
"    background-position: center left;\n"
"    \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/cil-home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home_IP_HUNTER.setIcon(icon2)
        self.Home_IP_HUNTER.setIconSize(QtCore.QSize(40, 30))
        self.Home_IP_HUNTER.setObjectName("Home_IP_HUNTER")
        self.verticalLayout_4.addWidget(self.Home_IP_HUNTER)
        #
        self.Home_IP_HUNTER.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_IP_HUNTER))
        self.WHOIS = QtWidgets.QPushButton(self.contein_left_menu_butttons)
        self.WHOIS.setMinimumSize(QtCore.QSize(40, 40))
        self.WHOIS.setStyleSheet("QFrame{\n"
"background-color : #000;\n"
"}\n"
"QPushButton{\n"
"    padding:20px 10px;\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: #000;\n"
"    padding-left:60px  ;\n"
"    background-position: center left;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.WHOIS.setIcon(icon1)
        self.WHOIS.setIconSize(QtCore.QSize(30, 20))
        self.WHOIS.setObjectName("WHOIS")
        self.verticalLayout_4.addWidget(self.WHOIS)
        #
        self.WHOIS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_WHOIS))
        self.ABUSE = QtWidgets.QPushButton(self.contein_left_menu_butttons)
        self.ABUSE.setMinimumSize(QtCore.QSize(40, 40))
        self.ABUSE.setStyleSheet("QFrame{\n"
"background-color : #000;\n"
"}\n"
"QPushButton{\n"
"    padding:20px 10px;\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: #000;\n"
"    padding-left:60px  ;\n"
"    background-position: center left;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.ABUSE.setIcon(icon1)
        self.ABUSE.setIconSize(QtCore.QSize(30, 20))
        self.ABUSE.setObjectName("ABUSE")
        self.verticalLayout_4.addWidget(self.ABUSE)
        #
        self.ABUSE.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_ABUSE))
        self.RADAR = QtWidgets.QPushButton(self.contein_left_menu_butttons)
        self.RADAR.setMinimumSize(QtCore.QSize(40, 40))
        self.RADAR.setStyleSheet("QFrame{\n"
"background-color : #000;\n"
"}\n"
"QPushButton{\n"
"    padding:20px 10px;\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: #000;\n"
"    padding-left:60px  ;\n"
"    background-position: center left;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.RADAR.setIcon(icon1)
        self.RADAR.setIconSize(QtCore.QSize(30, 20))
        self.RADAR.setObjectName("RADAR")
        self.verticalLayout_4.addWidget(self.RADAR)
        #
        
        self.RADAR.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_RADAR))
        self.SSL_SCAN = QtWidgets.QPushButton(self.contein_left_menu_butttons)
        self.SSL_SCAN.setMinimumSize(QtCore.QSize(40, 40))
        self.SSL_SCAN.setStyleSheet("QFrame{\n"
"background-color : #000;\n"
"}\n"
"QPushButton{\n"
"    padding:20px 10px;\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: #000;\n"
"    padding-left:75px  ;\n"
"    background-position: center left;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.SSL_SCAN.setIcon(icon1)
        self.SSL_SCAN.setIconSize(QtCore.QSize(30, 20))
        self.SSL_SCAN.setObjectName("SSL_SCAN")
        self.verticalLayout_4.addWidget(self.SSL_SCAN)
        #
        self.SSL_SCAN.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_SSL_SCAN))
        #self.SSL_SCAN.clicked.connect(lambda: self.RADAR.show())
        self.DATABASE = QtWidgets.QPushButton(self.contein_left_menu_butttons)
        self.DATABASE.setMinimumSize(QtCore.QSize(40, 40))
        self.DATABASE.setStyleSheet("QFrame{\n"
"background-color : #000;\n"
"}\n"
"QPushButton{\n"
"    padding:20px 10px;\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: #000;\n"
"    padding-left:79px  ;\n"
"    background-position: center left;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.DATABASE.setIcon(icon1)
        self.DATABASE.setIconSize(QtCore.QSize(30, 20))
        self.DATABASE.setObjectName("DATABASE")
        self.verticalLayout_4.addWidget(self.DATABASE)
        self.DATABASE.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_DATABASE_CHOICE))
        spacerItem = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.SETTINGS = QtWidgets.QPushButton(self.contein_left_menu_butttons)
        self.SETTINGS.setMinimumSize(QtCore.QSize(40, 40))
        self.SETTINGS.setStyleSheet("QFrame{\n"
"background-color : #000;\n"
"}\n"
"QPushButton{\n"
"    padding:20px 10px;\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: #000;\n"
"    padding-left:75px  ;\n"
"    background-position: center left;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/cil-settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SETTINGS.setIcon(icon3)
        self.SETTINGS.setIconSize(QtCore.QSize(30, 20))
        self.SETTINGS.setObjectName("SETTINGS")
        self.verticalLayout_4.addWidget(self.SETTINGS)
        self.SETTINGS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_SETTINGS))
        self.SEND_EMAIL = QtWidgets.QPushButton(self.contein_left_menu_butttons)
        self.SEND_EMAIL.setMinimumSize(QtCore.QSize(40, 40))
        self.SEND_EMAIL.setStyleSheet("QFrame{\n"
"background-color : #000;\n"
"}\n"
"QPushButton{\n"
"    padding:20px 10px;\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: #000;\n"
"    padding-left:41px  ;\n"
"    background-position: center left;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/cil-paper-plane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SEND_EMAIL.setIcon(icon4)
        self.SEND_EMAIL.setIconSize(QtCore.QSize(30, 20))
        self.SEND_EMAIL.setObjectName("SEND_EMAIL")
        self.verticalLayout_4.addWidget(self.SEND_EMAIL)
        self.SEND_EMAIL.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_HELP))
        self.verticalLayout_3.addWidget(self.contein_left_menu_butttons)
        self.horizontalLayout_2.addWidget(self.contein_left_menu)
        self.contein_page_background = QtWidgets.QFrame(self.body)


        self.contein_page_background.setStyleSheet("background-image: url(images/bg_IPh.png);")
        self.contein_page_background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_page_background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_page_background.setObjectName("contein_page_background")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.contein_page_background)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.page_retro_allPages = QtWidgets.QFrame(self.contein_page_background)
        self.page_retro_allPages.setMinimumSize(QtCore.QSize(0, 0))
        self.page_retro_allPages.setStyleSheet("background: transparent")
        self.page_retro_allPages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_retro_allPages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_retro_allPages.setObjectName("page_retro_allPages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_retro_allPages)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.page_retro_allPages)
        self.stackedWidget.setStyleSheet("color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.LOG_IN_2 = QtWidgets.QWidget()
        self.LOG_IN_2.setObjectName("LOG_IN_2")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.LOG_IN_2)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.retro_login = QtWidgets.QFrame(self.LOG_IN_2)
        self.retro_login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.retro_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.retro_login.setObjectName("retro_login")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.retro_login)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.log_in_PAGE = QtWidgets.QWidget(self.retro_login)
        self.log_in_PAGE.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.log_in_PAGE.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.log_in_PAGE.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border-style: none;\n"
"    border-radius: 20px;\n"
"    border: none; ")
        self.log_in_PAGE.setObjectName("log_in_PAGE")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.log_in_PAGE)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_IPHUNTER_2 = QtWidgets.QLabel(self.log_in_PAGE)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(28)
        self.label_IPHUNTER_2.setFont(font)
        self.label_IPHUNTER_2.setStyleSheet("\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border: none; \n"
"border-radius: 20px;")
        self.label_IPHUNTER_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_IPHUNTER_2.setObjectName("label_IPHUNTER_2")
        self.verticalLayout_33.addWidget(self.label_IPHUNTER_2)
        self.lineEdit_E_MAIL_2 = QtWidgets.QLineEdit(self.log_in_PAGE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_E_MAIL_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_E_MAIL_2.setSizePolicy(sizePolicy)
        self.lineEdit_E_MAIL_2.setMinimumSize(QtCore.QSize(500, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_E_MAIL_2.setFont(font)
        self.lineEdit_E_MAIL_2.setStyleSheet("border-radius:20px;\n"
"border:2px solid gray;")
        self.lineEdit_E_MAIL_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_E_MAIL_2.setClearButtonEnabled(True)
        self.lineEdit_E_MAIL_2.setObjectName("lineEdit_E_MAIL_2")
        self.verticalLayout_33.addWidget(self.lineEdit_E_MAIL_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(100, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_33.addItem(spacerItem1)
        self.lineEdit_PASSWORD_2 = QtWidgets.QLineEdit(self.log_in_PAGE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.lineEdit_PASSWORD_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_PASSWORD_2.setSizePolicy(sizePolicy)
        self.lineEdit_PASSWORD_2.setMinimumSize(QtCore.QSize(500, 41))
        self.lineEdit_PASSWORD_2.setMaximumSize(QtCore.QSize(502, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_PASSWORD_2.setFont(font)
        self.lineEdit_PASSWORD_2.setStyleSheet("border-radius:20px;\n"
"border:2px solid gray;")
        self.lineEdit_PASSWORD_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_PASSWORD_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_PASSWORD_2.setClearButtonEnabled(True)
        self.lineEdit_PASSWORD_2.setObjectName("lineEdit_PASSWORD_2")
        self.verticalLayout_33.addWidget(self.lineEdit_PASSWORD_2, 0, QtCore.Qt.AlignHCenter)
        self.insert_error_2 = QtWidgets.QLabel(self.log_in_PAGE)
        self.insert_error_2.setText("")
        self.insert_error_2.setObjectName("insert_error_2")
        self.verticalLayout_33.addWidget(self.insert_error_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.log_in_PAGE)
        self.pushButton_2.setMinimumSize(QtCore.QSize(250, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QFrame{\n"
"background-color : transparent;\n"
"}\n"
"QPushButton{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    border-radius:20px;\n"
"    color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48,48,48);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_33.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter)
        
        
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_RESET_PASSWORD))
        
        self.label_message_sendcode_2 = QtWidgets.QLabel(self.log_in_PAGE)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_message_sendcode_2.setFont(font)
        self.label_message_sendcode_2.setObjectName("label_message_sendcode_2")
        self.verticalLayout_33.addWidget(self.label_message_sendcode_2, 0, QtCore.Qt.AlignHCenter)
        self.SEND_CODEButton_2 = QtWidgets.QPushButton(self.log_in_PAGE)
        self.SEND_CODEButton_2.setMinimumSize(QtCore.QSize(350, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.SEND_CODEButton_2.setFont(font)
        self.SEND_CODEButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SEND_CODEButton_2.setStyleSheet("QFrame{\n"
"background-color : transparent;\n"
"}\n"
"QPushButton{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    border-radius:20px;\n"
"\n"
"    color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48,48,48);\n"
"}")
        self.SEND_CODEButton_2.setIconSize(QtCore.QSize(20, 20))
        self.SEND_CODEButton_2.setShortcut("")
        self.SEND_CODEButton_2.setCheckable(False)
        self.SEND_CODEButton_2.setAutoDefault(False)
        self.SEND_CODEButton_2.setDefault(False)
        self.SEND_CODEButton_2.setFlat(False)
        self.SEND_CODEButton_2.setObjectName("SEND_CODEButton_2")
        self.verticalLayout_33.addWidget(self.SEND_CODEButton_2, 0, QtCore.Qt.AlignHCenter)
        
        # collegare la funzione per la pagina del codice
        
        #self.SEND_CODEButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_INSERT_CODE))
        self.SEND_CODEButton_2.clicked.connect(self.page_code)
        self.label_want_register_2 = QtWidgets.QLabel(self.log_in_PAGE)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_want_register_2.setFont(font)
        self.label_want_register_2.setObjectName("label_want_register_2")
        self.verticalLayout_33.addWidget(self.label_want_register_2, 0, QtCore.Qt.AlignHCenter)
        self.SING_UPButton_2 = QtWidgets.QPushButton(self.log_in_PAGE)
        self.SING_UPButton_2.setMinimumSize(QtCore.QSize(350, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.SING_UPButton_2.setFont(font)
        self.SING_UPButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SING_UPButton_2.setStyleSheet("QFrame{\n"
"background-color : transparent;\n"
"}\n"
"QPushButton{\n"
"    \n"
"    border-radius:20px;\n"
"\n"
"    color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48,48,48);\n"
"}")
        self.SING_UPButton_2.setIconSize(QtCore.QSize(20, 20))
        self.SING_UPButton_2.setShortcut("")
        self.SING_UPButton_2.setCheckable(False)
        self.SING_UPButton_2.setAutoDefault(False)
        self.SING_UPButton_2.setDefault(False)
        self.SING_UPButton_2.setFlat(False)
        self.SING_UPButton_2.setObjectName("SING_UPButton_2")
        self.verticalLayout_33.addWidget(self.SING_UPButton_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_32.addWidget(self.log_in_PAGE)
        self.verticalLayout_31.addWidget(self.retro_login)
        self.stackedWidget.addWidget(self.LOG_IN_2)
        
        self.SING_UPButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_REGISTER))
        
        self.PAGE_INSERT_CODE = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PAGE_INSERT_CODE.sizePolicy().hasHeightForWidth())
        self.PAGE_INSERT_CODE.setSizePolicy(sizePolicy)
        self.PAGE_INSERT_CODE.setObjectName("PAGE_INSERT_CODE")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.PAGE_INSERT_CODE)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.label_LOG_IN_2 = QtWidgets.QLabel(self.PAGE_INSERT_CODE)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_LOG_IN_2.setFont(font)
        self.label_LOG_IN_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none; \n"
"border-radius: 20px;")
        self.label_LOG_IN_2.setObjectName("label_LOG_IN_2")
        self.verticalLayout_34.addWidget(self.label_LOG_IN_2, 0, QtCore.Qt.AlignHCenter)
        self.retro_insert_code = QtWidgets.QFrame(self.PAGE_INSERT_CODE)
        self.retro_insert_code.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.retro_insert_code.setFrameShadow(QtWidgets.QFrame.Raised)
        self.retro_insert_code.setObjectName("retro_insert_code")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.retro_insert_code)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.lineEdit_PASSWORD_3 = QtWidgets.QLineEdit(self.retro_insert_code)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_PASSWORD_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_PASSWORD_3.setSizePolicy(sizePolicy)
        self.lineEdit_PASSWORD_3.setMinimumSize(QtCore.QSize(300, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_PASSWORD_3.setFont(font)
        self.lineEdit_PASSWORD_3.setStyleSheet("border-radius:20px;\n"
"border: 2px solid gray;")
        self.lineEdit_PASSWORD_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_PASSWORD_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_PASSWORD_3.setClearButtonEnabled(True)
        self.lineEdit_PASSWORD_3.setObjectName("lineEdit_PASSWORD_3")
        self.verticalLayout_35.addWidget(self.lineEdit_PASSWORD_3, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_35.addItem(spacerItem2)
        self.SEND_CODEButton_3 = QtWidgets.QPushButton(self.retro_insert_code)
        self.SEND_CODEButton_3.setMinimumSize(QtCore.QSize(400, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.SEND_CODEButton_3.setFont(font)
        self.SEND_CODEButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SEND_CODEButton_3.setStyleSheet("QFrame{\n"
"background-color : transparent;\n"
"}\n"
"QPushButton{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    border-radius:20px;\n"
"    color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48,48,48);\n"
"}")
        self.SEND_CODEButton_3.setIconSize(QtCore.QSize(20, 20))
        self.SEND_CODEButton_3.setShortcut("")
        self.SEND_CODEButton_3.setCheckable(False)
        self.SEND_CODEButton_3.setAutoDefault(False)
        self.SEND_CODEButton_3.setDefault(False)
        self.SEND_CODEButton_3.setFlat(False)
        self.SEND_CODEButton_3.setObjectName("SEND_CODEButton_3")
        self.verticalLayout_35.addWidget(self.SEND_CODEButton_3, 0, QtCore.Qt.AlignHCenter)
        
        self.SEND_CODEButton_3.clicked.connect(self.start)
        
        self.log_in_PAGE_2 = QtWidgets.QFrame(self.retro_insert_code)
        self.log_in_PAGE_2.setMaximumSize(QtCore.QSize(400, 550))
        self.log_in_PAGE_2.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border-style: none;\n"
"    border-radius: 20px;\n"
"    border: none; ")
        self.log_in_PAGE_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.log_in_PAGE_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.log_in_PAGE_2.setObjectName("log_in_PAGE_2")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.log_in_PAGE_2)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.verticalLayout_35.addWidget(self.log_in_PAGE_2)
        self.verticalLayout_34.addWidget(self.retro_insert_code)
        self.stackedWidget.addWidget(self.PAGE_INSERT_CODE)
        self.PAGE_RESET_PASSWORD = QtWidgets.QWidget()
        self.PAGE_RESET_PASSWORD.setObjectName("PAGE_RESET_PASSWORD")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.PAGE_RESET_PASSWORD)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.retro_reset_password = QtWidgets.QFrame(self.PAGE_RESET_PASSWORD)
        self.retro_reset_password.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.retro_reset_password.setFrameShadow(QtWidgets.QFrame.Raised)
        self.retro_reset_password.setObjectName("retro_reset_password")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.retro_reset_password)
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.label_IPHUNTER_3 = QtWidgets.QLabel(self.retro_reset_password)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(25)
        self.label_IPHUNTER_3.setFont(font)
        self.label_IPHUNTER_3.setStyleSheet("\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border: none; \n"
"border-radius: 20px;")
        self.label_IPHUNTER_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_IPHUNTER_3.setObjectName("label_IPHUNTER_3")
        self.verticalLayout_39.addWidget(self.label_IPHUNTER_3, 0, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_39.addItem(spacerItem3)
        self.lineEdit_USERNAME = QtWidgets.QLineEdit(self.retro_reset_password)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_USERNAME.sizePolicy().hasHeightForWidth())
        self.lineEdit_USERNAME.setSizePolicy(sizePolicy)
        self.lineEdit_USERNAME.setMinimumSize(QtCore.QSize(300, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_USERNAME.setFont(font)
        self.lineEdit_USERNAME.setStyleSheet("border-radius:20px;\n"
"border:2px solid gray;")
        self.lineEdit_USERNAME.setText("")
        self.lineEdit_USERNAME.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_USERNAME.setClearButtonEnabled(True)
        self.lineEdit_USERNAME.setObjectName("lineEdit_USERNAME")
        self.verticalLayout_39.addWidget(self.lineEdit_USERNAME, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_39.addItem(spacerItem4)
        self.send_codeButton_for_reset = QtWidgets.QPushButton(self.retro_reset_password)
        self.send_codeButton_for_reset.setMinimumSize(QtCore.QSize(250, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.send_codeButton_for_reset.setFont(font)
        self.send_codeButton_for_reset.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.send_codeButton_for_reset.setStyleSheet("QFrame{\n"
"background-color : transparent;\n"
"}\n"
"QPushButton{\n"
"    \n"
"    border-radius:20px;\n"
"    color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48,48,48);\n"
"}")
        self.send_codeButton_for_reset.setIconSize(QtCore.QSize(20, 20))
        self.send_codeButton_for_reset.setShortcut("")
        self.send_codeButton_for_reset.setCheckable(False)
        self.send_codeButton_for_reset.setAutoDefault(False)
        self.send_codeButton_for_reset.setDefault(False)
        self.send_codeButton_for_reset.setFlat(False)
        self.send_codeButton_for_reset.setObjectName("send_codeButton_for_reset")
        self.verticalLayout_39.addWidget(self.send_codeButton_for_reset, 0, QtCore.Qt.AlignHCenter)
        
        self.send_codeButton_for_reset.clicked.connect(self.sendmail_reset)
        
        self.label_reset_password = QtWidgets.QLabel(self.retro_reset_password)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_reset_password.setFont(font)
        self.label_reset_password.setObjectName("label_reset_password")
        self.verticalLayout_39.addWidget(self.label_reset_password, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_entercode = QtWidgets.QLineEdit(self.retro_reset_password)
        self.lineEdit_entercode.setMinimumSize(QtCore.QSize(300, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_entercode.setFont(font)
        self.lineEdit_entercode.setStyleSheet("border-radius:20px;\n"
"border:2px solid gray;")
        self.lineEdit_entercode.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_entercode.setClearButtonEnabled(True)
        self.lineEdit_entercode.setObjectName("lineEdit_entercode")
        self.verticalLayout_39.addWidget(self.lineEdit_entercode, 0, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_39.addItem(spacerItem5)
        self.lineEdit_new_password = QtWidgets.QLineEdit(self.retro_reset_password)
        self.lineEdit_new_password.setMinimumSize(QtCore.QSize(300, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_new_password.setFont(font)
        self.lineEdit_new_password.setStyleSheet("border-radius:20px;\n"
"border:2px solid gray;")
        self.lineEdit_new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_new_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_new_password.setClearButtonEnabled(True)
        self.lineEdit_new_password.setObjectName("lineEdit_new_password")
        self.verticalLayout_39.addWidget(self.lineEdit_new_password, 0, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_39.addItem(spacerItem6)
        self.lineEdit_conf_password = QtWidgets.QLineEdit(self.retro_reset_password)
        self.lineEdit_conf_password.setMinimumSize(QtCore.QSize(300, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_conf_password.setFont(font)
        self.lineEdit_conf_password.setStyleSheet("border-radius:20px;\n"
"border:2px solid gray;")
        self.lineEdit_conf_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_conf_password.setClearButtonEnabled(True)
        self.lineEdit_conf_password.setObjectName("lineEdit_conf_password")
        self.verticalLayout_39.addWidget(self.lineEdit_conf_password, 0, QtCore.Qt.AlignHCenter)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_39.addItem(spacerItem7)
        self.Sing_upButton = QtWidgets.QPushButton(self.retro_reset_password)
        self.Sing_upButton.setMinimumSize(QtCore.QSize(200, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Sing_upButton.setFont(font)
        self.Sing_upButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Sing_upButton.setStyleSheet("QFrame{\n"
"background-color : transparent;\n"
"}\n"
"QPushButton{\n"
"    border-radius:20px;\n"
"\n"
"    color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48,48,48);\n"
"}")
        self.Sing_upButton.setIconSize(QtCore.QSize(20, 20))
        self.Sing_upButton.setShortcut("")
        self.Sing_upButton.setCheckable(False)
        self.Sing_upButton.setAutoDefault(False)
        self.Sing_upButton.setDefault(False)
        self.Sing_upButton.setFlat(False)
        self.Sing_upButton.setObjectName("Sing_upButton")
        self.verticalLayout_39.addWidget(self.Sing_upButton, 0, QtCore.Qt.AlignHCenter)
        
        self.Sing_upButton.clicked.connect(self.reset_password)
        
        self.verticalLayout_37.addWidget(self.retro_reset_password)
        self.stackedWidget.addWidget(self.PAGE_RESET_PASSWORD)
        self.PAGE_REGISTER = QtWidgets.QWidget()
        self.PAGE_REGISTER.setObjectName("PAGE_REGISTER")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.PAGE_REGISTER)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.retro_register = QtWidgets.QFrame(self.PAGE_REGISTER)
        self.retro_register.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.retro_register.setFrameShadow(QtWidgets.QFrame.Raised)
        self.retro_register.setObjectName("retro_register")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.retro_register)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.label_Register = QtWidgets.QLabel(self.retro_register)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(26)
        self.label_Register.setFont(font)
        self.label_Register.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none; \n"
"border-radius: 20px;")
        self.label_Register.setObjectName("label_Register")
        self.verticalLayout_40.addWidget(self.label_Register, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_USERNAME_2 = QtWidgets.QLineEdit(self.retro_register)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_USERNAME_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_USERNAME_2.setSizePolicy(sizePolicy)
        self.lineEdit_USERNAME_2.setMinimumSize(QtCore.QSize(350, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_USERNAME_2.setFont(font)
        self.lineEdit_USERNAME_2.setStyleSheet("border-radius:20px;\n"
"border:2px solid gray;")
        self.lineEdit_USERNAME_2.setText("")
        self.lineEdit_USERNAME_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_USERNAME_2.setClearButtonEnabled(True)
        self.lineEdit_USERNAME_2.setObjectName("lineEdit_USERNAME_2")
        self.verticalLayout_40.addWidget(self.lineEdit_USERNAME_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_40.addItem(spacerItem8)
        self.lineEdit_E_MAIL_3 = QtWidgets.QLineEdit(self.retro_register)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_E_MAIL_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_E_MAIL_3.setSizePolicy(sizePolicy)
        self.lineEdit_E_MAIL_3.setMinimumSize(QtCore.QSize(350, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_E_MAIL_3.setFont(font)
        self.lineEdit_E_MAIL_3.setStyleSheet("border-radius:20px;\n"
"border:2px solid gray;")
        self.lineEdit_E_MAIL_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_E_MAIL_3.setClearButtonEnabled(True)
        self.lineEdit_E_MAIL_3.setObjectName("lineEdit_E_MAIL_3")
        self.verticalLayout_40.addWidget(self.lineEdit_E_MAIL_3, 0, QtCore.Qt.AlignHCenter)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_40.addItem(spacerItem9)
        self.lineEdit_PASSWORD_5 = QtWidgets.QLineEdit(self.retro_register)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_PASSWORD_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_PASSWORD_5.setSizePolicy(sizePolicy)
        self.lineEdit_PASSWORD_5.setMinimumSize(QtCore.QSize(350, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_PASSWORD_5.setFont(font)
        self.lineEdit_PASSWORD_5.setStyleSheet("border-radius:20px;\n"
"border:2px solid gray;")
        self.lineEdit_PASSWORD_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_PASSWORD_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_PASSWORD_5.setClearButtonEnabled(True)
        self.lineEdit_PASSWORD_5.setObjectName("lineEdit_PASSWORD_5")
        self.verticalLayout_40.addWidget(self.lineEdit_PASSWORD_5, 0, QtCore.Qt.AlignHCenter)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_40.addItem(spacerItem10)
        self.Sing_upButton_2 = QtWidgets.QPushButton(self.retro_register)
        self.Sing_upButton_2.setMinimumSize(QtCore.QSize(200, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Sing_upButton_2.setFont(font)
        self.Sing_upButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Sing_upButton_2.setStyleSheet("QFrame{\n"
"background-color : transparent;\n"
"}\n"
"QPushButton{\n"
"   border-radius:20px;\n"
"\n"
"    \n"
"    color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48,48,48);\n"
"}")
        self.Sing_upButton_2.setIconSize(QtCore.QSize(20, 20))
        self.Sing_upButton_2.setShortcut("")
        self.Sing_upButton_2.setCheckable(False)
        self.Sing_upButton_2.setAutoDefault(False)
        self.Sing_upButton_2.setDefault(False)
        self.Sing_upButton_2.setFlat(False)
        self.Sing_upButton_2.setObjectName("Sing_upButton_2")
        self.verticalLayout_40.addWidget(self.Sing_upButton_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_38.addWidget(self.retro_register)
        
        
        self.Sing_upButton_2.clicked.connect(self.after_register)
        
        
        self.stackedWidget.addWidget(self.PAGE_REGISTER)
        self.PAGE_IP_HUNTER = QtWidgets.QWidget()
        self.PAGE_IP_HUNTER.setObjectName("PAGE_IP_HUNTER")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.PAGE_IP_HUNTER)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.contein_IP_HUNTER = QtWidgets.QFrame(self.PAGE_IP_HUNTER)
        self.contein_IP_HUNTER.setMinimumSize(QtCore.QSize(0, 200))
        self.contein_IP_HUNTER.setMaximumSize(QtCore.QSize(16777215, 300))
        self.contein_IP_HUNTER.setStyleSheet("background: transparent;\n"
"")
        self.contein_IP_HUNTER.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_IP_HUNTER.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_IP_HUNTER.setObjectName("contein_IP_HUNTER")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.contein_IP_HUNTER)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.TITLE_IP_HUNTER = QtWidgets.QLabel(self.contein_IP_HUNTER)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(35)
        self.TITLE_IP_HUNTER.setFont(font)
        self.TITLE_IP_HUNTER.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.TITLE_IP_HUNTER.setAlignment(QtCore.Qt.AlignCenter)
        self.TITLE_IP_HUNTER.setObjectName("TITLE_IP_HUNTER")
        self.verticalLayout_8.addWidget(self.TITLE_IP_HUNTER)
        self.Type_an_IP_AddressIPHUNTER = QtWidgets.QLineEdit(self.contein_IP_HUNTER)
        self.Type_an_IP_AddressIPHUNTER.setMinimumSize(QtCore.QSize(300, 30))
        self.Type_an_IP_AddressIPHUNTER.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Type_an_IP_AddressIPHUNTER.setFont(font)
        self.Type_an_IP_AddressIPHUNTER.setStyleSheet("border: 1px solid gray ;\n"
"border-radius: 10px;\n"
"color: white;\n"
"")
        self.Type_an_IP_AddressIPHUNTER.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Type_an_IP_AddressIPHUNTER.setText("")
        self.Type_an_IP_AddressIPHUNTER.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Type_an_IP_AddressIPHUNTER.setDragEnabled(True)
        self.Type_an_IP_AddressIPHUNTER.setObjectName("Type_an_IP_AddressIPHUNTER")
        self.verticalLayout_8.addWidget(self.Type_an_IP_AddressIPHUNTER, 0, QtCore.Qt.AlignHCenter)
        self.START_IPSEARHButton = QtWidgets.QPushButton(self.contein_IP_HUNTER)
        self.START_IPSEARHButton.setMinimumSize(QtCore.QSize(0, 0))
        self.START_IPSEARHButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.START_IPSEARHButton.setStyleSheet("\n"
"")
        self.START_IPSEARHButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/cil-arrow-circle-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.START_IPSEARHButton.setIcon(icon5)
        self.START_IPSEARHButton.setIconSize(QtCore.QSize(50, 50))
        self.START_IPSEARHButton.setObjectName("START_IPSEARHButton")
        self.verticalLayout_8.addWidget(self.START_IPSEARHButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.contein_IP_HUNTER)
        self.START_IPSEARHButton.clicked.connect(self.hunter)
        
        self.tabWidget_contein_output_IPHUNTER = QtWidgets.QTabWidget(self.PAGE_IP_HUNTER)
        self.tabWidget_contein_output_IPHUNTER.setAutoFillBackground(False)
        self.tabWidget_contein_output_IPHUNTER.setStyleSheet("QTabWidget::pane {\n"
"background: transparent;\n"
" border: 2px solid grey;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"background: transparent;\n"

"}")
        self.tabWidget_contein_output_IPHUNTER.setObjectName("tabWidget_contein_output_IPHUNTER")
        self.whois_output = QtWidgets.QWidget()
        self.whois_output.setObjectName("whois_output")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.whois_output)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.whois_output)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 912, 94))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_53.addWidget(self.label_7)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_52.addWidget(self.scrollArea_7)
        self.tabWidget_contein_output_IPHUNTER.addTab(self.whois_output, "")
        self.abuse_output = QtWidgets.QWidget()
        self.abuse_output.setEnabled(True)
        self.abuse_output.setObjectName("abuse_output")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.abuse_output)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.abuse_output)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 912, 94))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_51.addWidget(self.label_6)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_7)
        self.verticalLayout_50.addWidget(self.scrollArea_6)
        self.tabWidget_contein_output_IPHUNTER.addTab(self.abuse_output, "")
        self.NMAP_output = QtWidgets.QWidget()
        self.NMAP_output.setObjectName("NMAP_output")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.NMAP_output)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.NMAP_output)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 912, 94))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_20.addWidget(self.label_5)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_6)
        self.verticalLayout_49.addWidget(self.scrollArea_5)
        self.tabWidget_contein_output_IPHUNTER.addTab(self.NMAP_output, "")
        self.output_type = QtWidgets.QWidget()
        self.output_type.setObjectName("output_type")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.output_type)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.scrollArea = QtWidgets.QScrollArea(self.output_type)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 912, 94))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.label_type = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_type.setObjectName("label")
        self.verticalLayout_42.addWidget(self.label_type)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_41.addWidget(self.scrollArea)
        self.tabWidget_contein_output_IPHUNTER.addTab(self.output_type, "")
        self.output_class = QtWidgets.QWidget()
        self.output_class.setObjectName("output_class")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.output_class)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.output_class)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 912, 94))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.label_class = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_class.setObjectName("label_class")
        self.verticalLayout_44.addWidget(self.label_class)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_43.addWidget(self.scrollArea_2)
        self.tabWidget_contein_output_IPHUNTER.addTab(self.output_class, "")
        self.output_hostname = QtWidgets.QWidget()
        self.output_hostname.setObjectName("output_hostname")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.output_hostname)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.output_hostname)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 912, 94))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.label_hostname = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_hostname.setObjectName("label_hostname")
        self.verticalLayout_46.addWidget(self.label_hostname)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_45.addWidget(self.scrollArea_3)
        self.tabWidget_contein_output_IPHUNTER.addTab(self.output_hostname, "")
        self.output_macaddres = QtWidgets.QWidget()
        self.output_macaddres.setObjectName("output_macaddres")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.output_macaddres)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.output_macaddres)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 912, 94))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.label_macaddress = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_macaddress.setObjectName("label_macaddress")
        self.verticalLayout_48.addWidget(self.label_macaddress)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_47.addWidget(self.scrollArea_4)
        self.tabWidget_contein_output_IPHUNTER.addTab(self.output_macaddres, "")
        self.verticalLayout_7.addWidget(self.tabWidget_contein_output_IPHUNTER)
        self.contein_send_result = QtWidgets.QFrame(self.PAGE_IP_HUNTER)
        self.contein_send_result.setMinimumSize(QtCore.QSize(0, 100))
        self.contein_send_result.setMaximumSize(QtCore.QSize(16777215, 100))
        self.contein_send_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_send_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_send_result.setObjectName("contein_send_result")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.contein_send_result)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Send_result_ip_hunter = QtWidgets.QPushButton(self.contein_send_result)
        self.Send_result_ip_hunter.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Send_result_ip_hunter.sizePolicy().hasHeightForWidth())
        self.Send_result_ip_hunter.setSizePolicy(sizePolicy)
        self.Send_result_ip_hunter.setMinimumSize(QtCore.QSize(70, 70))
        self.Send_result_ip_hunter.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Send_result_ip_hunter.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        self.Send_result_ip_hunter.setFont(font)
        self.Send_result_ip_hunter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Send_result_ip_hunter.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: transparent;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Send_result_ip_hunter.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Send_result_ip_hunter.setAutoRepeatDelay(301)
        self.Send_result_ip_hunter.setAutoDefault(False)
        self.Send_result_ip_hunter.setDefault(False)
        self.Send_result_ip_hunter.setFlat(False)
        self.Send_result_ip_hunter.setObjectName("Send_result_ip_hunter")
        self.horizontalLayout_4.addWidget(self.Send_result_ip_hunter)
        self.verticalLayout_7.addWidget(self.contein_send_result)
        
        self.Send_result_ip_hunter.clicked.connect(self.sendresults_hunt)
        
        self.created_by_ATEAM_page_iphunter = QtWidgets.QFrame(self.PAGE_IP_HUNTER)
        self.created_by_ATEAM_page_iphunter.setMinimumSize(QtCore.QSize(0, 70))
        self.created_by_ATEAM_page_iphunter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.created_by_ATEAM_page_iphunter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.created_by_ATEAM_page_iphunter.setObjectName("created_by_ATEAM_page_iphunter")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.created_by_ATEAM_page_iphunter)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.created_by_ATEAM_IP_HUNTER = QtWidgets.QLabel(self.created_by_ATEAM_page_iphunter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.created_by_ATEAM_IP_HUNTER.setFont(font)
        self.created_by_ATEAM_IP_HUNTER.setStyleSheet("color: rgb(136, 136, 136);")
        self.created_by_ATEAM_IP_HUNTER.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.created_by_ATEAM_IP_HUNTER.setObjectName("created_by_ATEAM_IP_HUNTER")
        self.verticalLayout_23.addWidget(self.created_by_ATEAM_IP_HUNTER)
        self.verticalLayout_7.addWidget(self.created_by_ATEAM_page_iphunter)
        self.stackedWidget.addWidget(self.PAGE_IP_HUNTER)
        self.PAGE_WHOIS = QtWidgets.QWidget()
        self.PAGE_WHOIS.setObjectName("PAGE_WHOIS")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.PAGE_WHOIS)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.contein_all_WHOIS = QtWidgets.QFrame(self.PAGE_WHOIS)
        self.contein_all_WHOIS.setMinimumSize(QtCore.QSize(0, 200))
        self.contein_all_WHOIS.setMaximumSize(QtCore.QSize(16777215, 300))
        self.contein_all_WHOIS.setStyleSheet("background: transparent;\n"
"")
        self.contein_all_WHOIS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_all_WHOIS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_all_WHOIS.setObjectName("contein_all_WHOIS")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.contein_all_WHOIS)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.TITLE_WHOIS = QtWidgets.QLabel(self.contein_all_WHOIS)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(35)
        self.TITLE_WHOIS.setFont(font)
        self.TITLE_WHOIS.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.TITLE_WHOIS.setAlignment(QtCore.Qt.AlignCenter)
        self.TITLE_WHOIS.setObjectName("TITLE_WHOIS")
        self.verticalLayout_9.addWidget(self.TITLE_WHOIS)
        self.Type_an_IP_Address_WHOIS = QtWidgets.QLineEdit(self.contein_all_WHOIS)
        self.Type_an_IP_Address_WHOIS.setMinimumSize(QtCore.QSize(300, 30))
        self.Type_an_IP_Address_WHOIS.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Type_an_IP_Address_WHOIS.setFont(font)
        self.Type_an_IP_Address_WHOIS.setStyleSheet("border: 1px solid gray ;\n"
"border-radius: 10px;\n"
"color: white;\n"
"")
        self.Type_an_IP_Address_WHOIS.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Type_an_IP_Address_WHOIS.setText("")
        self.Type_an_IP_Address_WHOIS.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Type_an_IP_Address_WHOIS.setDragEnabled(True)
        self.Type_an_IP_Address_WHOIS.setObjectName("Type_an_IP_Address_WHOIS")
        self.verticalLayout_9.addWidget(self.Type_an_IP_Address_WHOIS, 0, QtCore.Qt.AlignHCenter)
        self.START_WHOISButton = QtWidgets.QPushButton(self.contein_all_WHOIS)
        self.START_WHOISButton.setMinimumSize(QtCore.QSize(0, 0))
        self.START_WHOISButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.START_WHOISButton.setStyleSheet("")
        self.START_WHOISButton.setText("")
        self.START_WHOISButton.setIcon(icon5)
        self.START_WHOISButton.setIconSize(QtCore.QSize(50, 50))
        self.START_WHOISButton.setObjectName("START_WHOISButton")
        
        self.START_WHOISButton.clicked.connect(self.whois_ip)
        self.verticalLayout_9.addWidget(self.START_WHOISButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_10.addWidget(self.contein_all_WHOIS)
        self.scrollArea_whois = QtWidgets.QScrollArea(self.PAGE_WHOIS)
        self.scrollArea_whois.setStyleSheet("border:none;")
        self.scrollArea_whois.setWidgetResizable(True)
        self.scrollArea_whois.setObjectName("scrollArea_whois")
        self.scrollAreaWidgetContents_whois = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_whois.setGeometry(QtCore.QRect(0, 0, 1154, 392))
        self.scrollAreaWidgetContents_whois.setStyleSheet("border: none;")
        self.scrollAreaWidgetContents_whois.setObjectName("scrollAreaWidgetContents_whois")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_whois)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.output_whois = QtWidgets.QLabel(self.scrollAreaWidgetContents_whois)
        self.output_whois.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:1px solid gray;")
        self.output_whois.setWordWrap(True)
        self.output_whois.setObjectName("output_whois")
        self.verticalLayout_29.addWidget(self.output_whois)
        self.scrollArea_whois.setWidget(self.scrollAreaWidgetContents_whois)
        self.verticalLayout_10.addWidget(self.scrollArea_whois)
        self.send_result_whois = QtWidgets.QFrame(self.PAGE_WHOIS)
        self.send_result_whois.setMinimumSize(QtCore.QSize(0, 70))
        self.send_result_whois.setMaximumSize(QtCore.QSize(16777215, 70))
        self.send_result_whois.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.send_result_whois.setFrameShadow(QtWidgets.QFrame.Raised)
        self.send_result_whois.setObjectName("send_result_whois")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.send_result_whois)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.contein_send_result_ssl_scal_2 = QtWidgets.QFrame(self.send_result_whois)
        self.contein_send_result_ssl_scal_2.setMinimumSize(QtCore.QSize(0, 100))
        self.contein_send_result_ssl_scal_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.contein_send_result_ssl_scal_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_send_result_ssl_scal_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_send_result_ssl_scal_2.setObjectName("contein_send_result_ssl_scal_2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.contein_send_result_ssl_scal_2)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.Send_resultl_ssl_scan_button_2 = QtWidgets.QPushButton(self.contein_send_result_ssl_scal_2)
        self.Send_resultl_ssl_scan_button_2.setEnabled(True)
        ##########################################################
        self.Send_resultl_ssl_scan_button_2.clicked.connect(self.sendresults_whois)
        
        ###########################################################
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Send_resultl_ssl_scan_button_2.sizePolicy().hasHeightForWidth())
        self.Send_resultl_ssl_scan_button_2.setSizePolicy(sizePolicy)
        self.Send_resultl_ssl_scan_button_2.setMinimumSize(QtCore.QSize(70, 70))
        self.Send_resultl_ssl_scan_button_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Send_resultl_ssl_scan_button_2.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        self.Send_resultl_ssl_scan_button_2.setFont(font)
        self.Send_resultl_ssl_scan_button_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Send_resultl_ssl_scan_button_2.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: transparent;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Send_resultl_ssl_scan_button_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Send_resultl_ssl_scan_button_2.setAutoRepeatDelay(301)
        self.Send_resultl_ssl_scan_button_2.setAutoDefault(False)
        self.Send_resultl_ssl_scan_button_2.setDefault(False)
        self.Send_resultl_ssl_scan_button_2.setFlat(False)
        self.Send_resultl_ssl_scan_button_2.setObjectName("Send_resultl_ssl_scan_button_2")
        self.horizontalLayout_14.addWidget(self.Send_resultl_ssl_scan_button_2)
        self.horizontalLayout_5.addWidget(self.contein_send_result_ssl_scal_2)
        self.verticalLayout_10.addWidget(self.send_result_whois)
        self.crested_by_ATEAM_page_ssl_scan_2 = QtWidgets.QLabel(self.PAGE_WHOIS)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.crested_by_ATEAM_page_ssl_scan_2.setFont(font)
        self.crested_by_ATEAM_page_ssl_scan_2.setStyleSheet("color: rgb(136, 136, 136);")
        self.crested_by_ATEAM_page_ssl_scan_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.crested_by_ATEAM_page_ssl_scan_2.setObjectName("crested_by_ATEAM_page_ssl_scan_2")
        self.verticalLayout_10.addWidget(self.crested_by_ATEAM_page_ssl_scan_2)
        self.stackedWidget.addWidget(self.PAGE_WHOIS)
        self.PAGE_ABUSE = QtWidgets.QWidget()
        self.PAGE_ABUSE.setObjectName("PAGE_ABUSE")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.PAGE_ABUSE)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.contein_all_ABUSE = QtWidgets.QFrame(self.PAGE_ABUSE)
        self.contein_all_ABUSE.setMinimumSize(QtCore.QSize(0, 200))
        self.contein_all_ABUSE.setMaximumSize(QtCore.QSize(16777215, 300))
        self.contein_all_ABUSE.setStyleSheet("background: transparent;\n"
"")
        self.contein_all_ABUSE.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_all_ABUSE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_all_ABUSE.setObjectName("contein_all_ABUSE")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.contein_all_ABUSE)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.TITLE_ABUSE = QtWidgets.QLabel(self.contein_all_ABUSE)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(35)
        self.TITLE_ABUSE.setFont(font)
        self.TITLE_ABUSE.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.TITLE_ABUSE.setAlignment(QtCore.Qt.AlignCenter)
        self.TITLE_ABUSE.setObjectName("TITLE_ABUSE")
        self.verticalLayout_11.addWidget(self.TITLE_ABUSE)
        self.Type_an_IP_Address_ABUSE = QtWidgets.QLineEdit(self.contein_all_ABUSE)
        self.Type_an_IP_Address_ABUSE.setMinimumSize(QtCore.QSize(300, 30))
        self.Type_an_IP_Address_ABUSE.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Type_an_IP_Address_ABUSE.setFont(font)
        self.Type_an_IP_Address_ABUSE.setStyleSheet("border: 1px solid gray ;\n"
"border-radius: 10px;\n"
"color: white;\n"
"")
        self.Type_an_IP_Address_ABUSE.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Type_an_IP_Address_ABUSE.setText("")
        self.Type_an_IP_Address_ABUSE.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Type_an_IP_Address_ABUSE.setDragEnabled(True)
        self.Type_an_IP_Address_ABUSE.setObjectName("Type_an_IP_Address_ABUSE")
        self.verticalLayout_11.addWidget(self.Type_an_IP_Address_ABUSE, 0, QtCore.Qt.AlignHCenter)
        self.START_ABUSEButton = QtWidgets.QPushButton(self.contein_all_ABUSE)
        self.START_ABUSEButton.setMinimumSize(QtCore.QSize(0, 0))
        self.START_ABUSEButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.START_ABUSEButton.setStyleSheet("")
        self.START_ABUSEButton.setText("")
        self.START_ABUSEButton.setIcon(icon5)
        self.START_ABUSEButton.setIconSize(QtCore.QSize(50, 50))
        self.START_ABUSEButton.setObjectName("START_ABUSEButton")
        
        ######################################################
        self.START_ABUSEButton.clicked.connect(self.IPabuse)#
        ######################################################
        
        self.verticalLayout_11.addWidget(self.START_ABUSEButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_12.addWidget(self.contein_all_ABUSE)
        self.scrollArea_abuse = QtWidgets.QScrollArea(self.PAGE_ABUSE)
        self.scrollArea_abuse.setWidgetResizable(True)
        self.scrollArea_abuse.setObjectName("scrollArea_abuse")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1152, 360))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.output_abuse = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.output_abuse.setStyleSheet("color: rgb(255, 255, 255);")
        self.output_abuse.setText("")
        self.output_abuse.setObjectName("output_abuse")
        self.horizontalLayout_6.addWidget(self.output_abuse)
        self.scrollArea_abuse.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_12.addWidget(self.scrollArea_abuse)
        self.contein_send_result_ssl_scal_3 = QtWidgets.QFrame(self.PAGE_ABUSE)
        self.contein_send_result_ssl_scal_3.setMinimumSize(QtCore.QSize(0, 100))
        self.contein_send_result_ssl_scal_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.contein_send_result_ssl_scal_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_send_result_ssl_scal_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_send_result_ssl_scal_3.setObjectName("contein_send_result_ssl_scal_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.contein_send_result_ssl_scal_3)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.Send_resultl_ssl_scan_button_3 = QtWidgets.QPushButton(self.contein_send_result_ssl_scal_3)
        self.Send_resultl_ssl_scan_button_3.setEnabled(True)
        #################################
        
        self.Send_resultl_ssl_scan_button_3.clicked.connect(self.sendresults_abuse)
        
        ##############################
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Send_resultl_ssl_scan_button_3.sizePolicy().hasHeightForWidth())
        self.Send_resultl_ssl_scan_button_3.setSizePolicy(sizePolicy)
        self.Send_resultl_ssl_scan_button_3.setMinimumSize(QtCore.QSize(70, 70))
        self.Send_resultl_ssl_scan_button_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Send_resultl_ssl_scan_button_3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        self.Send_resultl_ssl_scan_button_3.setFont(font)
        self.Send_resultl_ssl_scan_button_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Send_resultl_ssl_scan_button_3.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: transparent;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Send_resultl_ssl_scan_button_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Send_resultl_ssl_scan_button_3.setAutoRepeatDelay(301)
        self.Send_resultl_ssl_scan_button_3.setAutoDefault(False)
        self.Send_resultl_ssl_scan_button_3.setDefault(False)
        self.Send_resultl_ssl_scan_button_3.setFlat(False)
        self.Send_resultl_ssl_scan_button_3.setObjectName("Send_resultl_ssl_scan_button_3")
        self.horizontalLayout_15.addWidget(self.Send_resultl_ssl_scan_button_3)
        self.verticalLayout_12.addWidget(self.contein_send_result_ssl_scal_3)
        self.crested_by_ATEAM_page_ssl_scan_3 = QtWidgets.QLabel(self.PAGE_ABUSE)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.crested_by_ATEAM_page_ssl_scan_3.setFont(font)
        self.crested_by_ATEAM_page_ssl_scan_3.setStyleSheet("color: rgb(136, 136, 136);")
        self.crested_by_ATEAM_page_ssl_scan_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.crested_by_ATEAM_page_ssl_scan_3.setObjectName("crested_by_ATEAM_page_ssl_scan_3")
        self.verticalLayout_12.addWidget(self.crested_by_ATEAM_page_ssl_scan_3)
        self.stackedWidget.addWidget(self.PAGE_ABUSE)
        self.PAGE_RADAR = QtWidgets.QWidget()
        self.PAGE_RADAR.setObjectName("PAGE_RADAR")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.PAGE_RADAR)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.contein_all = QtWidgets.QFrame(self.PAGE_RADAR)
        self.contein_all.setMinimumSize(QtCore.QSize(0, 200))
        self.contein_all.setMaximumSize(QtCore.QSize(16777215, 300))
        self.contein_all.setStyleSheet("background: transparent;\n"
"")
        self.contein_all.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_all.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_all.setObjectName("contein_all")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.contein_all)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.TITLE_RADAR = QtWidgets.QLabel(self.contein_all)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(35)
        self.TITLE_RADAR.setFont(font)
        self.TITLE_RADAR.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.TITLE_RADAR.setAlignment(QtCore.Qt.AlignCenter)
        self.TITLE_RADAR.setObjectName("TITLE_RADAR")
        self.verticalLayout_16.addWidget(self.TITLE_RADAR)
        self.Type_an_IP_Address_radar = QtWidgets.QLineEdit(self.contein_all)
        self.Type_an_IP_Address_radar.setMinimumSize(QtCore.QSize(300, 30))
        self.Type_an_IP_Address_radar.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Type_an_IP_Address_radar.setFont(font)
        self.Type_an_IP_Address_radar.setStyleSheet("border: 1px solid gray ;\n"
"border-radius: 10px;\n"
"color: white;\n"
"")
        self.Type_an_IP_Address_radar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Type_an_IP_Address_radar.setText("")
        self.Type_an_IP_Address_radar.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Type_an_IP_Address_radar.setDragEnabled(True)
        self.Type_an_IP_Address_radar.setObjectName("Type_an_IP_Address_radar")
        self.verticalLayout_16.addWidget(self.Type_an_IP_Address_radar, 0, QtCore.Qt.AlignHCenter)
        self.START_RADARButton_radar = QtWidgets.QPushButton(self.contein_all)
        self.START_RADARButton_radar.setMinimumSize(QtCore.QSize(0, 0))
        self.START_RADARButton_radar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.START_RADARButton_radar.setStyleSheet("")
        self.START_RADARButton_radar.setText("")
        self.START_RADARButton_radar.setIcon(icon5)
        self.START_RADARButton_radar.setIconSize(QtCore.QSize(50, 50))
        self.START_RADARButton_radar.setObjectName("START_RADARButton_radar")
        self.verticalLayout_16.addWidget(self.START_RADARButton_radar)
				###################################################################
        self.START_RADARButton_radar.clicked.connect(self.radar)

        ##################################################
        self.label = QtWidgets.QLabel(self.contein_all)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_16.addWidget(self.label)
        self.verticalLayout_13.addWidget(self.contein_all)
        self.scrollArea_radar = QtWidgets.QScrollArea(self.PAGE_RADAR)
        self.scrollArea_radar.setWidgetResizable(True)
        self.scrollArea_radar.setObjectName("scrollArea_radar")
        self.scrollAreaWidgetContents_radar = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_radar.setGeometry(QtCore.QRect(0, 0, 1152, 368))
        self.scrollAreaWidgetContents_radar.setObjectName("scrollAreaWidgetContents_radar")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_radar)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.output_radar = QtWidgets.QLabel(self.scrollAreaWidgetContents_radar)
        self.output_radar.setStyleSheet("color: rgb(255, 255, 255);")
        self.output_radar.setText("")
        self.output_radar.setObjectName("output_radar")
        self.horizontalLayout_17.addWidget(self.output_radar)
        self.scrollArea_radar.setWidget(self.scrollAreaWidgetContents_radar)
        self.verticalLayout_13.addWidget(self.scrollArea_radar)
        self.contein_send_result_radar = QtWidgets.QFrame(self.PAGE_RADAR)
        self.contein_send_result_radar.setMinimumSize(QtCore.QSize(0, 80))
        self.contein_send_result_radar.setMaximumSize(QtCore.QSize(16777215, 80))
        self.contein_send_result_radar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_send_result_radar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_send_result_radar.setObjectName("contein_send_result_radar")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.contein_send_result_radar)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.contein_send_result_ssl_scal_4 = QtWidgets.QFrame(self.contein_send_result_radar)
        self.contein_send_result_ssl_scal_4.setMinimumSize(QtCore.QSize(0, 100))
        self.contein_send_result_ssl_scal_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.contein_send_result_ssl_scal_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_send_result_ssl_scal_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_send_result_ssl_scal_4.setObjectName("contein_send_result_ssl_scal_4")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.contein_send_result_ssl_scal_4)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.Send_resultl_ssl_scan_button_4 = QtWidgets.QPushButton(self.contein_send_result_ssl_scal_4)
        self.Send_resultl_ssl_scan_button_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Send_resultl_ssl_scan_button_4.sizePolicy().hasHeightForWidth())
        self.Send_resultl_ssl_scan_button_4.setSizePolicy(sizePolicy)
        self.Send_resultl_ssl_scan_button_4.setMinimumSize(QtCore.QSize(70, 70))
        self.Send_resultl_ssl_scan_button_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Send_resultl_ssl_scan_button_4.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        self.Send_resultl_ssl_scan_button_4.setFont(font)
        self.Send_resultl_ssl_scan_button_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Send_resultl_ssl_scan_button_4.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: transparent;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Send_resultl_ssl_scan_button_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Send_resultl_ssl_scan_button_4.setAutoRepeatDelay(301)
        self.Send_resultl_ssl_scan_button_4.setAutoDefault(False)
        self.Send_resultl_ssl_scan_button_4.setDefault(False)
        self.Send_resultl_ssl_scan_button_4.setFlat(False)
        self.Send_resultl_ssl_scan_button_4.setObjectName("Send_resultl_ssl_scan_button_4")
        self.horizontalLayout_16.addWidget(self.Send_resultl_ssl_scan_button_4)
        self.horizontalLayout_7.addWidget(self.contein_send_result_ssl_scal_4)
        #############################################
        self.Send_resultl_ssl_scan_button_4.clicked.connect(self.sendresults_geo)
        
        ############################################
        self.verticalLayout_13.addWidget(self.contein_send_result_radar)
        self.crested_by_ATEAM_page_ssl_scan_4 = QtWidgets.QLabel(self.PAGE_RADAR)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.crested_by_ATEAM_page_ssl_scan_4.setFont(font)
        self.crested_by_ATEAM_page_ssl_scan_4.setStyleSheet("color: rgb(136, 136, 136);")
        self.crested_by_ATEAM_page_ssl_scan_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.crested_by_ATEAM_page_ssl_scan_4.setObjectName("crested_by_ATEAM_page_ssl_scan_4")
        self.verticalLayout_13.addWidget(self.crested_by_ATEAM_page_ssl_scan_4)
        self.stackedWidget.addWidget(self.PAGE_RADAR)
        self.PAGE_SSL_SCAN = QtWidgets.QWidget()
        self.PAGE_SSL_SCAN.setObjectName("PAGE_SSL_SCAN")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.PAGE_SSL_SCAN)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.contein_all_SSL_SCAN = QtWidgets.QFrame(self.PAGE_SSL_SCAN)
        self.contein_all_SSL_SCAN.setMinimumSize(QtCore.QSize(0, 200))
        self.contein_all_SSL_SCAN.setMaximumSize(QtCore.QSize(16777215, 300))
        self.contein_all_SSL_SCAN.setStyleSheet("background: transparent;\n"
"")
        self.contein_all_SSL_SCAN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_all_SSL_SCAN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_all_SSL_SCAN.setObjectName("contein_all_SSL_SCAN")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.contein_all_SSL_SCAN)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.TITLE_SSL_SCAN = QtWidgets.QLabel(self.contein_all_SSL_SCAN)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(35)
        self.TITLE_SSL_SCAN.setFont(font)
        self.TITLE_SSL_SCAN.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.TITLE_SSL_SCAN.setAlignment(QtCore.Qt.AlignCenter)
        self.TITLE_SSL_SCAN.setObjectName("TITLE_SSL_SCAN")
        self.verticalLayout_14.addWidget(self.TITLE_SSL_SCAN)
        self.Type_an_IP_Address_ssl_scan = QtWidgets.QLineEdit(self.contein_all_SSL_SCAN)
        self.Type_an_IP_Address_ssl_scan.setMinimumSize(QtCore.QSize(300, 30))
        self.Type_an_IP_Address_ssl_scan.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Type_an_IP_Address_ssl_scan.setFont(font)
        self.Type_an_IP_Address_ssl_scan.setStyleSheet("border: 1px solid gray ;\n"
"border-radius: 10px;\n"
"color: white;\n"
"")
        self.Type_an_IP_Address_ssl_scan.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Type_an_IP_Address_ssl_scan.setText("")
        self.Type_an_IP_Address_ssl_scan.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Type_an_IP_Address_ssl_scan.setDragEnabled(True)
        self.Type_an_IP_Address_ssl_scan.setObjectName("Type_an_IP_Address_ssl_scan")
        self.verticalLayout_14.addWidget(self.Type_an_IP_Address_ssl_scan, 0, QtCore.Qt.AlignHCenter)
        self.START_SSL_SCANButton = QtWidgets.QPushButton(self.contein_all_SSL_SCAN)
        self.START_SSL_SCANButton.setMinimumSize(QtCore.QSize(0, 0))
        self.START_SSL_SCANButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.START_SSL_SCANButton.setStyleSheet("")
        self.START_SSL_SCANButton.setText("")
        self.START_SSL_SCANButton.setIcon(icon5)
        self.START_SSL_SCANButton.setIconSize(QtCore.QSize(50, 50))
        self.START_SSL_SCANButton.setObjectName("START_SSL_SCANButton")
        self.verticalLayout_14.addWidget(self.START_SSL_SCANButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_15.addWidget(self.contein_all_SSL_SCAN)
        self.scrollArea_ssl_scan = QtWidgets.QScrollArea(self.PAGE_SSL_SCAN)
        self.scrollArea_ssl_scan.setWidgetResizable(True)
        self.scrollArea_ssl_scan.setObjectName("scrollArea_ssl_scan")
        self.scrollAreaWidgetContents_ssl_scan = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_ssl_scan.setGeometry(QtCore.QRect(0, 0, 1152, 360))
        self.scrollAreaWidgetContents_ssl_scan.setObjectName("scrollAreaWidgetContents_ssl_scan")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_ssl_scan)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.output_ssl_scan = QtWidgets.QLabel(self.scrollAreaWidgetContents_ssl_scan)
        self.output_ssl_scan.setStyleSheet("color: rgb(255, 255, 255);")
        self.output_ssl_scan.setText("WORK IN PROGRESS THIS TOOL IS NOT WORKING NOW")
        self.output_ssl_scan.setObjectName("output_ssl_scan")
        self.horizontalLayout_8.addWidget(self.output_ssl_scan)
        self.scrollArea_ssl_scan.setWidget(self.scrollAreaWidgetContents_ssl_scan)
        self.verticalLayout_15.addWidget(self.scrollArea_ssl_scan)
        self.contein_send_result_ssl_scal_5 = QtWidgets.QFrame(self.PAGE_SSL_SCAN)
        self.contein_send_result_ssl_scal_5.setMinimumSize(QtCore.QSize(0, 100))
        self.contein_send_result_ssl_scal_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.contein_send_result_ssl_scal_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_send_result_ssl_scal_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_send_result_ssl_scal_5.setObjectName("contein_send_result_ssl_scal_5")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.contein_send_result_ssl_scal_5)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.Send_resultl_ssl_scan_button_5 = QtWidgets.QPushButton(self.contein_send_result_ssl_scal_5)
        self.Send_resultl_ssl_scan_button_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Send_resultl_ssl_scan_button_5.sizePolicy().hasHeightForWidth())
        self.Send_resultl_ssl_scan_button_5.setSizePolicy(sizePolicy)
        self.Send_resultl_ssl_scan_button_5.setMinimumSize(QtCore.QSize(70, 70))
        self.Send_resultl_ssl_scan_button_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Send_resultl_ssl_scan_button_5.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        self.Send_resultl_ssl_scan_button_5.setFont(font)
        self.Send_resultl_ssl_scan_button_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Send_resultl_ssl_scan_button_5.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: transparent;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Send_resultl_ssl_scan_button_5.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Send_resultl_ssl_scan_button_5.setAutoRepeatDelay(301)
        self.Send_resultl_ssl_scan_button_5.setAutoDefault(False)
        self.Send_resultl_ssl_scan_button_5.setDefault(False)
        self.Send_resultl_ssl_scan_button_5.setFlat(False)
        self.Send_resultl_ssl_scan_button_5.setObjectName("Send_resultl_ssl_scan_button_5")
        self.horizontalLayout_18.addWidget(self.Send_resultl_ssl_scan_button_5)
        self.verticalLayout_15.addWidget(self.contein_send_result_ssl_scal_5)
        self.crested_by_ATEAM_page_ssl_scan_5 = QtWidgets.QLabel(self.PAGE_SSL_SCAN)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.crested_by_ATEAM_page_ssl_scan_5.setFont(font)
        self.crested_by_ATEAM_page_ssl_scan_5.setStyleSheet("color: rgb(136, 136, 136);")
        self.crested_by_ATEAM_page_ssl_scan_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.crested_by_ATEAM_page_ssl_scan_5.setObjectName("crested_by_ATEAM_page_ssl_scan_5")
        self.verticalLayout_15.addWidget(self.crested_by_ATEAM_page_ssl_scan_5)
        self.stackedWidget.addWidget(self.PAGE_SSL_SCAN)
        self.PAGE_DATABASE_CHOICE = QtWidgets.QWidget()
        self.PAGE_DATABASE_CHOICE.setObjectName("PAGE_DATABASE_CHOICE")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.PAGE_DATABASE_CHOICE)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.TITLE_DATABASE = QtWidgets.QLabel(self.PAGE_DATABASE_CHOICE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TITLE_DATABASE.sizePolicy().hasHeightForWidth())
        self.TITLE_DATABASE.setSizePolicy(sizePolicy)
        self.TITLE_DATABASE.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(35)
        self.TITLE_DATABASE.setFont(font)
        self.TITLE_DATABASE.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.TITLE_DATABASE.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.TITLE_DATABASE.setObjectName("TITLE_DATABASE")
        self.verticalLayout_18.addWidget(self.TITLE_DATABASE)
        self.contein_all_DATABASE = QtWidgets.QFrame(self.PAGE_DATABASE_CHOICE)
        self.contein_all_DATABASE.setMinimumSize(QtCore.QSize(0, 200))
        self.contein_all_DATABASE.setMaximumSize(QtCore.QSize(16777215, 300))
        self.contein_all_DATABASE.setStyleSheet("background: transparent;\n"
"")
        self.contein_all_DATABASE.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_all_DATABASE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_all_DATABASE.setObjectName("contein_all_DATABASE")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.contein_all_DATABASE)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.contein_all_DATABASE_2 = QtWidgets.QFrame(self.contein_all_DATABASE)
        self.contein_all_DATABASE_2.setMinimumSize(QtCore.QSize(0, 200))
        self.contein_all_DATABASE_2.setMaximumSize(QtCore.QSize(16777215, 500))
        self.contein_all_DATABASE_2.setStyleSheet("background: transparent;\n"
"")
        self.contein_all_DATABASE_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_all_DATABASE_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_all_DATABASE_2.setObjectName("contein_all_DATABASE_2")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.contein_all_DATABASE_2)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.Search_bar = QtWidgets.QLineEdit(self.contein_all_DATABASE_2)
        self.Search_bar.setMinimumSize(QtCore.QSize(300, 30))
        self.Search_bar.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Search_bar.setFont(font)
        self.Search_bar.setStyleSheet("border: 1px solid gray ;\n"
"border-radius: 10px;\n"
"color: white;\n"
"")
        self.Search_bar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Search_bar.setText("")
        self.Search_bar.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Search_bar.setDragEnabled(True)
        self.Search_bar.setObjectName("Search_bar")
        self.verticalLayout_24.addWidget(self.Search_bar, 0, QtCore.Qt.AlignHCenter)
        self.START_DATABASE_Button = QtWidgets.QPushButton(self.contein_all_DATABASE_2)
        self.START_DATABASE_Button.setMinimumSize(QtCore.QSize(0, 0))
        self.START_DATABASE_Button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.START_DATABASE_Button.setStyleSheet("")
        self.START_DATABASE_Button.setText("")
        self.START_DATABASE_Button.setIcon(icon5)
        self.START_DATABASE_Button.setIconSize(QtCore.QSize(50, 50))
        self.START_DATABASE_Button.setObjectName("START_DATABASE_Button")
        self.verticalLayout_24.addWidget(self.START_DATABASE_Button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_17.addWidget(self.contein_all_DATABASE_2)
        
        self.START_DATABASE_Button.clicked.connect(self.search_db)
        
        
        
        self.Contein_database_choice = QtWidgets.QFrame(self.contein_all_DATABASE)
        self.Contein_database_choice.setStyleSheet("QFrame{\n"
"background-color : transparent;\n"
"}\n"
"QPushButton{\n"
"    padding:20px 10px;\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: #000;\n"
"    padding-left:25px  ;\n"
"    \n"
"    background-position: center left;\n"
"    \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Contein_database_choice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Contein_database_choice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Contein_database_choice.setObjectName("Contein_database_choice")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Contein_database_choice)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.public_ip = QtWidgets.QPushButton(self.Contein_database_choice)
        self.public_ip.setMaximumSize(QtCore.QSize(400, 16777215))
        self.public_ip.setStyleSheet("color: rgb(255, 255, 255);")
        self.public_ip.setObjectName("public_ip")
        self.horizontalLayout_3.addWidget(self.public_ip)
        self.public_ip.clicked.connect(self.public_db_open)
        #self.public_ip.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_DATABASE_Public_IP))

        
        self.private_ip = QtWidgets.QPushButton(self.Contein_database_choice)
        self.private_ip.setMaximumSize(QtCore.QSize(400, 16777215))
        self.private_ip.setStyleSheet("color: rgb(255, 255, 255);")
        self.private_ip.setObjectName("private_ip")
        self.horizontalLayout_3.addWidget(self.private_ip)
        ###
        #######################################################################
        #self.private_ip.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_DATABASE_private_IP))
        self.private_ip.clicked.connect(self.private_db_open)
        self.verticalLayout_17.addWidget(self.Contein_database_choice)
        self.verticalLayout_18.addWidget(self.contein_all_DATABASE)
        self.stackedWidget.addWidget(self.PAGE_DATABASE_CHOICE)
        self.PAGE_DATABASE_Public_IP = QtWidgets.QWidget()
        self.PAGE_DATABASE_Public_IP.setObjectName("PAGE_DATABASE_Public_IP")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.PAGE_DATABASE_Public_IP)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.contein_database_public = QtWidgets.QFrame(self.PAGE_DATABASE_Public_IP)
        self.contein_database_public.setMinimumSize(QtCore.QSize(0, 200))
        self.contein_database_public.setMaximumSize(QtCore.QSize(16777215, 300))
        self.contein_database_public.setStyleSheet("background: transparent;\n"
"")
        self.contein_database_public.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_database_public.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_database_public.setObjectName("contein_database_public")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.contein_database_public)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.TITLE_DATABASE_public = QtWidgets.QLabel(self.contein_database_public)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(35)
        self.TITLE_DATABASE_public.setFont(font)
        self.TITLE_DATABASE_public.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.TITLE_DATABASE_public.setAlignment(QtCore.Qt.AlignCenter)
        self.TITLE_DATABASE_public.setObjectName("TITLE_DATABASE_public")
        self.verticalLayout_19.addWidget(self.TITLE_DATABASE_public)
        self.TITTLE_PUBLIC_IP = QtWidgets.QLabel(self.contein_database_public)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(16)
        self.TITTLE_PUBLIC_IP.setFont(font)
        self.TITTLE_PUBLIC_IP.setStyleSheet("color: rgb(255, 255, 255);")
        self.TITTLE_PUBLIC_IP.setAlignment(QtCore.Qt.AlignCenter)
        self.TITTLE_PUBLIC_IP.setObjectName("TITTLE_PUBLIC_IP")
        self.verticalLayout_19.addWidget(self.TITTLE_PUBLIC_IP)
        self.verticalLayout_20.addWidget(self.contein_database_public)
        self.tableWidget_public_ip = QtWidgets.QTableWidget(self.PAGE_DATABASE_Public_IP)
        self.tableWidget_public_ip.setStyleSheet("color: rgb(111, 111, 111);")
        self.tableWidget_public_ip.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_public_ip.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_public_ip.setDefaultDropAction(QtCore.Qt.ActionMask)
        self.tableWidget_public_ip.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget_public_ip.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_public_ip.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_public_ip.setRowCount(9)
        self.tableWidget_public_ip.setColumnCount(27)
        self.tableWidget_public_ip.setObjectName("tableWidget_public_ip")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.Dense7Pattern)
        item.setBackground(brush)
        self.tableWidget_public_ip.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_public_ip.setItem(0, 13, item)
        self.verticalLayout_20.addWidget(self.tableWidget_public_ip)
        self.contein_send_result_public_ip = QtWidgets.QFrame(self.PAGE_DATABASE_Public_IP)
        self.contein_send_result_public_ip.setMinimumSize(QtCore.QSize(0, 100))
        self.contein_send_result_public_ip.setMaximumSize(QtCore.QSize(16777215, 100))
        self.contein_send_result_public_ip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_send_result_public_ip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_send_result_public_ip.setObjectName("contein_send_result_public_ip")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.contein_send_result_public_ip)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        
        self.Send_resultl_public_ip_button = QtWidgets.QPushButton(self.contein_send_result_public_ip)
        self.Send_resultl_public_ip_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Send_resultl_public_ip_button.sizePolicy().hasHeightForWidth())
        self.Send_resultl_public_ip_button.setSizePolicy(sizePolicy)
        self.Send_resultl_public_ip_button.setMinimumSize(QtCore.QSize(70, 70))
        self.Send_resultl_public_ip_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Send_resultl_public_ip_button.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        self.Send_resultl_public_ip_button.setFont(font)
        self.Send_resultl_public_ip_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Send_resultl_public_ip_button.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: transparent;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Send_resultl_public_ip_button.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Send_resultl_public_ip_button.setAutoRepeatDelay(301)
        self.Send_resultl_public_ip_button.setAutoDefault(False)
        self.Send_resultl_public_ip_button.setDefault(False)
        self.Send_resultl_public_ip_button.setFlat(False)
        self.Send_resultl_public_ip_button.setObjectName("Send_resultl_public_ip_button")
        self.horizontalLayout_9.addWidget(self.Send_resultl_public_ip_button)
        self.verticalLayout_20.addWidget(self.contein_send_result_public_ip)
        self.crested_by_ATEAM_page_public_ip = QtWidgets.QLabel(self.PAGE_DATABASE_Public_IP)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.crested_by_ATEAM_page_public_ip.setFont(font)
        self.crested_by_ATEAM_page_public_ip.setStyleSheet("color: rgb(136, 136, 136);")
        self.crested_by_ATEAM_page_public_ip.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.crested_by_ATEAM_page_public_ip.setObjectName("crested_by_ATEAM_page_public_ip")
        self.verticalLayout_20.addWidget(self.crested_by_ATEAM_page_public_ip)
        self.stackedWidget.addWidget(self.PAGE_DATABASE_Public_IP)
        self.PAGE_DATABASE_private_IP = QtWidgets.QWidget()
        self.PAGE_DATABASE_private_IP.setObjectName("PAGE_DATABASE_private_IP")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.PAGE_DATABASE_private_IP)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.contein_all_private = QtWidgets.QFrame(self.PAGE_DATABASE_private_IP)
        self.contein_all_private.setMinimumSize(QtCore.QSize(0, 200))
        self.contein_all_private.setMaximumSize(QtCore.QSize(16777215, 300))
        self.contein_all_private.setStyleSheet("background: transparent;\n"
"")
        self.contein_all_private.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_all_private.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_all_private.setObjectName("contein_all_private")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.contein_all_private)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.tittle_DATABASE_PRIVATE = QtWidgets.QLabel(self.contein_all_private)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(35)
        self.tittle_DATABASE_PRIVATE.setFont(font)
        self.tittle_DATABASE_PRIVATE.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.tittle_DATABASE_PRIVATE.setAlignment(QtCore.Qt.AlignCenter)
        self.tittle_DATABASE_PRIVATE.setObjectName("tittle_DATABASE_PRIVATE")
        self.verticalLayout_21.addWidget(self.tittle_DATABASE_PRIVATE)
        self.tittle_PUBLIC_IP = QtWidgets.QLabel(self.contein_all_private)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(17)
        self.tittle_PUBLIC_IP.setFont(font)
        self.tittle_PUBLIC_IP.setStyleSheet("color: rgb(255, 255, 255);")
        self.tittle_PUBLIC_IP.setAlignment(QtCore.Qt.AlignCenter)
        self.tittle_PUBLIC_IP.setObjectName("tittle_PUBLIC_IP")
        self.verticalLayout_21.addWidget(self.tittle_PUBLIC_IP)
        self.verticalLayout_22.addWidget(self.contein_all_private)
        self.tableWidget_private_ip = QtWidgets.QTableWidget(self.PAGE_DATABASE_private_IP)
        self.tableWidget_private_ip.setStyleSheet("color: rgb(111, 111, 111);")
        self.tableWidget_private_ip.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_private_ip.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_private_ip.setDefaultDropAction(QtCore.Qt.ActionMask)
        self.tableWidget_private_ip.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget_private_ip.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_private_ip.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_private_ip.setRowCount(9)
        self.tableWidget_private_ip.setColumnCount(29)
        self.tableWidget_private_ip.setObjectName("tableWidget_private_ip")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.Dense7Pattern)
        item.setBackground(brush)
        self.tableWidget_private_ip.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_private_ip.setItem(0, 15, item)
        self.verticalLayout_22.addWidget(self.tableWidget_private_ip)
        self.contein_send_result_private_ip = QtWidgets.QFrame(self.PAGE_DATABASE_private_IP)
        self.contein_send_result_private_ip.setMinimumSize(QtCore.QSize(0, 100))
        self.contein_send_result_private_ip.setMaximumSize(QtCore.QSize(16777215, 100))
        self.contein_send_result_private_ip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_send_result_private_ip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_send_result_private_ip.setObjectName("contein_send_result_private_ip")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.contein_send_result_private_ip)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Send_resultl_private_ip = QtWidgets.QPushButton(self.contein_send_result_private_ip)
        self.Send_resultl_private_ip.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Send_resultl_private_ip.sizePolicy().hasHeightForWidth())
        self.Send_resultl_private_ip.setSizePolicy(sizePolicy)
        self.Send_resultl_private_ip.setMinimumSize(QtCore.QSize(70, 70))
        self.Send_resultl_private_ip.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Send_resultl_private_ip.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        self.Send_resultl_private_ip.setFont(font)
        self.Send_resultl_private_ip.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Send_resultl_private_ip.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: transparent;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Send_resultl_private_ip.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Send_resultl_private_ip.setAutoRepeatDelay(301)
        self.Send_resultl_private_ip.setAutoDefault(False)
        self.Send_resultl_private_ip.setDefault(False)
        self.Send_resultl_private_ip.setFlat(False)
        self.Send_resultl_private_ip.setObjectName("Send_resultl_private_ip")
        self.horizontalLayout_10.addWidget(self.Send_resultl_private_ip)
        self.verticalLayout_22.addWidget(self.contein_send_result_private_ip)
        self.crested_by_ATEAM_page_private_ip = QtWidgets.QLabel(self.PAGE_DATABASE_private_IP)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.crested_by_ATEAM_page_private_ip.setFont(font)
        self.crested_by_ATEAM_page_private_ip.setStyleSheet("color: rgb(136, 136, 136);")
        self.crested_by_ATEAM_page_private_ip.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.crested_by_ATEAM_page_private_ip.setObjectName("crested_by_ATEAM_page_private_ip")
        self.verticalLayout_22.addWidget(self.crested_by_ATEAM_page_private_ip)
        self.stackedWidget.addWidget(self.PAGE_DATABASE_private_IP)
        self.PAGE_SETTINGS = QtWidgets.QWidget()
        self.PAGE_SETTINGS.setObjectName("PAGE_SETTINGS")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.PAGE_SETTINGS)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.contein_all_SETTINGS = QtWidgets.QFrame(self.PAGE_SETTINGS)
        self.contein_all_SETTINGS.setMinimumSize(QtCore.QSize(0, 200))
        self.contein_all_SETTINGS.setMaximumSize(QtCore.QSize(16777215, 300))
        self.contein_all_SETTINGS.setStyleSheet("background: transparent;\n"
"")
        self.contein_all_SETTINGS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_all_SETTINGS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_all_SETTINGS.setObjectName("contein_all_SETTINGS")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.contein_all_SETTINGS)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.TITLE_Settings = QtWidgets.QLabel(self.contein_all_SETTINGS)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(35)
        self.TITLE_Settings.setFont(font)
        self.TITLE_Settings.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.TITLE_Settings.setAlignment(QtCore.Qt.AlignCenter)
        self.TITLE_Settings.setObjectName("TITLE_Settings")
        self.verticalLayout_25.addWidget(self.TITLE_Settings)
        self.text_change_password = QtWidgets.QLabel(self.contein_all_SETTINGS)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(10)
        self.text_change_password.setFont(font)
        self.text_change_password.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_change_password.setAlignment(QtCore.Qt.AlignCenter)
        self.text_change_password.setObjectName("text_change_password")
        self.verticalLayout_25.addWidget(self.text_change_password)
        self.verticalLayout_26.addWidget(self.contein_all_SETTINGS)
        self.contein_change_password = QtWidgets.QFrame(self.PAGE_SETTINGS)
        self.contein_change_password.setStyleSheet("background:transparent;")
        self.contein_change_password.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_change_password.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_change_password.setObjectName("contein_change_password")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.contein_change_password)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.reset_password_button = QtWidgets.QPushButton(self.contein_change_password)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_password_button.sizePolicy().hasHeightForWidth())
        self.reset_password_button.setSizePolicy(sizePolicy)
        self.reset_password_button.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.reset_password_button.setFont(font)
        self.reset_password_button.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"\n"
"    border : 2px solid gray;\n"
"    border-radius:8px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.reset_password_button.setObjectName("reset_password_button")
        self.horizontalLayout_11.addWidget(self.reset_password_button)
        self.verticalLayout_26.addWidget(self.contein_change_password)
        
        self.reset_password_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PAGE_RESET_PASSWORD))
        self.reset_password_button.hide()
        self.contein_2fa = QtWidgets.QFrame(self.PAGE_SETTINGS)
        self.contein_2fa.setStyleSheet("background:transparent;")
        self.contein_2fa.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_2fa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_2fa.setObjectName("contein_2fa")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.contein_2fa)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.text_change_tema = QtWidgets.QLabel(self.contein_2fa)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(10)
        self.text_change_tema.setFont(font)
        self.text_change_tema.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_change_tema.setAlignment(QtCore.Qt.AlignCenter)
        self.text_change_tema.setObjectName("text_change_tema")
        self.horizontalLayout_12.addWidget(self.text_change_tema)
        self.verticalLayout_26.addWidget(self.contein_2fa)
        self.contein_change_tema = QtWidgets.QFrame(self.PAGE_SETTINGS)
        self.contein_change_tema.setStyleSheet("background:transparent;")
        self.contein_change_tema.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_change_tema.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_change_tema.setObjectName("contein_change_tema")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.contein_change_tema)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.Golden_Button = QtWidgets.QPushButton(self.contein_change_tema)
        self.Golden_Button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Golden_Button.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"\n"
"    border : 2px solid gray;\n"
"    border-radius:8px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Golden_Button.setObjectName("Golden_Button")
        self.horizontalLayout_13.addWidget(self.Golden_Button)
        
        
        
        self.Golden_Button.clicked.connect(self.color_gold)        
        self.Greeen_Button = QtWidgets.QPushButton(self.contein_change_tema)
        self.Greeen_Button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Greeen_Button.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"\n"
"    border : 2px solid gray;\n"
"    border-radius:8px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Greeen_Button.setObjectName("Greeen_Button")
        self.horizontalLayout_13.addWidget(self.Greeen_Button)
        self.Greeen_Button.clicked.connect(self.color_green)
        self.Skye_Blue_Button = QtWidgets.QPushButton(self.contein_change_tema)
        self.Skye_Blue_Button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Skye_Blue_Button.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"\n"
"    border : 2px solid gray;\n"
"    border-radius:8px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Skye_Blue_Button.setObjectName("Skye_Blue_Button")
        self.horizontalLayout_13.addWidget(self.Skye_Blue_Button)
        self.Skye_Blue_Button.clicked.connect(self.color_skyblue)
        self.Red_Button = QtWidgets.QPushButton(self.contein_change_tema)
        self.Red_Button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Red_Button.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"\n"
"    border : 2px solid gray;\n"
"    border-radius:8px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Red_Button.setObjectName("Red_Button")
        self.horizontalLayout_13.addWidget(self.Red_Button)
        self.Red_Button.clicked.connect(self.color_red)
        self.default_purpleButton = QtWidgets.QPushButton(self.contein_change_tema)
        self.default_purpleButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.default_purpleButton.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"    border : 2px solid gray;\n"
"    border-radius:8px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.default_purpleButton.setObjectName("default_purpleButton")
        self.horizontalLayout_13.addWidget(self.default_purpleButton)
        self.verticalLayout_26.addWidget(self.contein_change_tema)
        self.default_purpleButton.clicked.connect(self.color_purple)
        self.crested_by_ATEAM_page_ssl_scan = QtWidgets.QLabel(self.PAGE_SETTINGS)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.crested_by_ATEAM_page_ssl_scan.setFont(font)
        self.crested_by_ATEAM_page_ssl_scan.setStyleSheet("color: rgb(136, 136, 136);")
        self.crested_by_ATEAM_page_ssl_scan.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.crested_by_ATEAM_page_ssl_scan.setObjectName("crested_by_ATEAM_page_ssl_scan")
        self.verticalLayout_26.addWidget(self.crested_by_ATEAM_page_ssl_scan)
        self.stackedWidget.addWidget(self.PAGE_SETTINGS)
        self.PAGE_HELP = QtWidgets.QWidget()
        self.PAGE_HELP.setObjectName("PAGE_HELP")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.PAGE_HELP)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.contein_title_help = QtWidgets.QFrame(self.PAGE_HELP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contein_title_help.sizePolicy().hasHeightForWidth())
        self.contein_title_help.setSizePolicy(sizePolicy)
        self.contein_title_help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_title_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_title_help.setObjectName("contein_title_help")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.contein_title_help)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.TITLE_HELP_2 = QtWidgets.QLabel(self.contein_title_help)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(35)
        self.TITLE_HELP_2.setFont(font)
        self.TITLE_HELP_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.TITLE_HELP_2.setAlignment(QtCore.Qt.AlignCenter)
        self.TITLE_HELP_2.setObjectName("TITLE_HELP_2")
        self.verticalLayout_30.addWidget(self.TITLE_HELP_2)
        self.verticalLayout_27.addWidget(self.contein_title_help)
        self.contein_all_help = QtWidgets.QFrame(self.PAGE_HELP)
        self.contein_all_help.setMinimumSize(QtCore.QSize(0, 200))
        self.contein_all_help.setMaximumSize(QtCore.QSize(16777215, 300))
        self.contein_all_help.setStyleSheet("background: transparent;\n"
"")
        self.contein_all_help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_all_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_all_help.setObjectName("contein_all_help")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.contein_all_help)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.empty = QtWidgets.QLabel(self.contein_all_help)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)
        self.empty.setFont(font)
        self.empty.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.empty.setText("")
        self.empty.setAlignment(QtCore.Qt.AlignCenter)
        self.empty.setObjectName("empty")
        self.verticalLayout_28.addWidget(self.empty)
        self.Mail_object = QtWidgets.QLineEdit(self.contein_all_help)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mail_object.sizePolicy().hasHeightForWidth())
        self.Mail_object.setSizePolicy(sizePolicy)
        self.Mail_object.setMinimumSize(QtCore.QSize(0, 40))
        self.Mail_object.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Mail_object.setFont(font)
        self.Mail_object.setStyleSheet("border: 1px solid gray ;\n"
"border-radius: 10px;\n"
"color: white;")
        self.Mail_object.setAlignment(QtCore.Qt.AlignCenter)
        self.Mail_object.setObjectName("Mail_object")
        self.verticalLayout_28.addWidget(self.Mail_object)
        self.plainTextEdit_HELP = QtWidgets.QLineEdit(self.contein_all_help)
        self.plainTextEdit_HELP.setStyleSheet("color: rgb(255, 255, 255);")

        self.plainTextEdit_HELP.setReadOnly(False)
        self.plainTextEdit_HELP.setMaximumHeight(16777209)
        self.plainTextEdit_HELP.setObjectName("plainTextEdit_HELP")
        self.verticalLayout_28.addWidget(self.plainTextEdit_HELP)
        self.verticalLayout_27.addWidget(self.contein_all_help)
        self.contein_send_result_ssl_scal_6 = QtWidgets.QFrame(self.PAGE_HELP)
        self.contein_send_result_ssl_scal_6.setMinimumSize(QtCore.QSize(0, 100))
        self.contein_send_result_ssl_scal_6.setMaximumSize(QtCore.QSize(16777215, 100))
        self.contein_send_result_ssl_scal_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contein_send_result_ssl_scal_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contein_send_result_ssl_scal_6.setObjectName("contein_send_result_ssl_scal_6")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.contein_send_result_ssl_scal_6)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.Send_resultl_ssl_scan_button_6 = QtWidgets.QPushButton(self.contein_send_result_ssl_scal_6)
        self.Send_resultl_ssl_scan_button_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Send_resultl_ssl_scan_button_6.sizePolicy().hasHeightForWidth())
        self.Send_resultl_ssl_scan_button_6.setSizePolicy(sizePolicy)
        self.Send_resultl_ssl_scan_button_6.setMinimumSize(QtCore.QSize(80, 80))
        self.Send_resultl_ssl_scan_button_6.setMaximumSize(QtCore.QSize(130, 16777215))
        self.Send_resultl_ssl_scan_button_6.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        self.Send_resultl_ssl_scan_button_6.setFont(font)
        self.Send_resultl_ssl_scan_button_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Send_resultl_ssl_scan_button_6.setStyleSheet("QFrame{\n"
"background-color :transparent;\n"
"}\n"
"QPushButton{\n"
"    border : none;\n"
"    border-radius:8px;\n"
"    background-color: transparent;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(48, 48, 48);\n"
"}")
        self.Send_resultl_ssl_scan_button_6.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Send_resultl_ssl_scan_button_6.setAutoRepeatDelay(301)
        self.Send_resultl_ssl_scan_button_6.setAutoDefault(False)
        self.Send_resultl_ssl_scan_button_6.setDefault(False)
        self.Send_resultl_ssl_scan_button_6.setFlat(False)
        self.Send_resultl_ssl_scan_button_6.setObjectName("Send_resultl_ssl_scan_button_6")
        self.horizontalLayout_19.addWidget(self.Send_resultl_ssl_scan_button_6)
        self.verticalLayout_27.addWidget(self.contein_send_result_ssl_scal_6)
        
        self.Send_resultl_ssl_scan_button_6.clicked.connect(self.send_dilemma)
        self.stackedWidget.addWidget(self.PAGE_HELP)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.verticalLayout_6.addWidget(self.page_retro_allPages)
        self.horizontalLayout_2.addWidget(self.contein_page_background)
        self.verticalLayout.addWidget(self.body)
        IPSEARCH_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(IPSEARCH_window)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_contein_output_IPHUNTER.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(IPSEARCH_window)

    def retranslateUi(self, IPSEARCH_window):
        
        _translate = QtCore.QCoreApplication.translate
        IPSEARCH_window.setWindowTitle(_translate("IPSEARCH_window", "MainWindow"))
        #self.IP_HUNTER_tittle.setText(_translate("IPSEARCH_window", mail))
        self.LOG_IN.setText(_translate("IPSEARCH_window", "LOG-IN"))
        self.Home_IP_HUNTER.setText(_translate("IPSEARCH_window", "HOME"))
        self.WHOIS.setText(_translate("IPSEARCH_window", "WHOIS"))
        self.ABUSE.setText(_translate("IPSEARCH_window", " ABUSE"))
        self.RADAR.setText(_translate("IPSEARCH_window", "RADAR"))
        self.SSL_SCAN.setText(_translate("IPSEARCH_window", "SSL SCAN"))
        self.DATABASE.setText(_translate("IPSEARCH_window", "DATABASE"))
        self.SETTINGS.setText(_translate("IPSEARCH_window", "SETTINGS"))
        self.SEND_EMAIL.setText(_translate("IPSEARCH_window", "HELP"))
        self.label_IPHUNTER_2.setText(_translate("IPSEARCH_window", "LOG - IN"))
        self.lineEdit_E_MAIL_2.setPlaceholderText(_translate("IPSEARCH_window", "E-mail"))
        self.lineEdit_PASSWORD_2.setPlaceholderText(_translate("IPSEARCH_window", "Password"))
        self.pushButton_2.setText(_translate("IPSEARCH_window", "forgot your password?"))
        self.label_message_sendcode_2.setText(_translate("IPSEARCH_window", " the access code will be sent to your e-mail:"))
        self.SEND_CODEButton_2.setText(_translate("IPSEARCH_window", "send code"))
        self.label_want_register_2.setText(_translate("IPSEARCH_window", " you are not registered yet ?"))
        self.SING_UPButton_2.setText(_translate("IPSEARCH_window", "sing-up"))
        self.label_LOG_IN_2.setText(_translate("IPSEARCH_window", "insert code"))
        self.lineEdit_PASSWORD_3.setPlaceholderText(_translate("IPSEARCH_window", "Insert Code"))
        self.SEND_CODEButton_3.setText(_translate("IPSEARCH_window", "Start the Hunt"))
        self.label_IPHUNTER_3.setText(_translate("IPSEARCH_window", "reset password"))
        self.lineEdit_USERNAME.setPlaceholderText(_translate("IPSEARCH_window", "Enter E-mail"))
        self.send_codeButton_for_reset.setText(_translate("IPSEARCH_window", "Send Code "))
        self.label_reset_password.setText(_translate("IPSEARCH_window", "Create New  Password :"))
        self.lineEdit_entercode.setPlaceholderText(_translate("IPSEARCH_window", "Enter Code"))
        self.lineEdit_new_password.setPlaceholderText(_translate("IPSEARCH_window", "New Password"))
        self.lineEdit_conf_password.setPlaceholderText(_translate("IPSEARCH_window", " Confirm New Password"))
        self.Sing_upButton.setText(_translate("IPSEARCH_window", "SET"))
        self.label_Register.setText(_translate("IPSEARCH_window", "REGISTER"))
        self.lineEdit_USERNAME_2.setPlaceholderText(_translate("IPSEARCH_window", "USERNAME"))
        self.lineEdit_E_MAIL_3.setPlaceholderText(_translate("IPSEARCH_window", "E-mail"))
        self.lineEdit_PASSWORD_5.setPlaceholderText(_translate("IPSEARCH_window", "PASSWORD"))
        self.Sing_upButton_2.setText(_translate("IPSEARCH_window", "sing-up"))
        self.TITLE_IP_HUNTER.setText(_translate("IPSEARCH_window", "IP HUNTER"))
        self.Type_an_IP_AddressIPHUNTER.setPlaceholderText(_translate("IPSEARCH_window", "Type an IP Address"))
        self.START_IPSEARHButton.setShortcut(_translate("IPSEARCH_window", "Ctrl+R, Ctrl+R"))
        self.label_7.setText(_translate("IPSEARCH_window", ""))
        self.tabWidget_contein_output_IPHUNTER.setTabText(self.tabWidget_contein_output_IPHUNTER.indexOf(self.whois_output), _translate("IPSEARCH_window", "WHOIS"))
        self.label_6.setText(_translate("IPSEARCH_window", ""))
        self.tabWidget_contein_output_IPHUNTER.setTabText(self.tabWidget_contein_output_IPHUNTER.indexOf(self.abuse_output), _translate("IPSEARCH_window", "ABUSE"))
        self.label_5.setText(_translate("IPSEARCH_window", ""))
        self.tabWidget_contein_output_IPHUNTER.setTabText(self.tabWidget_contein_output_IPHUNTER.indexOf(self.NMAP_output), _translate("IPSEARCH_window", "NMAP"))
        self.label_type.setText(_translate("IPSEARCH_window", ""))
        self.tabWidget_contein_output_IPHUNTER.setTabText(self.tabWidget_contein_output_IPHUNTER.indexOf(self.output_type), _translate("IPSEARCH_window", "Type"))
       
        self.label_class.setText(_translate("IPSEARCH_window", ""))
        self.tabWidget_contein_output_IPHUNTER.setTabText(self.tabWidget_contein_output_IPHUNTER.indexOf(self.output_class), _translate("IPSEARCH_window", "Class"))
        self.label_hostname.setText(_translate("IPSEARCH_window", ""))
        self.tabWidget_contein_output_IPHUNTER.setTabText(self.tabWidget_contein_output_IPHUNTER.indexOf(self.output_hostname), _translate("IPSEARCH_window", "Hostname"))
        self.label_macaddress.setText(_translate("IPSEARCH_window", ""))
        self.tabWidget_contein_output_IPHUNTER.setTabText(self.tabWidget_contein_output_IPHUNTER.indexOf(self.output_macaddres), _translate("IPSEARCH_window", "mac address"))
        self.Send_result_ip_hunter.setText(_translate("IPSEARCH_window", "SEND RESULT"))
        self.created_by_ATEAM_IP_HUNTER.setText(_translate("IPSEARCH_window", "Created by : A-TEAM"))
        self.TITLE_WHOIS.setText(_translate("IPSEARCH_window", "WHOIS"))
        self.Type_an_IP_Address_WHOIS.setPlaceholderText(_translate("IPSEARCH_window", "Type an IP Address"))
        self.START_WHOISButton.setShortcut(_translate("IPSEARCH_window", "Ctrl+R, Ctrl+R"))
        self.Send_resultl_ssl_scan_button_2.setText(_translate("IPSEARCH_window", "SEND RESULT"))
        self.crested_by_ATEAM_page_ssl_scan_2.setText(_translate("IPSEARCH_window", "Created by : A-TEAM"))
        self.TITLE_ABUSE.setText(_translate("IPSEARCH_window", "ABUSE"))
        self.Type_an_IP_Address_ABUSE.setPlaceholderText(_translate("IPSEARCH_window", "Type an IP Address"))
        self.START_ABUSEButton.setShortcut(_translate("IPSEARCH_window", "Ctrl+R, Ctrl+R"))
        self.Send_resultl_ssl_scan_button_3.setText(_translate("IPSEARCH_window", "SEND RESULT"))
        self.crested_by_ATEAM_page_ssl_scan_3.setText(_translate("IPSEARCH_window", "Created by : A-TEAM"))
        self.TITLE_RADAR.setText(_translate("IPSEARCH_window", "RADAR"))
        self.Type_an_IP_Address_radar.setPlaceholderText(_translate("IPSEARCH_window", "Type an IP Address"))
        self.START_RADARButton_radar.setShortcut(_translate("IPSEARCH_window", "Ctrl+R, Ctrl+R"))
        self.Send_resultl_ssl_scan_button_4.setText(_translate("IPSEARCH_window", "SEND RESULT"))
        self.crested_by_ATEAM_page_ssl_scan_4.setText(_translate("IPSEARCH_window", "Created by : A-TEAM"))
        self.TITLE_SSL_SCAN.setText(_translate("IPSEARCH_window", "SSL SCAN"))
        self.Type_an_IP_Address_ssl_scan.setPlaceholderText(_translate("IPSEARCH_window", "Type an IP Address"))
        self.START_SSL_SCANButton.setShortcut(_translate("IPSEARCH_window", "Ctrl+R, Ctrl+R"))
        self.Send_resultl_ssl_scan_button_5.setText(_translate("IPSEARCH_window", "SEND RESULT"))
        self.crested_by_ATEAM_page_ssl_scan_5.setText(_translate("IPSEARCH_window", "Created by : A-TEAM"))
        self.TITLE_DATABASE.setText(_translate("IPSEARCH_window", "DATABASE"))
        self.Search_bar.setPlaceholderText(_translate("IPSEARCH_window", "Search Bar"))
        self.START_DATABASE_Button.setShortcut(_translate("IPSEARCH_window", "Ctrl+R, Ctrl+R"))
        self.public_ip.setText(_translate("IPSEARCH_window", "PUBLIC IP"))
        self.private_ip.setText(_translate("IPSEARCH_window", "PRIVATE IP"))
        self.TITLE_DATABASE_public.setText(_translate("IPSEARCH_window", "DATABASE"))
        self.TITTLE_PUBLIC_IP.setText(_translate("IPSEARCH_window", "PUBLIC IP"))
        item = self.tableWidget_public_ip.horizontalHeaderItem(0)
        item.setText(_translate("IPSEARCH_window", "ip address"))
        item = self.tableWidget_public_ip.horizontalHeaderItem(1)
        item.setText(_translate("IPSEARCH_window", "port"))
        item = self.tableWidget_public_ip.horizontalHeaderItem(2)
        item.setText(_translate("IPSEARCH_window", "name"))
        item = self.tableWidget_public_ip.horizontalHeaderItem(3)
        item.setText(_translate("IPSEARCH_window", "protocol"))
        item = self.tableWidget_public_ip.horizontalHeaderItem(4)
        item.setText(_translate("IPSEARCH_window", "state"))
        item = self.tableWidget_public_ip.horizontalHeaderItem(5)
        item.setText(_translate("IPSEARCH_window", "product"))
        item = self.tableWidget_public_ip.horizontalHeaderItem(6)
        item.setText(_translate("IPSEARCH_window", "extrainfo"))
        item = self.tableWidget_public_ip.horizontalHeaderItem(7)
        item.setText(_translate("IPSEARCH_window", "reason"))
        item = self.tableWidget_public_ip.horizontalHeaderItem(8)
        item.setText(_translate("IPSEARCH_window", "version"))
        item = self.tableWidget_public_ip.horizontalHeaderItem(9)
        item.setText(_translate("IPSEARCH_window", "conf"))
        item = self.tableWidget_public_ip.horizontalHeaderItem(10)
        item.setText(_translate("IPSEARCH_window", "cpe"))
        item = self.tableWidget_public_ip.horizontalHeaderItem(11)
        item.setText(_translate("IPSEARCH_window", "scan data"))
        item = self.tableWidget_public_ip.horizontalHeaderItem(12)
        item.setText(_translate("IPSEARCH_window", "scan username"))
        __sortingEnabled = self.tableWidget_public_ip.isSortingEnabled()
        self.tableWidget_public_ip.setSortingEnabled(False)
        self.tableWidget_public_ip.setSortingEnabled(__sortingEnabled)
        self.Send_resultl_public_ip_button.setText(_translate("IPSEARCH_window", "BACK"))
        self.Send_resultl_public_ip_button.clicked.connect(self.back_to)
        
        
        
        self.crested_by_ATEAM_page_public_ip.setText(_translate("IPSEARCH_window", "Created by : A-TEAM"))
        self.tittle_DATABASE_PRIVATE.setText(_translate("IPSEARCH_window", "DATABASE"))
        self.tittle_PUBLIC_IP.setText(_translate("IPSEARCH_window", "PRIVATE IP"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(0)
        item.setText(_translate("IPSEARCH_window", "ip_address"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(1)
        item.setText(_translate("IPSEARCH_window", "port"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(2)
        item.setText(_translate("IPSEARCH_window", "name"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(3)
        item.setText(_translate("IPSEARCH_window", "protocol"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(4)
        item.setText(_translate("IPSEARCH_window", "state"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(5)
        item.setText(_translate("IPSEARCH_window", "products"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(6)
        item.setText(_translate("IPSEARCH_window", "mac_address"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(7)
        item.setText(_translate("IPSEARCH_window", "vendor"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(8)
        item.setText(_translate("IPSEARCH_window", "extrainfo"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(9)
        item.setText(_translate("IPSEARCH_window", "reason"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(10)
        item.setText(_translate("IPSEARCH_window", "versione"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(11)
        item.setText(_translate("IPSEARCH_window", "conf"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(12)
        item.setText(_translate("IPSEARCH_window", "cpe"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(13)
        item.setText(_translate("IPSEARCH_window", "scan data"))
        item = self.tableWidget_private_ip.horizontalHeaderItem(14)
        item.setText(_translate("IPSEARCH_window", "scan username"))
        __sortingEnabled = self.tableWidget_private_ip.isSortingEnabled()
        self.tableWidget_private_ip.setSortingEnabled(False)
        self.tableWidget_private_ip.setSortingEnabled(__sortingEnabled)
        self.Send_resultl_private_ip.setText(_translate("IPSEARCH_window", "BACK"))
        self.Send_resultl_private_ip.clicked.connect(self.back_to)
        self.crested_by_ATEAM_page_private_ip.setText(_translate("IPSEARCH_window", "Created by : A-TEAM"))
        self.TITLE_Settings.setText(_translate("IPSEARCH_window", "SETTINGS"))
        self.text_change_password.setText(_translate("IPSEARCH_window", " want change your password ?"))
        self.text_change_password.hide()
        self.reset_password_button.setText(_translate("IPSEARCH_window", "RESET PASSWORD"))
        self.text_change_tema.setText(_translate("IPSEARCH_window", "change Tema"))
        self.Golden_Button.setText(_translate("IPSEARCH_window", "GOLDEN"))
        self.Greeen_Button.setText(_translate("IPSEARCH_window", "GREEN"))
        self.Skye_Blue_Button.setText(_translate("IPSEARCH_window", "SKY BLUE"))
        self.Red_Button.setText(_translate("IPSEARCH_window", "RED"))
        self.default_purpleButton.setText(_translate("IPSEARCH_window", "ORIGINAL_PURPLE"))
        self.crested_by_ATEAM_page_ssl_scan.setText(_translate("IPSEARCH_window", "Created by : A-TEAM"))
        self.TITLE_HELP_2.setText(_translate("IPSEARCH_window", "HELP"))
        self.Mail_object.setPlaceholderText(_translate("IPSEARCH_window", "Mail-object"))
        self.Send_resultl_ssl_scan_button_6.setText(_translate("IPSEARCH_window", "SEND DILEMMA"))
        
        
        #--------------------------CHIUDIAMO I BOTTONI PRIMA DEL LOG IN----------------------------------
        
        self.ABUSE.hide()
        self.DATABASE.hide()
        self.Home_IP_HUNTER.hide()
        self.SSL_SCAN.hide()
        self.WHOIS.hide()
        self.SETTINGS.hide()
        self.RADAR.hide()
        self.output_type.hide()
        

#--------------------------- CAMBIAMENTO DEI BACKGROUND NEI SETTINGS------------------------------------
    def color_gold(self):
        import sign_in
        self.contein_page_background.setStyleSheet("background-image: url(images/bg_IPh_gold.png);")
        with sqlite3.connect("IpHunter.db") as db:                # creazione di un database                                                         
                c = db.cursor()
        setting = "background-image: url(images/bg_IPh_gold.png);"
        modify = ("UPDATE user_cred SET settings = ? WHERE email = ?")
        data =  [(setting), (sign_in.mail)]
        c.execute(modify, data)
        db.commit()            
    def color_green(self):
        import sign_in
        self.contein_page_background.setStyleSheet("background-image: url(images/bg_IPh_green.png);")
        with sqlite3.connect("IpHunter.db") as db:                # creazione di un database                                                         
                c = db.cursor()
        setting = "background-image: url(images/bg_IPh_green.png);"
        modify = ("UPDATE user_cred SET settings = ? WHERE email = ?")
        data =  [(setting), (sign_in.mail)]
        c.execute(modify, data)
        db.commit()          
    def color_skyblue(self):
        import sign_in
        self.contein_page_background.setStyleSheet("background-image: url(images/bg_IPh_skyblue.png);")        
        with sqlite3.connect("IpHunter.db") as db:                # creazione di un database                                                         
                c = db.cursor()
        setting = "background-image: url(images/bg_IPh_skyblue.png);"
        modify = ("UPDATE user_cred SET settings = ? WHERE email = ?")
        data =  [(setting), (sign_in.mail)]
        c.execute(modify, data)
        db.commit()    
    def color_red(self):
        import sign_in
        self.contein_page_background.setStyleSheet("background-image: url(images/bg_IPh_red.png);")       
        with sqlite3.connect("IpHunter.db") as db:                # creazione di un database                                                         
                c = db.cursor()
        setting = "background-image: url(images/bg_IPh_red.png);"
        modify = ("UPDATE user_cred SET settings = ? WHERE email = ?")
        data =  [(setting), (sign_in.mail)]
        c.execute(modify, data)
        db.commit()
    
    def color_purple(self):
        import sign_in
        self.contein_page_background.setStyleSheet("background-image: url(images/bg_IPh.png);")
        with sqlite3.connect("IpHunter.db") as db:                # creazione di un database                                                         
                c = db.cursor()
        setting = "background-image: url(images/bg_IPh.png);"
        modify = ("UPDATE user_cred SET settings = ? WHERE email = ?")
        data =  [(sign_in.mail), (setting)]
        c.execute(modify, data)

    def personal_color(self):
        # fare la query nel database
        import sign_in
        with sqlite3.connect("IpHunter.db") as db:                # creazione di un database                                                         
                c = db.cursor()
        select = ("SELECT settings FROM user_cred WHERE email = ?")
        data = [(sign_in.mail)]
        c.execute(select, data)
        setting = c.fetchone()
               
        self.contein_page_background.setStyleSheet(setting[0])
                     

#----------------------------------------FUNZIONI GENERALI------------------------------------------------------------------

    def hunter(self):
        getvar = self.Type_an_IP_AddressIPHUNTER.text()
        if IPAddress(getvar).is_private():
                
                self.label_7.clear()
                self.label_6.clear()
                self.label_5.clear()
                self.look_vendor()
                self.host_name()
                self.class_def()
                
                self.insert_data()
                pass
                # devo richiamare le funzione nel caso in cui fosse pubblico
        else:
                self.label_class.clear()
                self.label_hostname.clear()
                self.whois_hunt()
                self.IPabuse_hunt()
                self.scan()
                self.insert_publicdata()

        
    def radar(self):
        self.output_radar.clear()   
        self.IP_geo()
        


#-------------------FUNZIONI PER IL DATABASE-----------------------------------------------------------
    def public_db_open(self):
        self.database_public_ip()          
        self.stackedWidget.setCurrentWidget(self.PAGE_DATABASE_Public_IP)
        
        
    
    def private_db_open(self):
        self.database_private_ip()          
        self.stackedWidget.setCurrentWidget(self.PAGE_DATABASE_private_IP)
        
        
    def search_db(self):
        self.search_db_tool()
        
        
#-------------------------------FUNZIONI DI BACK PAGE---------------------------------------------------------------------------

    def back_to(self):
        self.stackedWidget.setCurrentWidget(self.PAGE_DATABASE_CHOICE)          
        
        
#-----------------------------------------------------------------------------------------------------        
    def menu_appear(self):
        width = self.contein_left_menu.width()


        # SET MAX WIDTH
        if width == 40:
                widthExtended = 180
        else:
                widthExtended = 40

        # ANIMATION
        self.animation = QPropertyAnimation(self.contein_left_menu, b"minimumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    def page_code(self):
        self.login()
        #self.stackedWidget.setCurrentWidget(self.PAGE_INSERT_CODE) 
    
    def after_register(self):
        self.register()
        #self.stackedWidget.setCurrentWidget(self.LOG_IN_2)
    
    def start(self):
        import sign_in
        self.verify()
        #cambio delle settings del background


    
import newsource


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IPSEARCH_window = QtWidgets.QMainWindow()
    ui = Ui_IPSEARCH_window()
    ui.setupUi(IPSEARCH_window)
    IPSEARCH_window.show()
    IP_DB()
    #create_db()
    sys.exit(app.exec_())
