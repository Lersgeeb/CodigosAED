# -*- coding: utf8 -*-
from Núcleo.UiWindow import Ui_MainWindow, QtCore, QtGui, QtWidgets
from Núcleo.Tree import Tree 



class MainWindowUser(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #--------------------------------------
        
        self.tree1 = Tree()
        self.tree1.fileToTree("Memoria//Tree-A.mem")
        self.tree2 = Tree()
        self.tree2.fileToTree("Memoria//Tree-B.mem")
       

       
        self.Explorer1.itemDoubleClicked.connect(self.qGoTo1)
        self.CreateDir1.clicked.connect(self.qAddDir1)
        self.CreateAr1.clicked.connect(self.qAddAr1)
        self.Remove1.clicked.connect(self.qRemove1)
      
        self.Explorer2.itemDoubleClicked.connect(self.qGoTo2)
        self.CreateDir2.clicked.connect(self.qAddDir2)
        self.CreateAr2.clicked.connect(self.qAddAr2)
        self.Remove2.clicked.connect(self.qRemove2)
        self.Copy1to2.clicked.connect(self.qCopy1to2)
        self.Copy2to1.clicked.connect(self.qCopy2to1)
        self.qRefresh1(self.tree1.update())
        self.qRefresh2(self.tree2.update())
        
       

    def qGoTo1(self):#***
        if(self.Explorer1.currentItem().text() == ".."):
            node = self.tree1.update("back")
            self.Explorer1.clear()
            self.qRefresh1(node)
        elif(self.Explorer1.currentItem().text() == "."):
            node = self.tree1.update("goStart")
            self.Explorer1.clear()
            self.qRefresh1(node)
        elif(self.Explorer1.currentItem().text()[-1] == "/"):
            node = self.tree1.update("goto",self.Explorer1.currentItem().text())
            self.Explorer1.clear()
            self.qRefresh1(node)

    def qGoTo2(self):#***
        if(self.Explorer2.currentItem().text() == ".."):
            node = self.tree2.update("back")
            self.Explorer2.clear()
            self.qRefresh2(node)
        elif(self.Explorer2.currentItem().text() == "."):
            node = self.tree2.update("goStart")
            self.Explorer2.clear()
            self.qRefresh2(node)
        elif(self.Explorer2.currentItem().text()[-1] == "/"):
            node = self.tree2.update("goto",self.Explorer2.currentItem().text())
            self.Explorer2.clear()
            self.qRefresh2(node)
        
    
    def qGetName(self,dataType):#***
        text,okPressed = QtWidgets.QInputDialog.getText(self,"",("Nombre de su %s" % dataType), QtWidgets.QLineEdit.Normal, "")
        if(okPressed and text != ''):
            return text
        else:
            return False

    def qAddDir1(self):#***
        name = self.qGetName("carpeta")
        if(name):
            name = name + "/"
            node = self.tree1.update("add",name)
            self.Explorer1.clear()
            self.qRefresh1(node)
            
        else:
            pass  

    def qAddDir2(self):#***
        name = self.qGetName("carpeta")
        if(name):
            name = name + "/"
            node = self.tree2.update("add",name)
            self.Explorer2.clear()
            self.qRefresh2(node)
            
        else:
            pass   

    def qRefresh1(self,node):#***
        a = self.tree1.showMeChildrens(node)
        items = []
        if(node.value != "ROOT/"):
            deepBackItem = QtWidgets.QListWidgetItem(".") 
            deepBackItem.setFlags(QtCore.Qt.NoItemFlags) 
            deepBackItem.setFlags(QtCore.Qt.ItemIsEnabled) 
            self.Explorer1.addItem(deepBackItem)
            backItem = QtWidgets.QListWidgetItem("..") 
            backItem.setFlags(QtCore.Qt.NoItemFlags) 
            backItem.setFlags(QtCore.Qt.ItemIsEnabled) 
            self.Explorer1.addItem(backItem)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Núcleo//folderIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Núcleo//archiveIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        for value in a:
            if(value[-1] == "/"):
                items.append(QtWidgets.QListWidgetItem(icon1,value))
            else:
                items.append(QtWidgets.QListWidgetItem(icon2,value))
        for item in items:
            self.Explorer1.addItem(item)
        
        self.tree1.tsvToFile(self.tree1.root,"Memoria//Tree-A.mem")

    def qRefresh2(self,node):#***
        a = self.tree2.showMeChildrens(node)
        items = []
        if(node.value != "ROOT/"):
            deepBackItem = QtWidgets.QListWidgetItem(".") 
            deepBackItem.setFlags(QtCore.Qt.NoItemFlags) 
            deepBackItem.setFlags(QtCore.Qt.ItemIsEnabled) 
            self.Explorer2.addItem(deepBackItem)
            backItem = QtWidgets.QListWidgetItem("..") 
            backItem.setFlags(QtCore.Qt.NoItemFlags) 
            backItem.setFlags(QtCore.Qt.ItemIsEnabled) 
            self.Explorer2.addItem(backItem)
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Núcleo//folderIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Núcleo//archiveIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        for value in a:
            if(value[-1] == "/"):
                items.append(QtWidgets.QListWidgetItem(icon1,value))
            else:
                items.append(QtWidgets.QListWidgetItem(icon2,value))
        for item in items:
            self.Explorer2.addItem(item)

        self.tree2.tsvToFile(self.tree2.root,"Memoria//Tree-B.mem")
   
    def qAddAr1(self):#***
        name = self.qGetName("archivo")
        if(name):
            node = self.tree1.update("add",name)
            self.Explorer1.clear()
            self.qRefresh1(node)
            
        else:
            pass    

    def qAddAr2(self):#***
        name = self.qGetName("archivo")
        if(name):
            node = self.tree2.update("add",name)
            self.Explorer2.clear()
            self.qRefresh2(node)
            
        else:
            pass      

    def qRemove1(self):
        listItems=self.Explorer1.selectedItems()
        if not listItems: return        
        for item in listItems:
            node = self.tree1.update("remove",item.text())
        self.Explorer1.clear()
        self.qRefresh1(node)
   
    def qRemove2(self):
        listItems=self.Explorer2.selectedItems()
        if not listItems: return        
        for item in listItems:
            node = self.tree2.update("remove",item.text())
        self.Explorer2.clear()
        self.qRefresh2(node)

    

    def qCopy1to2(self):
        listItems = self.Explorer1.selectedItems()
        if not listItems: return   
        for item in listItems:
            node = self.tree2.update("copy",item.text(),self.tree1,self.tree2)

        self.Explorer2.clear()
        self.qRefresh2(node)

    def qCopy2to1(self):
        listItems = self.Explorer2.selectedItems()
        if not listItems: return   
        for item in listItems:
            node = self.tree2.update("copy",item.text(),self.tree2,self.tree1)
            
        self.Explorer1.clear()
        self.qRefresh1(node)

   

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindowUser()
    window.show()
    app.exec_()
    #--------------------------------
    