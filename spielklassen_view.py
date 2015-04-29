from spielklassen_list import *
from database import *

# Import all of Qt
from PyQt5.Qt import *


class spielklassenView_c( QTableView ):

	def __init__( self, spielklassenList ):
		QTableView.__init__( self )
		self.spielklassenList = spielklassenList
		self.setModel( self.spielklassenList )
