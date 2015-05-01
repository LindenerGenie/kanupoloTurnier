# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mannschaften_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mannschaftenDialog_c(object):
    def setupUi(self, mannschaftenDialog_c):
        mannschaftenDialog_c.setObjectName("mannschaftenDialog_c")
        mannschaftenDialog_c.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(mannschaftenDialog_c)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(mannschaftenDialog_c)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.listView_2 = QtWidgets.QListView(mannschaftenDialog_c)
        self.listView_2.setObjectName("listView_2")
        self.horizontalLayout.addWidget(self.listView_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(mannschaftenDialog_c)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(mannschaftenDialog_c)
        self.buttonBox.accepted.connect(mannschaftenDialog_c.accept)
        self.buttonBox.rejected.connect(mannschaftenDialog_c.reject)
        QtCore.QMetaObject.connectSlotsByName(mannschaftenDialog_c)

    def retranslateUi(self, mannschaftenDialog_c):
        _translate = QtCore.QCoreApplication.translate
        mannschaftenDialog_c.setWindowTitle(_translate("mannschaftenDialog_c", "Mannschaften"))

