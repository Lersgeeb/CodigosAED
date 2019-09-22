# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'embeddedimageGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImageWindow(object):
    def setupUi(self, ImageWindow):
        ImageWindow.setObjectName("Mapa (Grafo)")
        ImageWindow.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImageWindow.sizePolicy().hasHeightForWidth())
        ImageWindow.setSizePolicy(sizePolicy)
        ImageWindow.setMinimumSize(QtCore.QSize(640, 480))
        ImageWindow.setMaximumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(ImageWindow)
        self.centralwidget.setObjectName("centralwidget")
        ImageWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ImageWindow)
        QtCore.QMetaObject.connectSlotsByName(ImageWindow)

    def retranslateUi(self, ImageWindow):
        _translate = QtCore.QCoreApplication.translate
        ImageWindow.setWindowTitle(_translate("Mapa (Grafo)", "Mapa (Grafo)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageWindow = QtWidgets.QMainWindow()
    ui = Ui_ImageWindow()
    ui.setupUi(ImageWindow)
    ImageWindow.show()
    sys.exit(app.exec_())
