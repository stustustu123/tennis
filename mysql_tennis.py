#!/usr/bin/env python

import MySQLdb as mdb

class MySQLObject(object):
	#global scoring_dbName, scoring_dbPass, scoring_dbUser
	def __init__(self, connection_info, scoring_dbUser, scoring_dbPass, scoring_dbName):
		import _mysql_exceptions
		self.con = mdb.connect(connection_info, scoring_dbUser, scoring_dbPass, scoring_dbName)
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
			cur.execute("INSERT INTO Players(FirstName, MiddleName, FamilyName, TickerName, DateOfBirth, Gender) \
				VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % addvalues)
			self.print_edit("Players")

	def get_players(self):
		try:
			a = ()
			cur = self.con.cursor()
			with self.con:
				cur.execute("SELECT FirstName FROM Players")
				for i in range(cur.rowcount):
					row = cur.fetchone()
					
					a = a + (row[0],)
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
