# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tennis_test.ui'
#
# Created: Mon Oct 20 22:33:44 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(501, 144)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_p1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_p1.setGeometry(QtCore.QRect(380, -2, 85, 41))
        self.pushButton_p1.setObjectName(_fromUtf8("pushButton_p1"))
        self.pushButton_p2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_p2.setGeometry(QtCore.QRect(380, 47, 85, 41))
        self.pushButton_p2.setObjectName(_fromUtf8("pushButton_p2"))
        self.checkBox_p1 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_p1.setGeometry(QtCore.QRect(340, 8, 21, 21))
        self.checkBox_p1.setText(_fromUtf8(""))
        self.checkBox_p1.setObjectName(_fromUtf8("checkBox_p1"))
        self.checkBox_p2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_p2.setGeometry(QtCore.QRect(340, 57, 21, 21))
        self.checkBox_p2.setText(_fromUtf8(""))
        self.checkBox_p2.setObjectName(_fromUtf8("checkBox_p2"))
        self.lineEdit_1_P1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_1_P1.setGeometry(QtCore.QRect(10, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_1_P1.setFont(font)
        self.lineEdit_1_P1.setObjectName(_fromUtf8("lineEdit_1_P1"))
        self.lineEdit_1_P2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_1_P2.setGeometry(QtCore.QRect(10, 50, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_1_P2.setFont(font)
        self.lineEdit_1_P2.setObjectName(_fromUtf8("lineEdit_1_P2"))
        self.lineEdit_2_P2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2_P2.setGeometry(QtCore.QRect(50, 50, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_2_P2.setFont(font)
        self.lineEdit_2_P2.setObjectName(_fromUtf8("lineEdit_2_P2"))
        self.lineEdit_2_P1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2_P1.setGeometry(QtCore.QRect(50, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_2_P1.setFont(font)
        self.lineEdit_2_P1.setObjectName(_fromUtf8("lineEdit_2_P1"))
        self.lineEdit_3_P2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3_P2.setGeometry(QtCore.QRect(90, 50, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_3_P2.setFont(font)
        self.lineEdit_3_P2.setObjectName(_fromUtf8("lineEdit_3_P2"))
        self.lineEdit_3_P1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3_P1.setGeometry(QtCore.QRect(90, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_3_P1.setFont(font)
        self.lineEdit_3_P1.setObjectName(_fromUtf8("lineEdit_3_P1"))
        self.lineEdit_4_P2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4_P2.setGeometry(QtCore.QRect(130, 50, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_4_P2.setFont(font)
        self.lineEdit_4_P2.setObjectName(_fromUtf8("lineEdit_4_P2"))
        self.lineEdit_4_P1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4_P1.setGeometry(QtCore.QRect(130, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_4_P1.setFont(font)
        self.lineEdit_4_P1.setObjectName(_fromUtf8("lineEdit_4_P1"))
        self.lineEdit_5_P2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5_P2.setGeometry(QtCore.QRect(170, 50, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_5_P2.setFont(font)
        self.lineEdit_5_P2.setObjectName(_fromUtf8("lineEdit_5_P2"))
        self.lineEdit_5_P1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5_P1.setGeometry(QtCore.QRect(170, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_5_P1.setFont(font)
        self.lineEdit_5_P1.setObjectName(_fromUtf8("lineEdit_5_P1"))
        self.lineEdit_Sets_P2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Sets_P2.setGeometry(QtCore.QRect(230, 50, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_Sets_P2.setFont(font)
        self.lineEdit_Sets_P2.setObjectName(_fromUtf8("lineEdit_Sets_P2"))
        self.lineEdit_Sets_P1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Sets_P1.setGeometry(QtCore.QRect(230, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_Sets_P1.setFont(font)
        self.lineEdit_Sets_P1.setObjectName(_fromUtf8("lineEdit_Sets_P1"))
        self.lineEdit_Game_P2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Game_P2.setGeometry(QtCore.QRect(290, 50, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_Game_P2.setFont(font)
        self.lineEdit_Game_P2.setObjectName(_fromUtf8("lineEdit_Game_P2"))
        self.lineEdit_Game_P1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Game_P1.setGeometry(QtCore.QRect(290, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_Game_P1.setFont(font)
        self.lineEdit_Game_P1.setObjectName(_fromUtf8("lineEdit_Game_P1"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 501, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_p1.setText(_translate("MainWindow", "P1 point", None))
        self.pushButton_p2.setText(_translate("MainWindow", "P2 point", None))

