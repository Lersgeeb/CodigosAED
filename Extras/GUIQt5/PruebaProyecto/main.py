from UiWindow import *

class MainWindowUser(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #--------------------------------------
        #self.Explorer1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        
       
        self.Explorer1.itemDoubleClicked.connect(self.qShowDialog1)
        self.CreateDir1.clicked.connect(self.qAddDir1)
        self.CreateAr1.clicked.connect(self.qAddAr1)
        self.Remove1.clicked.connect(self.qRemove1)
        self.Explorer2.itemDoubleClicked.connect(self.qShowDialog2)
        self.CreateDir2.clicked.connect(self.qAddDir2)
        self.CreateAr2.clicked.connect(self.qAddAr2)
        self.Remove2.clicked.connect(self.qRemove2)
        self.Copy1to2.clicked.connect(self.qCopy1to2)
        self.Copy2to1.clicked.connect(self.qCopy2to1)
        
       

    def qShowDialog1(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("%s" % self.Explorer1.currentItem().text())
        
        msgBox.setWindowTitle("Contenido: ")
        
        msgBox.exec()

    def qShowDialog2(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("%s" % self.Explorer2.currentItem().text())
        
        msgBox.setWindowTitle("Contenido: ")
        
        msgBox.exec()
    
    def qGetName(self,dataType):
        text,okPressed = QtWidgets.QInputDialog.getText(self,"",("Nombre de su %s" % dataType), QtWidgets.QLineEdit.Normal, "")
        if(okPressed and text != ''):
            return text
        else:
            return False

    def qAddDir1(self):
        name = self.qGetName("carpeta")
        if(name):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("folderIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item = QtWidgets.QListWidgetItem(icon,name)
            self.Explorer1.addItem(item)
        else:
            pass   

    def qAddDir2(self):
        name = self.qGetName("carpeta")
        if(name):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("folderIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item = QtWidgets.QListWidgetItem(icon,name)
            self.Explorer2.addItem(item)
        else:
            pass   

    def qAddAr1(self):
        name = self.qGetName("archivo")
        if(name):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("archiveIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item = QtWidgets.QListWidgetItem(icon,name)
            self.Explorer1.addItem(item)
        else:
            pass    

    def qAddAr2(self):
        name = self.qGetName("archivo")
        if(name):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("archiveIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item = QtWidgets.QListWidgetItem(icon,name)
            self.Explorer2.addItem(item)
        else:
            pass    

    def qRemove1(self):
        listItems=self.Explorer1.selectedItems()
        if not listItems: return        
        for item in listItems:
            self.Explorer1.takeItem(self.Explorer1.row(item))

    def qRemove2(self):
        listItems=self.Explorer2.selectedItems()
        if not listItems: return        
        for item in listItems:
            self.Explorer2.takeItem(self.Explorer2.row(item))

    def qCopy1to2(self):
        item = self.Explorer1.currentItem()
        if (not item): return False 
        item2 = item.clone()
        self.Explorer2.addItem(item2)
    
    def qCopy2to1(self):
        item = self.Explorer2.currentItem()
        if (not item): return False
        item2 = item.clone()
        self.Explorer1.addItem(item2)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindowUser()
    window.show()
    app.exec_()
    #--------------------------------
    