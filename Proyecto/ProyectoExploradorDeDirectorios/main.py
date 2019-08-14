from UiWindow import *
from Tree import *
import copy


class MainWindowUser(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #--------------------------------------
        
        self.tree1 = Tree()
        self.tree1.fileToTree("Archivo1.tsv")
        self.tree2 = Tree()
        self.tree2.fileToTree("Archivo2.tsv")
       

       
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
        self.qRefresh1(self.tree1.refresh())
        self.qRefresh2(self.tree2.refresh())
        
       

    def qGoTo1(self):#***
        if(self.Explorer1.currentItem().text() == ".."):
            node = self.tree1.refresh("back")
            self.Explorer1.clear()
            self.qRefresh1(node)
        elif(self.Explorer1.currentItem().text() == "."):
            node = self.tree1.refresh("goStart")
            self.Explorer1.clear()
            self.qRefresh1(node)
        elif(self.Explorer1.currentItem().text()[-1] == "/"):
            node = self.tree1.refresh("goto",self.Explorer1.currentItem().text())
            self.Explorer1.clear()
            self.qRefresh1(node)

    def qGoTo2(self):#***
        if(self.Explorer2.currentItem().text() == ".."):
            node = self.tree2.refresh("back")
            self.Explorer2.clear()
            self.qRefresh2(node)
        elif(self.Explorer2.currentItem().text() == "."):
            node = self.tree2.refresh("goStart")
            self.Explorer2.clear()
            self.qRefresh2(node)
        elif(self.Explorer2.currentItem().text()[-1] == "/"):
            node = self.tree2.refresh("goto",self.Explorer2.currentItem().text())
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
            node = self.tree1.refresh("add",name)
            self.Explorer1.clear()
            self.qRefresh1(node)
            
        else:
            pass  

    def qAddDir2(self):#***
        name = self.qGetName("carpeta")
        if(name):
            name = name + "/"
            node = self.tree2.refresh("add",name)
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
        icon1.addPixmap(QtGui.QPixmap("folderIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("archiveIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        for value in a:
            if(value[-1] == "/"):
                items.append(QtWidgets.QListWidgetItem(icon1,value))
            else:
                items.append(QtWidgets.QListWidgetItem(icon2,value))
        for item in items:
            self.Explorer1.addItem(item)
        
        self.tree1.tsvToFile(self.tree1.root,"Archivo1.tsv")

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
        icon1.addPixmap(QtGui.QPixmap("folderIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("archiveIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        for value in a:
            if(value[-1] == "/"):
                items.append(QtWidgets.QListWidgetItem(icon1,value))
            else:
                items.append(QtWidgets.QListWidgetItem(icon2,value))
        for item in items:
            self.Explorer2.addItem(item)

        self.tree2.tsvToFile(self.tree2.root,"Archivo2.tsv")
   
    def qAddAr1(self):#***
        name = self.qGetName("archivo")
        if(name):
            node = self.tree1.refresh("add",name)
            self.Explorer1.clear()
            self.qRefresh1(node)
            
        else:
            pass    

    def qAddAr2(self):#***
        name = self.qGetName("archivo")
        if(name):
            node = self.tree2.refresh("add",name)
            self.Explorer2.clear()
            self.qRefresh2(node)
            
        else:
            pass      

    def qRemove1(self):
        listItems=self.Explorer1.selectedItems()
        if not listItems: return        
        for item in listItems:
            node = self.tree1.refresh("remove",item.text())
        self.Explorer1.clear()
        self.qRefresh1(node)
   
    def qRemove2(self):
        listItems=self.Explorer2.selectedItems()
        if not listItems: return        
        for item in listItems:
            node = self.tree2.refresh("remove",item.text())
        self.Explorer2.clear()
        self.qRefresh2(node)

    

    def qCopy1to2(self):
        listItems = self.Explorer1.selectedItems()
        if not listItems: return   
        for item in listItems:
            node1 = copy.deepcopy(self.tree1.getNodeParents(item.text(),self.tree1.WIA.getLastValue()))
            node2 = self.tree2.WIA.getLastValue()
            node2.children.add(node1.value)
            node3 = node2.children.getNode(node1.value)
            node3.children = node1.children

        self.Explorer2.clear()
        self.qRefresh2(node2)

    def qCopy2to1(self):
        listItems = self.Explorer2.selectedItems()
        if not listItems: return   
        for item in listItems:
            node1 = copy.deepcopy(self.tree2.getNodeParents(item.text(),self.tree2.WIA.getLastValue()))
            node2 = self.tree1.WIA.getLastValue()
            node2.children.add(node1.value)
            node3 = node2.children.getNode(node1.value)
            node3.children = node1.children

        self.Explorer1.clear()
        self.qRefresh1(node2)

   

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindowUser()
    window.show()
    app.exec_()
    #--------------------------------
    