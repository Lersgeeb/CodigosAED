from Queue import *
from LinkedList import *
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

    def refresh(self, command = None, value = None):
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
        
        elif(not command):
            return self.WIA.getLastValue()
    
    def showMeChildrens(self,current = None):
        if(not current): current=self.root
        Arr = current.children.toArray()

        return Arr  #Retorna todos los valores del Children del current nodo

    def treeToTSV(self,parent,count=0,text = None):
        if not text: text = Text()
        text.text+="\t"*count
        text.text+= ("%s \n" % (parent.value,))
        if parent.next:
            if parent.children.first:
                self.treeToTSV(parent.children.first,count+1,text)
            self.treeToTSV(parent.next,count,text)
        elif parent.children.first:
            count+=1
            self.treeToTSV(parent.children.first,count,text)
        return text.text

    def tsvToFile(self,current,filename):
        text = self.treeToTSV(current)
        f = open(filename,"w")
        f.write(text)
        f.close


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
                    #n: ir atras n posiciones y agregar en el current 0: add en el current lugar -1:meterme en el anterior agregado y add en el current
                    if(difTab == -1 ):
                        self.refresh("add",current.strip())
                        self.refresh("goto",current.strip())
                    elif(difTab == 0 ):
                        self.refresh("back")
                        self.refresh("add",current.strip())
                        self.refresh("goto",current.strip())
                    elif(difTab > 0):
                        for i in range(0,difTab+1,1):
                            self.refresh("back")
                        self.refresh("add",current.strip())
                        self.refresh("goto",current.strip()) 

        self.WIA.clearQueue()
    
       
        

        