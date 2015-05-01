# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spielklassen_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_spielklassenDialog_c(object):
    def setupUi(self, spielklassenDialog_c):
        spielklassenDialog_c.setObjectName("spielklassenDialog_c")
        spielklassenDialog_c.resize(532, 417)
        self.verticalLayout = QtWidgets.QVBoxLayout(spielklassenDialog_c)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spielklassenListView_c = QtWidgets.QListView(spielklassenDialog_c)
        self.spielklassenListView_c.setObjectName("spielklassenListView_c")
        self.verticalLayout.addWidget(self.spielklassenListView_c)
        self.buttonBox = QtWidgets.QDialogButtonBox(spielklassenDialog_c)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(spielklassenDialog_c)
        self.buttonBox.accepted.connect(spielklassenDialog_c.accept)
        self.buttonBox.rejected.connect(spielklassenDialog_c.reject)
        QtCore.QMetaObject.connectSlotsByName(spielklassenDialog_c)

    def retranslateUi(self, spielklassenDialog_c):
        _translate = QtCore.QCoreApplication.translate
        spielklassenDialog_c.setWindowTitle(_translate("spielklassenDialog_c", "Spielklassen"))

