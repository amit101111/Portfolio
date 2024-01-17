# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(795, 597)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.MainFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.MainFrame)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.headerFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.headerContent = QLabel(self.headerFrame)
        self.headerContent.setObjectName(u"headerContent")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.headerContent.setFont(font)
        self.headerContent.setLayoutDirection(Qt.LeftToRight)
        self.headerContent.setFrameShape(QFrame.Panel)
        self.headerContent.setFrameShadow(QFrame.Raised)
        self.headerContent.setLineWidth(4)

        self.gridLayout_2.addWidget(self.headerContent, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.bodyLayout = QGridLayout()
        self.bodyLayout.setSpacing(3)
        self.bodyLayout.setObjectName(u"bodyLayout")
        self.bodyLayout.setContentsMargins(0, 0, 0, 0)
        self.rightTop = QLabel(self.MainFrame)
        self.rightTop.setObjectName(u"rightTop")
        self.rightTop.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.bodyLayout.addWidget(self.rightTop, 0, 1, 1, 1)

        self.leftDown = QLabel(self.MainFrame)
        self.leftDown.setObjectName(u"leftDown")
        self.leftDown.setAlignment(Qt.AlignCenter)

        self.bodyLayout.addWidget(self.leftDown, 1, 0, 1, 1)

        self.rightDown = QLabel(self.MainFrame)
        self.rightDown.setObjectName(u"rightDown")
        self.rightDown.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.bodyLayout.addWidget(self.rightDown, 1, 1, 1, 1)

        self.date_timeLayout = QFrame(self.MainFrame)
        self.date_timeLayout.setObjectName(u"date_timeLayout")
        self.date_timeLayout.setFrameShape(QFrame.StyledPanel)
        self.date_timeLayout.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.date_timeLayout)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.timeLayout = QHBoxLayout()
        self.timeLayout.setSpacing(0)
        self.timeLayout.setObjectName(u"timeLayout")
        self.time = QLabel(self.date_timeLayout)
        self.time.setObjectName(u"time")

        self.timeLayout.addWidget(self.time)

        self.currentTime = QLabel(self.date_timeLayout)
        self.currentTime.setObjectName(u"currentTime")

        self.timeLayout.addWidget(self.currentTime)

        self.timeLayout.setStretch(0, 2)
        self.timeLayout.setStretch(1, 8)

        self.verticalLayout_3.addLayout(self.timeLayout)

        self.dateLayout = QHBoxLayout()
        self.dateLayout.setSpacing(0)
        self.dateLayout.setObjectName(u"dateLayout")
        self.date = QLabel(self.date_timeLayout)
        self.date.setObjectName(u"date")

        self.dateLayout.addWidget(self.date)

        self.currentDate = QLabel(self.date_timeLayout)
        self.currentDate.setObjectName(u"currentDate")

        self.dateLayout.addWidget(self.currentDate)

        self.dateLayout.setStretch(0, 2)
        self.dateLayout.setStretch(1, 8)

        self.verticalLayout_3.addLayout(self.dateLayout)


        self.bodyLayout.addWidget(self.date_timeLayout, 0, 0, 1, 1)

        self.bodyLayout.setRowStretch(0, 1)
        self.bodyLayout.setRowStretch(1, 3)
        self.bodyLayout.setColumnStretch(0, 1)
        self.bodyLayout.setColumnStretch(1, 3)

        self.verticalLayout.addLayout(self.bodyLayout)

        self.footerLayout = QFrame(self.MainFrame)
        self.footerLayout.setObjectName(u"footerLayout")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.footerLayout.sizePolicy().hasHeightForWidth())
        self.footerLayout.setSizePolicy(sizePolicy)
        self.footerLayout.setAutoFillBackground(False)
        self.footerLayout.setFrameShape(QFrame.NoFrame)
        self.footerLayout.setFrameShadow(QFrame.Raised)
        self.footerLayout.setLineWidth(2)
        self.gridLayout_3 = QGridLayout(self.footerLayout)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.footerContent = QLabel(self.footerLayout)
        self.footerContent.setObjectName(u"footerContent")
        sizePolicy.setHeightForWidth(self.footerContent.sizePolicy().hasHeightForWidth())
        self.footerContent.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(6)
        self.footerContent.setFont(font1)

        self.gridLayout_3.addWidget(self.footerContent, 0, 0, 1, 1, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footerLayout, 0, Qt.AlignRight|Qt.AlignBottom)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.MainFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 795, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.headerContent.setText(QCoreApplication.translate("MainWindow", u"Welcome to my Portfolio Website", None))
        self.rightTop.setText(QCoreApplication.translate("MainWindow", u"AMIT SARKER KISHOR\n"
"Contact: +8801643395505\n"
"Email: amit.cityu.cse@gmail.com\n"
"Linkedin: https://www.linkedin.com/in/amit101111/", None))
        self.leftDown.setText(QCoreApplication.translate("MainWindow", u"LeftContent", None))
        self.rightDown.setText(QCoreApplication.translate("MainWindow", u"MainBody", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"Time :", None))
        self.currentTime.setText(QCoreApplication.translate("MainWindow", u"10:07 PM", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.currentDate.setText(QCoreApplication.translate("MainWindow", u"17/01/2024", None))
        self.footerContent.setText(QCoreApplication.translate("MainWindow", u"@Copyright 2024 by Amit Sarker Kishor", None))
    # retranslateUi

