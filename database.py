from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *

class database_c :
	def __init__( self ) :
		self.db = QSqlDatabase.addDatabase( "QSQLITE" )
		self.db.setDatabaseName( "turnier" ) 
		self.db.open()

	def init( self ) :
		query = QSqlQuery( self.db )
		query.exec_( """CREATE TABLE spielklassen( id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, name VARCHAR NOT NULL ) """ )
		query2 = QSqlQuery( self.db )
		query2.prepare( """INSERT INTO spielklassen (id, name) VALUES (:id, :name ) """ )
		query2.bindValue( ":id", QVariant( 1 ) )
		query2.bindValue( ":name", QVariant( "Schüler" ) )
		query2.exec_()


