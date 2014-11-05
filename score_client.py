#!/usr/bin/env python

# Attempt to create a Tennis scoring client for on-court scoring

import sys
import string
import socket
import time
import os
import MySQLdb as mdb
import cPickle as pickle

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import exc

#engine = create_engine('mysql://stuart:pataks99@localhost')


from PyQt4 import QtCore,  QtGui

from Ui_scoring_client import Ui_MainWindow
from Ui_player_create import Ui_PlayerCreateWindow
from Ui_match_create import Ui_MatchCreateWindow
from Ui_load_match import Ui_LoadMatchWindow

#from calc_score import tennis_score

scoring_dbName = 'tennis'
scoring_dbUser = 'stuart'
scoring_dbPass = 'pataks99'

settings_file = 'config.p'
log_file = 'score_client.log'

class ScoringForm(QtGui.QMainWindow):   
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#self.status_bar = (QtGui.QLabel(""),1)
		self.status_bar = QtGui.QLabel("")      # Re-work status bar so text doesn't disappear
		self.status_bar.setObjectName("status") # Re-work status bar so text doesn't disappear
		self.ui.statusbar.addPermanentWidget(self.status_bar)
		self.set_buttons_state(0)
		self.set_db_menus(False)
		
		self.ui.pushButton_CONNECT_DB.clicked.connect(self.pushButton_connect_db)
		#self.ui.pushButton_CONNECT_DB.clicked.connect(SQLAlchObject)
		self.ui.pushButton_TEST_DB.clicked.connect(self.pushButton_test_db)
		self.ui.pushButton_SELXMLFILE.clicked.connect(self.pushButton_sel_xml_file)
		self.ui.pushButton_SAVE_CONFIG.clicked.connect(self.pushButton_save_config)
		self.ui.actionExit.triggered.connect(self.closeEvent)
		self.ui.actionNew_Player.triggered.connect(self.menu_playercreate)
		self.ui.actionNew_Match.triggered.connect(self.menu_matchcreate)
		self.ui.actionLoad_Match.triggered.connect(self.menu_loadmatch)
		
		
	def closeEvent(self, event):
		log_message('User exited application')
		sys.exit()
		
	def menu_playercreate(self):
		#playercreate = PlayerCreate()
		playercreate.show_window()

	def menu_loadmatch(self):
		#playercreate = PlayerCreate()
		loadmatch.show_window()

	def menu_matchcreate(self):
		a=SQLAlchObject(str(scoringform.ui.LineEdit_DATABASE_SERVER.text()), scoring_dbUser, scoring_dbPass, scoring_dbName)
		players=a.get_players()
		if players != 0:
			matchcreate.ui.comboBox_PlayerA.clear()
			for item in players:
				matchcreate.ui.comboBox_PlayerA.addItem(str(item))
				matchcreate.ui.comboBox_PlayerB.addItem(str(item))
			matchcreate.show_window()

	def set_buttons_state(self, state):
		if state == 0:
			self.ui.frame_P1_BUTTONS.hide()
			self.ui.frame_P2_BUTTONS.hide()
		else:
			self.ui.frame_P1_BUTTONS.show()
			self.ui.frame_P2_BUTTONS.show()
		#self.ui.checkBox_P1_SERVICE.setEnabled(False)
		
	def pushButton_save_config(self):
		global settings_file
		config = {"db_host":(self.ui.LineEdit_DATABASE_SERVER.text())}
		try:
			pickle.dump (config, open (settings_file, "wb"))
			log_message('Config saved.')
		except (pickle.PicklingError, IOError) as error:
			log_message('Error writing config file! Error: %s' % (msg[1]))
					
	def pushButton_connect_db(self):
		global scoring_dbName, scoring_dbPass, scoring_dbUser
		try:
			con = mdb.connect(str(self.ui.LineEdit_DATABASE_SERVER.text()), scoring_dbUser, scoring_dbPass, scoring_dbName)
			log_message('Connected to DB %s on %s' % (scoring_dbName, str(self.ui.LineEdit_DATABASE_SERVER.text())))
			self.indicate_connected(1, str(self.ui.LineEdit_DATABASE_SERVER.text()))
			self.set_db_menus(True)
		except (mdb.Error) as error:
			log_message('DB connection error: %s' % error)
			self.indicate_connected(0, str(self.ui.LineEdit_DATABASE_SERVER.text()))
			self.set_db_menus(False)
			reply = QtGui.QMessageBox.critical(self, 'Warning', ("Error connecting to DB: \n %s " % error), QtGui.QMessageBox.Ok)
			
	def indicate_connected (self,  enabled, db_host):
		# changes 'connect' button colour & disable / reenable the buttons
		palette = QtGui.QPalette()
		if enabled:
			brush = QtGui.QBrush(QtGui.QColor(0, 192, 0))
			#self.ui.statusbar.status.setText("Connected to Database : %s  " % (db_host))
			self.status_bar.setText("Connected to Database : %s  " % (db_host))
		else:
			brush = QtGui.QBrush(QtGui.QColor(192, 0, 0))
			self.status_bar.setText("Disconnected")
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
		self.ui.pushButton_CONNECT_DB.setPalette(palette)
		#self.enable_buttons(enabled)
		
	def set_db_menus(self, state):
		# Disables relevant menus when DB is not connected
		self.ui.actionNew_Match.setEnabled(state)
		self.ui.actionLoad_Match.setEnabled(state)
		self.ui.menuPlayers.setEnabled(state)


	def pushButton_test_db(self):
		global scoring_dbName, scoring_dbPass, scoring_dbUser
		a=SQLAlchObject(str(scoringform.ui.LineEdit_DATABASE_SERVER.text()), scoring_dbUser, scoring_dbPass, scoring_dbName)
		db_test = a.test_db_connection()
		if db_test > 0:
			log_message('DB connection error: %s' % db_test)
			popup_message('Warning', ("Error connecting to DB: \n %s " % db_test))
		else:
			log_message('User tested connection to DB. Result = OK')
			popup_message('Success', "User tested connection to DB. Result = OK")
			
		#try:
			#engine = create_engine('mysql://' + scoring_dbUser + ':' + scoring_dbPass + '@' + (str(self.ui.LineEdit_DATABASE_SERVER.text())))
			#engine.execute("CREATE DATABASE IF NOT EXISTS " + scoring_dbName)
			#engine.execute("Use " + scoring_dbName)
			##con = mdb.connect(str(self.ui.LineEdit_DATABASE_SERVER.text()), scoring_dbUser, scoring_dbPass, scoring_dbName)
			#log_message('User tested connection to DB. Result = OK')
			#popup_message('Success', "User tested connection to DB. Result = OK")
			##reply = QtGui.QMessageBox.information(self, 'Success', "User tested connection to DB. Result = OK", QtGui.QMessageBox.Ok)
			##con.close()
		#except (mdb.Error) as error:
			#log_message('DB connection error: %s' % error)
			#popup_message('Warning', ("Error connecting to DB: \n %s " % error))
			#reply = QtGui.QMessageBox.critical(self, 'Warning', ("Error connecting to DB: \n %s " % error), QtGui.QMessageBox.Ok)
			

	def pushButton_sel_xml_file(self):
		xmlfilename = self.fileDialog = QtGui.QFileDialog.getOpenFileName(self, 'Select XML File', (os.getcwd()))
		#self.fileDialog.show()
		if (len(xmlfilename))>0:
			#self.log_message('Select Bug file: %s' % xmlfilename)
			self.ui.LineEdit_XML_Output_File.setText(xmlfilename)
			
