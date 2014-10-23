#!/usr/bin/env python

import sys
import string
import os
from PyQt4 import QtCore, QtGui

from Ui_tennis_test import Ui_MainWindow

import test_class as score

a=score.tennis_score("Female")
a.p1_name="Bob"
a.p2_name="Albert"

class TestForm(QtGui.QMainWindow):   
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.update_scores()

        self.ui.pushButton_p1.clicked.connect(self.pushButton_p1)
        self.ui.pushButton_p2.clicked.connect(self.pushButton_p2)
	
    def pushButton_p1(self):
        a.point_scored(0)
        self.update_scores()

    def pushButton_p2(self):
        a.point_scored(1)
        self.update_scores()
        
    def update_scores(self):
        self.ui.lineEdit_1_P1.setText(str(a.p1_set_points[0]))
        self.ui.lineEdit_2_P1.setText(str(a.p1_set_points[1]))
        self.ui.lineEdit_3_P1.setText(str(a.p1_set_points[2]))
        self.ui.lineEdit_4_P1.setText(str(a.p1_set_points[3]))
        self.ui.lineEdit_5_P1.setText(str(a.p1_set_points[4]))
        self.ui.lineEdit_1_P2.setText(str(a.p2_set_points[0]))
        self.ui.lineEdit_2_P2.setText(str(a.p2_set_points[1]))
        self.ui.lineEdit_3_P2.setText(str(a.p2_set_points[2]))
        self.ui.lineEdit_4_P2.setText(str(a.p2_set_points[3]))
        self.ui.lineEdit_5_P2.setText(str(a.p2_set_points[4]))
        if a.tie_breaker==False:
	    self.ui.lineEdit_Game_P1.setText(str(a.game[a.p1_game_points]))
	    self.ui.lineEdit_Game_P2.setText(str(a.game[a.p2_game_points]))
	else:
	    self.ui.lineEdit_Game_P1.setText(str(a.p1_game_points))
	    self.ui.lineEdit_Game_P2.setText(str(a.p2_game_points))
	    
        self.ui.lineEdit_Sets_P1.setText(str(a.p1_set_tally))
        self.ui.lineEdit_Sets_P2.setText(str(a.p2_set_tally))
        b = (a.current_set)
        if b==0:
            self.ui.radioButton_set1.setChecked(1)
        elif b==1:
            self.ui.radioButton_set2.setChecked(2)
        elif b==2:
            self.ui.radioButton_set3.setChecked(2)
        elif b==3:
            self.ui.radioButton_set4.setChecked(2)
        else:
            self.ui.radioButton_set5.setChecked(2)
        
        
	
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    testform = TestForm()
    
    #app.processEvents()
    testform.show()
    sys.exit(app.exec_())