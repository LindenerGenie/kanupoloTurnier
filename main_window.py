from PyQt5.Qt import *

from spielklassen_view import *
from spielklassen_list import *
from database import *

class mainWindow_c( QMainWindow ):
	def __init__( self ):
		QMainWindow.__init__( self )
		self.db = database_c()
		self.slist = spielklassenList_c( self.db.db )
		self.spielklassenView = spielklassenView_c( self.slist )
		self.setCentralWidget( self.spielklassenView )