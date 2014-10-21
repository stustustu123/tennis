#!/usr/bin/env python

import sys
import string
import os
from PyQt4 import QtCore, QtGui

from Ui_tennis_test import Ui_MainWindow

import test_class as tennis_score

a=tennis_score.tennis_score("Male")
a.p1_name="Bob"
a.p2_name="Albert"

class TestForm(QtGui.QMainWindow):   
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_p1.clicked.connect(self.pushButton_p1)
        self.ui.pushButton_p2.clicked.connect(self.pushButton_p2)
	
    def pushButton_p1(self):
        a.point_scored(0)

    def pushButton_p2(self):
        a.point_scored(1)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    testform = TestForm()
    
    #app.processEvents()
    testform.show()
    sys.exit(app.exec_())