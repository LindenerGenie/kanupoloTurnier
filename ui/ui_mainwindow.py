# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow_c(object):
    def setupUi(self, mainWindow_c):
        mainWindow_c.setObjectName("mainWindow_c")
        mainWindow_c.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow_c)
        self.centralwidget.setObjectName("centralwidget")
        mainWindow_c.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow_c)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        self.menuDaten = QtWidgets.QMenu(self.menubar)
        self.menuDaten.setObjectName("menuDaten")
        mainWindow_c.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow_c)
        self.statusbar.setObjectName("statusbar")
        mainWindow_c.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(mainWindow_c)
        self.toolBar.setObjectName("toolBar")
        mainWindow_c.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNeu = QtWidgets.QAction(mainWindow_c)
        self.actionNeu.setObjectName("actionNeu")
        self.actionLaden = QtWidgets.QAction(mainWindow_c)
        self.actionLaden.setObjectName("actionLaden")
        self.actionSpeichern = QtWidgets.QAction(mainWindow_c)
        self.actionSpeichern.setObjectName("actionSpeichern")
        self.actionSpielklassen = QtWidgets.QAction(mainWindow_c)
        self.actionSpielklassen.setObjectName("actionSpielklassen")
        self.actionMannschaften = QtWidgets.QAction(mainWindow_c)
        self.actionMannschaften.setObjectName("actionMannschaften")
        self.menuDatei.addAction(self.actionNeu)
        self.menuDatei.addAction(self.actionLaden)
        self.menuDatei.addAction(self.actionSpeichern)
        self.menuDaten.addAction(self.actionSpielklassen)
        self.menuDaten.addAction(self.actionMannschaften)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuDaten.menuAction())

        self.retranslateUi(mainWindow_c)
        QtCore.QMetaObject.connectSlotsByName(mainWindow_c)

    def retranslateUi(self, mainWindow_c):
        _translate = QtCore.QCoreApplication.translate
        mainWindow_c.setWindowTitle(_translate("mainWindow_c", "Turnier Planer"))
        self.menuDatei.setTitle(_translate("mainWindow_c", "Datei"))
        self.menuDaten.setTitle(_translate("mainWindow_c", "Daten"))
        self.toolBar.setWindowTitle(_translate("mainWindow_c", "toolBar"))
        self.actionNeu.setText(_translate("mainWindow_c", "Neu"))
        self.actionLaden.setText(_translate("mainWindow_c", "Laden"))
        self.actionSpeichern.setText(_translate("mainWindow_c", "Speichern"))
        self.actionSpielklassen.setText(_translate("mainWindow_c", "Spielklassen"))
        self.actionMannschaften.setText(_translate("mainWindow_c", "Mannschaften"))

