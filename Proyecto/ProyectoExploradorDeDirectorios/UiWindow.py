# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Copy2to1 = QtWidgets.QPushButton(self.centralwidget)
        self.Copy2to1.setGeometry(QtCore.QRect(360, 210, 81, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("copyIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Copy2to1.setIcon(icon)
        self.Copy2to1.setObjectName("Copy2to1")
        self.Copy1to2 = QtWidgets.QPushButton(self.centralwidget)
        self.Copy1to2.setGeometry(QtCore.QRect(360, 260, 81, 31))
        self.Copy1to2.setIcon(icon)
        self.Copy1to2.setObjectName("Copy1to2")
        self.CreateDir1 = QtWidgets.QPushButton(self.centralwidget)
        self.CreateDir1.setGeometry(QtCore.QRect(10, 490, 101, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("folderIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CreateDir1.setIcon(icon1)
        self.CreateDir1.setObjectName("CreateDir1")
        self.Explorer2 = QtWidgets.QListWidget(self.centralwidget)
        self.Explorer2.setGeometry(QtCore.QRect(450, 10, 341, 471))
        self.Explorer2.setObjectName("Explorer2")
        self.Explorer2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Explorer1 = QtWidgets.QListWidget(self.centralwidget)
        self.Explorer1.setGeometry(QtCore.QRect(10, 10, 341, 471))
        self.Explorer1.setObjectName("Explorer1")
        self.CreateAr1 = QtWidgets.QPushButton(self.centralwidget)
        self.CreateAr1.setGeometry(QtCore.QRect(130, 490, 101, 61))
        self.Explorer1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("archiveIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CreateAr1.setIcon(icon2)
        self.CreateAr1.setObjectName("CreateAr1")
        self.Remove1 = QtWidgets.QPushButton(self.centralwidget)
        self.Remove1.setGeometry(QtCore.QRect(250, 490, 101, 61))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("trashIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Remove1.setIcon(icon3)
        self.Remove1.setObjectName("Remove1")
        self.CreateAr2 = QtWidgets.QPushButton(self.centralwidget)
        self.CreateAr2.setGeometry(QtCore.QRect(570, 490, 101, 61))
        self.CreateAr2.setIcon(icon2)
        self.CreateAr2.setObjectName("CreateAr2")
        self.Remove2 = QtWidgets.QPushButton(self.centralwidget)
        self.Remove2.setGeometry(QtCore.QRect(690, 490, 101, 61))
        self.Remove2.setIcon(icon3)
        self.Remove2.setObjectName("Remove2")
        self.CreateDir2 = QtWidgets.QPushButton(self.centralwidget)
        self.CreateDir2.setGeometry(QtCore.QRect(450, 490, 101, 61))
        self.CreateDir2.setIcon(icon1)
        self.CreateDir2.setObjectName("CreateDir2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Copy2to1.setText(_translate("MainWindow", "<--"))
        self.Copy1to2.setText(_translate("MainWindow", "-->"))
        self.CreateDir1.setText(_translate("MainWindow", "Crear Carpeta"))
        self.CreateAr1.setText(_translate("MainWindow", "Crear Archivo"))
        self.Remove1.setText(_translate("MainWindow", "Remover"))
        self.CreateAr2.setText(_translate("MainWindow", "Crear Archivo"))
        self.Remove2.setText(_translate("MainWindow", "Remover"))
        self.CreateDir2.setText(_translate("MainWindow", "Crear Carpeta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

