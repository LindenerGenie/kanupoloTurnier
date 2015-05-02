# Allow access to command-line arguments
import sys
 
# SIP allows us to select the API we wish to use
import sip
 
from main_window import *

# Import all of Qt
from PyQt5.Qt import *
 
if __name__ == "__main__":
	# Every Qt application must have one and only one QApplication object;
	# it receives the command line arguments passed to the script, as they
	# can be used to customize the application's appearance and behavior
	qt_app = QApplication(sys.argv)

	db = database_c()
	db.init()
	slist = spielklassenList_c( db.db )
	mainwindow = mainWindow_c()
	spielklassenDialog = spielklassenDialog_c( slist, mainwindow )
	spielklassenDialog.exec_()


	# Run the application's event loop
	qt_app.exec_()