from PyQt5.Qt import *
from PyQt5.QtSql import *

class spielklassenList_c :

	def __init__( self ):
		self.model = QSqlTableModel( self )
		self.model.setTable( "spielklassen" )
		