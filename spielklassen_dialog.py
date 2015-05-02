from spielklassen_list import *
from database import *

import sys

# Import all of Qt
from PyQt5.Qt import *

sys.path.append( "ui" )

import ui_spielklassen_dialog

class spielklassenDialog_c( ui_spielklassen_dialog.Ui_spielklassenDialog_c, QDialog ):

	def __init__( self, spielklassenList, parent = None ):
		super( spielklassenDialog_c, self ).__init__( parent )
		self.setupUi( self )

		self.spielklassenList = spielklassenList
		self.spielklassenListView.setModel( self.spielklassenList )
		self.spielklassenListView.setItemDelegate( QSqlRelationalDelegate( self) )
