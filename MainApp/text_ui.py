# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_textWindow(object):
    def setupUi(self, textWindow):
        textWindow.setObjectName("textWindow")
        textWindow.resize(1920, 1082)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        textWindow.setFont(font)
        textWindow.setMouseTracking(True)
        textWindow.setToolTipDuration(-2)
        textWindow.setAutoFillBackground(False)
        textWindow.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        textWindow.setIconSize(QtCore.QSize(24, 24))
        textWindow.setAnimated(True)
        textWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(textWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    background: #FFFFFF;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(90, 150, 451, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Newsreader")
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background: transparent;\n"
"border: none;\n"
"color: #191919;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 40, 641, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Newsreader")
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background: transparent;\n"
"border: none;\n"
"color: #426B1F;\n"
"")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.videoDetectorButton = QtWidgets.QPushButton(self.centralwidget)
        self.videoDetectorButton.setGeometry(QtCore.QRect(1350, 40, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Newsreader")
        font.setPointSize(13)
        self.videoDetectorButton.setFont(font)
        self.videoDetectorButton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.videoDetectorButton.setObjectName("videoDetectorButton")
        self.whoWeAreButton = QtWidgets.QPushButton(self.centralwidget)
        self.whoWeAreButton.setGeometry(QtCore.QRect(1530, 40, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Newsreader")
        font.setPointSize(13)
        self.whoWeAreButton.setFont(font)
        self.whoWeAreButton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.whoWeAreButton.setObjectName("whoWeAreButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(1710, 40, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Newsreader")
        font.setPointSize(15)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton {\n"
"    background-color: #426B1F;\n"
"    color: white;\n"
"    border-radius: 30px;\n"
"    padding: 5px 20px;\n"
"}")
        self.backButton.setObjectName("backButton")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(960, 190, 931, 601))
        font = QtGui.QFont()
        font.setFamily("Newsreader")
        font.setPointSize(15)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.backButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.backButton_2.setGeometry(QtCore.QRect(1460, 800, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Newsreader")
        font.setPointSize(15)
        self.backButton_2.setFont(font)
        self.backButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #191919;\n"
"    color: white;\n"
"    border-radius: 30px;\n"
"    padding: 5px 20px;\n"
"}")
        self.backButton_2.setObjectName("backButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 230, 251, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Screenshot_5.png"))
        self.label.setObjectName("label")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(960, 800, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Newsreader")
        font.setPointSize(14)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(90, 530, 461, 161))
        font = QtGui.QFont()
        font.setFamily("Newsreader")
        font.setPointSize(20)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setStyleSheet("  border-radius: 40px;\n"
"")
        self.textBrowser_5.setObjectName("textBrowser_5")
        textWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(textWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        textWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(textWindow)
        self.statusbar.setObjectName("statusbar")
        textWindow.setStatusBar(self.statusbar)

        self.retranslateUi(textWindow)
        QtCore.QMetaObject.connectSlotsByName(textWindow)

    def retranslateUi(self, textWindow):
        _translate = QtCore.QCoreApplication.translate
        textWindow.setWindowTitle(_translate("textWindow", "Live Emotion Detection"))
        self.textBrowser.setHtml(_translate("textWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Newsreader\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600;\">Sentiment Analysis</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("textWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Newsreader\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Emotion Detecter</span></p></body></html>"))
        self.videoDetectorButton.setText(_translate("textWindow", "Video Detector"))
        self.whoWeAreButton.setText(_translate("textWindow", "Who we are"))
        self.backButton.setText(_translate("textWindow", "BACK"))
        self.backButton_2.setText(_translate("textWindow", "Submit"))
        self.textBrowser_5.setHtml(_translate("textWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Newsreader\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">What is on your mind?</p></body></html>"))
