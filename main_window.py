from spielklassen_dialog import *

import sys

# Import all of Qt
from PyQt5.Qt import *

sys.path.append( "ui" )

import ui_mainwindow

class mainWindow_c( QMainWindow, ui_mainwindow.Ui_mainWindow_c  ):

	def __init__( self, parent = None ):
		super( mainWindow_c, self ).__init__( parent )
		self.setupUi( self )
