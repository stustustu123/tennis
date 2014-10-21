#!/usr/bin/env python

import string
import os
from PyQt4 import QtCore, QtGui

from Ui_tennis_test import Ui_MainWindow

class TestForm(QtGui.QMainWindow):   
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

	self.ui.pushButton_p1.clicked.connect(self.pushButton_p1)
	
    def pushButton_p1(self):
	return


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    testform = TestForm()
    app.processEvents()
    tesform.show()
    sys.exit(app.exec_())