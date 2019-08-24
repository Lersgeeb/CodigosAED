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
        self.WIA = Queue(self.root) #WIA = WhereIAM

    def add(self,value,current = None):
        if(not current): current=self.root
        current.children.add(value)
        return True
    
    def remove(self,value,current = None):
        if(not current): current=self.root
        current.children.removeForValue(value)
        return True

    def getNodeParents(self, value, current = None):   #retorna nodo que contiene el valor en dicha lista enlazada 
        if(not current): current=self.root
        node = current.children.getNode(value) 
        return node

    def update(self, command = None, value = None, tree1 = None, tree2 = None):
        if(command == "goto"):
            node = self.getNodeParents(value,self.WIA.getLastValue())
            self.WIA.add(node)
           
            return node

        elif(command == "back"):
            self.WIA.removeLast()
            node = self.WIA.getLastValue()

            return node
        
        elif(command == "add"):
            node = self.WIA.getLastValue()
            self.add(value,node)
            return self.WIA.getLastValue()

        elif(command == "remove"):
            node = self.WIA.getLastValue()
            self.remove(value,node)
            return self.WIA.getLastValue()
        
        elif(command == "goStart"):
            self.WIA.clearQueue()
            
            return self.WIA.getLastValue()

        elif(command == "copy"):
            nodeToCopy = copy.deepcopy(tree1.getNodeParents(value,tree1.WIA.getLastValue()))
            nodeWhereCopy = tree2.WIA.getLastValue()
            nodeWhereCopy.children.add(nodeToCopy.value)
            nodeCopied = nodeWhereCopy.children.getNode(nodeToCopy.value)
            nodeCopied.children = nodeToCopy.children

            return nodeWhereCopy
        
        elif(not command):
            return self.WIA.getLastValue()
    
    def showMeChildrens(self,current = None):
        if(not current): current=self.root
        Arr = current.children.toArray()

        return Arr  #Retorna todos los valores del Children del current nodo
    
    def treeToTsv(self,current,tab=0):
        trail = ""
        while(current):
            if(current.value[-1]=="/"):
                trail = "%s%s%s\n" % (trail,"\t"*tab,current.value)
                trail = "%s%s" % (trail,self.treeToTsv(current.children.first,tab+1))
            else:
                trail = "%s%s%s\n" % (trail,"\t"*tab,current.value)
            current = current.next
        return trail
        
    def tsvToFile(self,filename):
        current = self.root
        tsvStr = self.treeToTsv(current)
        f = open(filename,"w")
        f.write(tsvStr)
        f.close()
        return True


    def fileToTree(self,filename):
        f = open(filename,"r")
        tsvStr = f.read()
        f.close()
        tsvArr = tsvStr.split("\n")
        for value in tsvArr:
            if(value != ""):
                copyValue = copy.copy(value)
                if(copyValue.strip() == "ROOT/"): 
                    current = value
                else:
                    before = current
                    current = value
                    beforeTabs = before.count("\t")
                    currentTabs = current.count("\t")
                    difTab = (beforeTabs - currentTabs)
                
                    if(difTab == -1 ):
                        self.update("add",current.strip())
                        self.update("goto",current.strip())
                    elif(difTab == 0 ):
                        self.update("back")
                        self.update("add",current.strip())
                        self.update("goto",current.strip())
                    elif(difTab > 0):
                        for _ in range(0,difTab+1,1):
                            self.update("back")
                        self.update("add",current.strip())
                        self.update("goto",current.strip()) 

        self.WIA.clearQueue()
    
       
        

        