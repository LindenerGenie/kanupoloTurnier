# Allow access to command-line arguments
import sys
 
# SIP allows us to select the API we wish to use
import sip
 
 
# Import all of Qt
from PyQt5.Qt import *
from PyQt5.QtSql import *

 
# Every Qt application must have one and only one QApplication object;
# it receives the command line arguments passed to the script, as they
# can be used to customize the application's appearance and behavior
qt_app = QApplication(sys.argv)

db = QSqlDatabase.addDatabase( "QSQLITE" )
db.setDatabaseName( ":memory:" ) 
db.open()

query = QSqlQuery()
query.exec( """CREATE TABLE spielklassen( id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, name VARCHAR NOT NULL ) """ )
 
# Run the application's event loop
qt_app.exec_()