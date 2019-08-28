# -*- coding: utf8 -*-
from Núcleo.UiWindow import Ui_MainWindow, QtCore, QtGui, QtWidgets
from Núcleo.Tree import Tree 

class MainWindowUser(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #--------------------------------------
        self.center()

        self.treeA = Tree()   #Crear arbol para la lista A
        self.treeA.fileToTree("Memoria//Tree-A.mem") #Leer la memoria del Arbol A 
        self.treeB = Tree()   #Crear arbol para la lista A
        self.treeB.fileToTree("Memoria//Tree-B.mem") #Leer la memoria del arbol B 
              
        #Conectar Eventos de los Botones de la Lista A con los metodos      
        self.Explorer1.itemDoubleClicked.connect(self.qGoTo1)  
        self.CreateDir1.clicked.connect(self.qAddDir1) 
        self.CreateAr1.clicked.connect(self.qAddAr1)
        self.Remove1.clicked.connect(self.qRemove1)
        self.qRefresh1(self.treeA.update())
      
        #Conectar Eventos de los Botones de la Lista B con los metodos  
        self.Explorer2.itemDoubleClicked.connect(self.qGoTo2)
        self.CreateDir2.clicked.connect(self.qAddDir2)
        self.CreateAr2.clicked.connect(self.qAddAr2)
        self.Remove2.clicked.connect(self.qRemove2)
        self.qRefresh2(self.treeB.update())
       
        #Conectar Eventos de los Botones de Copiar con los metodos  
        self.Copy1to2.clicked.connect(self.qCopy1to2)
        self.Copy2to1.clicked.connect(self.qCopy2to1)
        
       

    def qGoTo1(self):   #Metodo para navegar por el Arbol A (ejecutado cuando se le hace dobleCLick a un item)
       
        if(self.Explorer1.currentItem().text() == ".."):   #En caso de ser ".."
            node = self.treeA.update("back")   #Ejecutar comando Regresar que retorara el nodo anterior del padre
            self.Explorer1.clear()   #Limpiar pantalla de la Lista A
            self.qRefresh1(node)   #Refrescar pantalla con el padre nodo ya actualizado
        
        elif(self.Explorer1.currentItem().text() == "."):   #En caso de ser "."
            node = self.treeA.update()   #Retornara el nodo actual
            self.Explorer1.clear()   #Limpiar pantalla de la Lista A
            self.qRefresh1(node)     #Refrescar pantalla con el padre nodo ya actualizado
        
        elif(self.Explorer1.currentItem().text()[-1] == "/"):   #En caso de ser Carpeta
            node = self.treeA.update("goto",self.Explorer1.currentItem().text())   #Ejecutar comando "ir" y el objeto seleccionado lo retorna como nodo padre
            self.Explorer1.clear()   #Limpiar pantalla de la Lista A
            self.qRefresh1(node)    #Refrescar pantalla con el padre nodo ya actualizado

    def qGoTo2(self): #Metodo para navegar por el Arbol B (ejecutado cuando se le hace dobleCLick a un item) 
        if(self.Explorer2.currentItem().text() == ".."): 
            node = self.treeB.update("back")
            self.Explorer2.clear()
            self.qRefresh2(node)
        elif(self.Explorer2.currentItem().text() == "."):
            node = self.treeB.update()
            self.Explorer2.clear()
            self.qRefresh2(node)
        elif(self.Explorer2.currentItem().text()[-1] == "/"):
            node = self.treeB.update("goto",self.Explorer2.currentItem().text())
            self.Explorer2.clear()
            self.qRefresh2(node)
        
    
    def qGetName(self,dataType):   #Metodo que abre una nueva Ventana para preguntar el nombre del nuevo Archivo/Carpeta y retornarlo
        
        text,okPressed = QtWidgets.QInputDialog.getText(self,"",("Nombre de su %s" % dataType), QtWidgets.QLineEdit.Normal, "")
        #El metodo retornara una tupla de la forma(str , bool) el segundo depende de si fue presionado el boton OK
        if(okPressed and text != ''):
            return text
        else:
            return False

    def qAddDir1(self):   #Metodo para Agregar nueva carpeta en la Lista A
        name = self.qGetName("carpeta") #Obtener nombre de la carpeta
        if(name):
            name = name + "/" #al final del nombre agregarle "/"
            node = self.treeA.update("add",name)   #Ejecutar comando añadir en padre y retorna el mismo nodo actualizado
            self.Explorer1.clear()   #Limpiar pantalla de la Lista A
            self.qRefresh1(node)   #Refrescar pantalla con el padre nodo ya actualizado
            
        else:
            pass  

    def qAddDir2(self):   #Metodo para Agregar nueva carpeta en la Lista B
        name = self.qGetName("carpeta")
        if(name):
            name = name + "/"
            node = self.treeB.update("add",name)
            self.Explorer2.clear()
            self.qRefresh2(node)
            
        else:
            pass   

    def qRefresh1(self,node): #Metodo para Actualizar la Pantalla de la Lista A segun el nodo padre dado
        a = self.treeA.showMeChildrens(node)   #del nodo padre Obtener un Arreglo con los valores de los hijos 
        items = []   #Arreglo donde se agregaran los valores en forma de items y respectivo icono
        
        if(node.value != "ROOT/"):   #si el nodo padre no es el nodo root
            
            deepBackItem = QtWidgets.QListWidgetItem(".")   #crear item "."
            deepBackItem.setFlags(QtCore.Qt.NoItemFlags)   #Quitarle los "eventos" que retorna (Para evitar que sea seleccionada)
            deepBackItem.setFlags(QtCore.Qt.ItemIsEnabled)   #agregarle eventos de Clicado
            self.Explorer1.addItem(deepBackItem)   #Añadirlo a la lista
            
            backItem = QtWidgets.QListWidgetItem("..")   #crear item ".."
            backItem.setFlags(QtCore.Qt.NoItemFlags)   #Quitarle los "eventos" que retorna(Para evitar que sea seleccionada)
            backItem.setFlags(QtCore.Qt.ItemIsEnabled)   #agregarle eventos de Clicado
            self.Explorer1.addItem(backItem)   #Añadirlo a la lista

        icon1 = QtGui.QIcon()   #crear Icono1
        icon1.addPixmap(QtGui.QPixmap("Núcleo//folderIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  #Añadir Icono Folder
        icon2 = QtGui.QIcon()  #crear Icono2
        icon2.addPixmap(QtGui.QPixmap("Núcleo//archiveIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)   #Añadir Icono Archivo

        for value in a:
            if(value[-1] == "/"):   #En caso de ser Carpeta
                items.append(QtWidgets.QListWidgetItem(icon1,value))   #Crear/Agregar al arreglo un item del valor actual y respectivo icono
            else:   #en Caso de ser Archivo
                items.append(QtWidgets.QListWidgetItem(icon2,value))   #Crear/Agregar al arreglo un item del valor actual y respectivo icono
        for item in items:
            self.Explorer1.addItem(item)   #Añadir los items a la pantalla 
        
        self.treeA.treeToFile("Memoria//Tree-A.mem")   #Guardar el cambio en memoria

    def qRefresh2(self,node):   #Metodo para Actualizar la Pantalla de la Lista B segun el nodo padre dado
        a = self.treeB.showMeChildrens(node)
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

        self.treeB.treeToFile("Memoria//Tree-B.mem")
   
    def qAddAr1(self):   #Metodo para Agregar nueva Archivo en la Lista A
        name = self.qGetName("archivo")   #Obtener nombre del Archivo
        if(name):
            node = self.treeA.update("add",name)   #Ejecutar comando añadir en padre y retorna el mismo nodo actualizado
            self.Explorer1.clear()   #Limpiar pantalla de la Lista A
            self.qRefresh1(node)   #Refrescar pantalla con el padre nodo ya actualizado
            
        else:
            pass    

    def qAddAr2(self):   #Metodo para Agregar nueva Archivo en la Lista B
        name = self.qGetName("archivo")
        if(name):
            node = self.treeB.update("add",name)
            self.Explorer2.clear()
            self.qRefresh2(node)
            
        else:
            pass      

    def qRemove1(self):    #Metodo para Eliminar item en la Lista A
        listItems=self.Explorer1.selectedItems() #Arreglo de los items seleccionado
        if not listItems: return  #En caso de no haber algo seleccionado       
        
        for item in listItems:   
            node = self.treeA.update("remove",item.text())   #Ejecutar comando "Remover" en padre y retornar el mismo nodo actualizado
        self.Explorer1.clear()   #Limpiar pantalla de la Lista A
        self.qRefresh1(node)   #Refrescar pantalla con el padre nodo ya actualizado
   
    def qRemove2(self):   #Metodo para Eliminar item en la Lista B
        listItems=self.Explorer2.selectedItems()
        if not listItems: return        
        for item in listItems:
            node = self.treeB.update("remove",item.text())
        self.Explorer2.clear()
        self.qRefresh2(node)

    

    def qCopy1to2(self):   #Metodo para Copiar items de la Lista A en la Lista B
        listItems = self.Explorer1.selectedItems()    #Arreglo de los items seleccionado
        if not listItems: return   #En caso de no haber algo seleccionado 
        for item in listItems:
            node = self.treeB.update("copy",item.text(),self.treeA,self.treeB)   #Ejecutar comando "copiar" el valor del arbolA al padre actual del ArbolB y retornar el mismo padre actualizado

        self.Explorer2.clear()    #Limpiar pantalla de la Lista B
        self.qRefresh2(node)   #Refrescar pantalla de La lista B con el padre nodo ya actualizado

    def qCopy2to1(self):   #Metodo para Copiar items de la Lista B en la Lista A
        listItems = self.Explorer2.selectedItems()
        if not listItems: return   
        for item in listItems:
            node = self.treeB.update("copy",item.text(),self.treeB,self.treeA)
            
        self.Explorer1.clear()
        self.qRefresh1(node) 

    def center(self):   #Metodo para centrar la ventana
        qRect = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft()) 
   
#------------------------------------
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindowUser()
    window.show()
    app.exec_()
    #--------------------------------
    