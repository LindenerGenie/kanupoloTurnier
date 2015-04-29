from PyQt5.QtSql import *

class database_c :
	def __init__( self ) :
		self.db = QSqlDatabase.addDatabase( "QSQLITE" )
		self.db.setDatabaseName( ":memory:" ) 
		self.db.open()

	def init():
		query = QSqlQuery()
		query.exec( """CREATE TABLE spielklassen( id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, name VARCHAR NOT NULL ) """ )

