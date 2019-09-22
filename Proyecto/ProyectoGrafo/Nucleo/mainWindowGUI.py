# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ventana Principal (main.py)")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.editor = QtWidgets.QTextEdit(self.centralwidget)
        self.editor.setGeometry(QtCore.QRect(40, 70, 491, 511))
        self.editor.setObjectName("editor")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 50, 131, 17))
        self.label.setObjectName("label")
        self.initialServer = QtWidgets.QLineEdit(self.centralwidget)
        self.initialServer.setGeometry(QtCore.QRect(620, 120, 113, 25))
        self.initialServer.setObjectName("initialServer")
        self.finalServer = QtWidgets.QLineEdit(self.centralwidget)
        self.finalServer.setGeometry(QtCore.QRect(620, 200, 113, 25))
        self.finalServer.setObjectName("finalServer")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 100, 91, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 180, 81, 17))
        self.label_3.setObjectName("label_3")
        self.openFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFileButton.setGeometry(QtCore.QRect(620, 320, 89, 25))
        self.openFileButton.setObjectName("openFileButton")
        self.makeGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.makeGraphButton.setGeometry(QtCore.QRect(620, 380, 89, 25))
        self.makeGraphButton.setObjectName("makeGraphButton")
        self.makeTableButton = QtWidgets.QPushButton(self.centralwidget)
        self.makeTableButton.setGeometry(QtCore.QRect(620, 440, 89, 25))
        self.makeTableButton.setObjectName("makeTableButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Ventana Principal (main.py)", "Ventana Principal (main.py)"))
        self.label.setText(_translate("MainWindow", "Network structure"))
        self.label_2.setText(_translate("MainWindow", "Initial Server"))
        self.label_3.setText(_translate("MainWindow", "Final Server"))
        self.openFileButton.setText(_translate("MainWindow", "Open File"))
        self.makeGraphButton.setText(_translate("MainWindow", "Make Graph"))
        self.makeTableButton.setText(_translate("MainWindow", "Make Table"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
