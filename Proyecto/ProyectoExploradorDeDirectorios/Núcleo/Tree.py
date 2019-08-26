# -*- coding: utf-8 -*-
from Núcleo.Queue import *
from Núcleo.LinkedList import LinkedList
import copy
class Text:
    def __init__(self):
        self.text = ""


class Tree:

    def __init__(self):
        self.root = Node("ROOT/")
        self.root.children = LinkedList()   
        self.WIA = Queue(self.root) #WIA = WhereIAM  (El Ultimo Valor del WIA sera el actual padre activo,por defecto sera el root)
                                    #El WIA es una cola de nodos es decir de padres y Actuara como una memoria de la localizacion del Usario
    
    def add(self,value,current = None):   #Añadir Valor En la lista Children del actual Padre
        if(not current): current=self.root
        current.children.add(value)
        return True
    
    def remove(self,value,current = None):   #Eliminar Valor En la lista Children del actual Padre
        if(not current): current=self.root
        current.children.removeForValue(value)
        return True

    def getNodeParents(self, value, current = None):   #retorna el Nodo con el respectivo valor en la lista Children del actual Padre
        if(not current): current=self.root
        node = current.children.getNode(value) 
        return node
    
    '''Ejecuta un Comando,modifica el arbol dependiendo 
    el actual padre activo(Ultimo valor en el WIA)
    y retorna el el actual padre activo Actualizado'''
    def update(self, command = None, value = None, tree1 = None, tree2 = None):   
                                                                                  
        if(command == "goto"):  #Comando "ir"
            node = self.getNodeParents(value,self.WIA.getLastValue())   #Obtiene el nodo con el respectivo Valor en la lista Children del Actual Padre Activo
            self.WIA.add(node) #Añade el nodo en la WIA (El cual se convertira en el actual padre activo)
           
            return node   #Regresa el actual padre activo actualizado

        elif(command == "back"):   #Comando "Regresar"
            self.WIA.removeLast()   #Remueve el Ultimo valor del WIA cambiando el Actual padre activo al anterior
            node = self.WIA.getLastValue()   #Obtiene el Actual padre Activo

            return node   #Regresa el actual padre activo actualizado
        
        elif(command == "add"):   #Comando "Añadir"
            node = self.WIA.getLastValue()   #Obtiene el Actual padre Activo
            self.add(value,node)   #Añade el nuevo valor en el children del Actual padre Activo
            
            return self.WIA.getLastValue()   #Regresa el actual padre activo actualizado

        elif(command == "remove"):   #Comando "Eliminar"
            node = self.WIA.getLastValue()   #Obtiene el Actual padre Activo
            self.remove(value,node)    #Elimina el valor en el children del Actual padre Activo
            
            return self.WIA.getLastValue()   #Regresa el actual padre activo actualizado
        
        elif(command == "goStart"):   #Comando "Ir a Inicio"
            self.WIA.clearQueue()  #Limpia el WIA y el padre actual Activo pasa a ser el root
            
            return self.WIA.getLastValue() #Regresa el actual padre activo actualizado

        elif(command == "copy"):   #Comando "Copiar"

            #obtiene el actual padre activo del Arbol1
            #Busca dentro del ActualPadreActivo el nodo con el valor a copiar
            #retorna dicho nodo y se clona 
            nodeToCopy = copy.deepcopy(tree1.getNodeParents(value,tree1.WIA.getLastValue()))   
            nodeWhereCopy = tree2.WIA.getLastValue()   #obtiene el actual padre activo del Arbol2
            nodeWhereCopy.children.add(nodeToCopy.value)   #Añade en el children del actual padre activo del Arbol2 el valor del nodo clonado
            nodeCopied = nodeWhereCopy.children.getNode(nodeToCopy.value)   #busca el nodo agregado y lo retorna
            nodeCopied.children = nodeToCopy.children   #EL children del nodo clonado pasa a ser del nuevo nodo agregado en el arbol2

            return nodeWhereCopy   #Regresa el actual padre activo del arbol2 actualizado
        
        elif(not command):
            return self.WIA.getLastValue()   #Regresa el actual padre activo actualizado
    
    def showMeChildrens(self,current = None):   #Metodo Para retornar los valores del chidren de un nodo en forma de un arreglo
        if(not current): current=self.root
        Arr = current.children.toArray()

        return Arr  
    
    def treeToTsvStr(self,current,tab=0):  #Metodo para generar una cadena que representa el arbol 
        trail = ""
        while(current):
            if(current.value[-1]=="/"):   #en caso de ser carpeta generar otro texto que represente el contenido 
                trail = "%s%s%s\n" % (trail,"\t"*tab,current.value)
                trail = "%s%s" % (trail,self.treeToTsvStr(current.children.first,tab+1))#El contenido se ira acumulando recursivamente y la cantidad de tabulado se ira incrementando
            else:   #en caso de ser archivo
                trail = "%s%s%s\n" % (trail,"\t"*tab,current.value)
            current = current.next
        return trail
        
    def treeToFile(self,filename):   #Metodo que convierte el arbol en un texto plano
        current = self.root
        tsvStr = self.treeToTsvStr(current)
        f = open(filename,"w")
        f.write(tsvStr)
        f.close()
        return True


    def fileToTree(self,filename):   #Metodo que Convierte el texto plano en arbol
        f = open(filename,"r")
        tsvStr = f.read()   #Leer Archivo y guardar la cadena
        f.close()
        tsvArr = tsvStr.split("\n")   #Separa la cadena por cada salto de linea y la convierte en un arreglo
        for value in tsvArr:  
            if(value != ""):
                if(value.strip() == "ROOT/"):   #root se agrega por defeto asi que no sera necesario agregarlo
                    current = value   #El primer Current sera el Root
                
                else:   #Agregar los valores actuales, estos POR DEFECTO se AGREGARAN en el ANTERIOR
                    before = current   #El before sera el anterior current
                    current = value   #El Current pasara a ser el nuevo valor del bucle
                    beforeTabs = before.count("\t")   #cuenta los tabulados del anterior valor
                    currentTabs = current.count("\t")  #cuenta los tabulados del actual valor
                    difTab = (beforeTabs - currentTabs) #guarda la diferencia de tabulados entre los dos valores

                    if(difTab == -1 ):  #En caso de que el valor actual este dentro del valor anterior
                        self.update("add",current.strip()) #Añadir valor actual(por defecto se guardan en el anterior)
                        self.update("goto",current.strip()) #ir al Actual valor
                   
                    elif(difTab == 0 ):   #En caso de que el valor este en el mismo lugar que la carpeta anterior
                        self.update("back")   #Regresar dentro del arbol debido a que se guardan por defecto dentro del anterior
                        self.update("add",current.strip())   #Añadir valor actual
                        self.update("goto",current.strip())   #ir al Actual valor
                    
                    elif(difTab > 0):   #En caso de que el valor este agregado antes que el anterior
                        for _ in range(0,difTab+1,1):  #bucle que regresara segun la diferencia de tabulados a través del arbol 
                            self.update("back")
                        self.update("add",current.strip())    #Añadir valor actual
                        self.update("goto",current.strip())    #ir al Actual valor

        self.WIA.clearQueue()   #Limpiar WIA dejando el root para no afectar la visualizacion de la lista
    
       
        

        