class PlayerCreate(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_PlayerCreateWindow()
		#self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.ui.setupUi(self)
		self.ui.pushButton_DELETE_ALL_PLAYERS.clicked.connect(self.delete_all_players)
		self.ui.pushButton_EXIT.clicked.connect(self.button_close)
		self.ui.pushButton_SAVE_EXIT.clicked.connect(self.button_save_close)
		#self.show_window()
		
	def show_window(self):
		self.show()
	
	def closeEvent(self, event):
		#detects when user hits X to close script editor window!
		self.button_close()
		
	def button_close(self):
		self.close()
		#self.deleteLater()

	def button_save_close(self):
		a=SQLAlchObject(str(scoringform.ui.LineEdit_DATABASE_SERVER.text()), scoring_dbUser, scoring_dbPass, scoring_dbName)
		a.add_player((str(playercreate.ui.LineEdit_firstname.text())), (str(playercreate.ui.LineEdit_middlename.text())), \
			(str(playercreate.ui.LineEdit_familyname.text())), (str(playercreate.ui.LineEdit_tickername.text())), \
			(str(playercreate.ui.DateEdit_dateofbirth.date().toPyDate())), (str(playercreate.ui.comboBox_gender.currentText())))
		self.close()
		#self.deleteLater()
		
	def delete_all_players(self):
		a=SQLAlchObject(str(scoringform.ui.LineEdit_DATABASE_SERVER.text()), scoring_dbUser, scoring_dbPass, scoring_dbName)
		a.delete_all_players()
		self.close()
				
class MatchCreate(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MatchCreateWindow()
		#self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.ui.setupUi(self)
		self.ui.pushButton_DELETE_ALL_MATCHES.clicked.connect(self.delete_all_matches)
		self.ui.pushButton_EXIT.clicked.connect(self.button_close)
		self.ui.pushButton_SAVE_EXIT.clicked.connect(self.button_save_close)
		#self.show_window()
		
	def show_window(self):
		self.show()
	
	def closeEvent(self, event):
		#detects when user hits X to close script editor window!
		self.button_close()
		
	def button_close(self):
		self.close()
		#self.deleteLater()

	def button_save_close(self):
		a=SQLAlchObject(str(scoringform.ui.LineEdit_DATABASE_SERVER.text()), scoring_dbUser, scoring_dbPass, scoring_dbName)
		a.add_match(str(matchcreate.ui.comboBox_PlayerA.currentText()), str(matchcreate.ui.comboBox_PlayerB.currentText()))
		self.close()
		#self.deleteLater()
		
	def delete_all_players(self):
		a=SQLAlchObject(str(scoringform.ui.LineEdit_DATABASE_SERVER.text()), scoring_dbUser, scoring_dbPass, scoring_dbName)
		a.delete_all_players()
		self.close()
		
	def delete_all_matches(self):
		a=SQLAlchObject(str(scoringform.ui.LineEdit_DATABASE_SERVER.text()), scoring_dbUser, scoring_dbPass, scoring_dbName)
		a.delete_all_matches()
		self.close()

class LoadMatch(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_LoadMatchWindow()
		#self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.ui.setupUi(self)
		self.ui.pushButton_EXIT.clicked.connect(self.button_close)
		self.ui.pushButton_SAVE_EXIT.clicked.connect(self.button_save_close)
		
	def show_window(self):
		self.show()
	
	def closeEvent(self, event):
		#detects when user hits X to close script editor window!
		self.button_close()
		
	def button_close(self):
		self.close()
		#self.deleteLater()

	def button_save_close(self):
		#a=SQLAlchObject(str(scoringform.ui.LineEdit_DATABASE_SERVER.text()), scoring_dbUser, scoring_dbPass, scoring_dbName)
		#a.add_match(str(matchcreate.ui.comboBox_PlayerA.currentText()), str(matchcreate.ui.comboBox_PlayerB.currentText()))
		self.close()
		#self.deleteLater()

class SQLAlchObject(object):
	#global scoring_dbName, scoring_dbPass, scoring_dbUser
	def __init__(self, connection_info, scoring_dbUser, scoring_dbPass, scoring_dbName):
		#import _mysql_exceptions
		#self.con = mdb.connect(connection_info, scoring_dbUser, scoring_dbPass, scoring_dbName)
		engine = create_engine('mysql://' + scoring_dbUser + ':' + scoring_dbPass + '@' + (str(scoringform.ui.LineEdit_DATABASE_SERVER.text())))
		#engine.execute("CREATE DATABASE IF NOT EXISTS " + scoring_dbName)
		#engine.execute("Use " + scoring_dbName)

		#log_message('SQLAlchObject __init__ worked')
		#connect_db(scoring_dbName, scoring_dbUser)
		return

	def test_db_connection(self):
		try:
			engine = create_engine('mysql://' + scoring_dbUser + ':' + scoring_dbPass + '@' + (str(scoringform.ui.LineEdit_DATABASE_SERVER.text())))
			engine.execute("Use " + scoring_dbName)
		except exc.SQLAlchemyError as e:
			return e
	
	def add_player(self, *addvalues):
		#try:
		cur = self.con.cursor()
		with self.con:
			cur.execute("CREATE TABLE IF NOT EXISTS Players(Id INT PRIMARY KEY AUTO_INCREMENT, FirstName VARCHAR(50), MiddleName VARCHAR(50), \
				FamilyName VARCHAR(50), TickerName VARCHAR(30), DateOfBirth VARCHAR(20), Gender VARCHAR(10))")
			#cur.execute("INSERT INTO Players(FirstName) VALUES('%s')" % addvalues)
			cur.execute("INSERT INTO Players(FirstName, MiddleName, FamilyName, TickerName, DateOfBirth, Gender) \
				VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % addvalues)
			#log_message ('Inserted record')
			self.print_edit("Players")
			#return

	def get_players(self):
		try:
			a = ()
			cur = self.con.cursor()
			with self.con:
				cur.execute("SELECT FirstName FROM Players")
				for i in range(cur.rowcount):
					row = cur.fetchone()
					
					a = a + (row[0],)
		# for row in rows:
				log_message(a)
				return a
		except mdb.Error as e:
			log_message ("Error getting players: %s" % e[1])
			popup_message('Warning', "Error getting players: \n%s" % e[1])
			return 0
	
	def add_match(self, playerA, playerB):
		log_message(playerA + "  " + playerB)
		cur = self.con.cursor()
		with self.con:
			cur.execute("CREATE TABLE IF NOT EXISTS Matches(Id INT PRIMARY KEY AUTO_INCREMENT, playerA VARCHAR(25), playerB VARCHAR(25))")
			cur.execute("INSERT INTO Matches(playerA, playerB) VALUES (%s, %s)", [(playerA), (playerB)])
			self.print_edit("Matches")
			#return

	def delete_all_players(self):
		cur = self.con.cursor()
		#with self.con:
		cur.execute("DROP TABLE IF EXISTS Players")
		log_message("Emptied PLAYERS table")
		
	def delete_all_matches(self):
		cur = self.con.cursor()
		#with self.con:
		cur.execute("DROP TABLE IF EXISTS Matches")
		log_message("Emptied PLAYERS table")

	def print_edit(self, table):
		with self.con: 
			cur = self.con.cursor()
			cur.execute("SELECT * FROM %s" % (str(table)))

			for i in range(cur.rowcount):
				row = cur.fetchone()
				a = len(row)
				
				#log_message ('Database contains: %s and %s' % (row[0], row[1]))
				log_message ('Database contains: %s' % (str(row[0:a])))

def read_config(settings_file):
	# read the settings data & assign values to our forms.
	try:
		config = pickle.load (open(settings_file))
		scoringform.ui.LineEdit_DATABASE_SERVER.setText(config["db_host"])
		#boxesform.ui.lineEditCGIP.setText(cg_config["host"])
		#boxesform.ui.spinBoxPORT.setValue(int (cg_config["port"]))
	except (pickle.UnpicklingError, IOError) as error:
		log_message('Error reading config file. Settings not loaded.')


		
def log_message(log_msg):
	global log_file
	# Append logging messages to our log window.
	message = scoringform.ui.plainTextEdit_log
	log_time = str(time.strftime("%x - %H:%M:%S"))
	message.appendPlainText('%s  -->  %s' % (log_time, log_msg))
	print ('%s --> %s' % (log_time, log_msg))
	with open(log_file, "a") as log:
		log.write('%s --> %s\n' % (log_time, log_msg))
		
def popup_message(status, popup_message):
	reply = QtGui.QMessageBox.information(scoringform, status, popup_message, QtGui.QMessageBox.Ok)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	scoringform = ScoringForm()
	playercreate = PlayerCreate()
	matchcreate = MatchCreate()
	loadmatch = LoadMatch()

	# Create and display the splash screen
	splash_pix = QtGui.QPixmap('aus open tennis ball.png')
	splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
	splash.setMask(splash_pix.mask())
	log_message('Application started')
	#splash.show()
	read_config(settings_file)
	#time.sleep(2)
	scoringform.ui.tabWidget.setCurrentIndex(0)
	app.processEvents()
	scoringform.show()
	sys.exit(app.exec_())
	
#reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
#reply = QtGui.QMessageBox.information(self, 'Message', "Press ok", QtGui.QMessageBox.Ok)
