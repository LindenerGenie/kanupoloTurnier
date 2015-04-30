from PyQt5.Qt import *
from PyQt5.QtSql import *

class spielklassenList_c( QSqlTableModel ) :

	def __init__( self, db ):
		QSqlTableModel.__init__( self, None, db )
		self.setTable( "spielklassen" )
		
