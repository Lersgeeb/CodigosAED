from Queue import *
from LinkedList import *
class Tree:

    def __init__(self):
        self.root = Node("ROOT")
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

    def getNodeParents(self, value, current = None):    
        if(not current): current=self.root
        node = current.children.getNode(value) 
        return node

    def refresh(self, command, value = None):
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
    
    def showMeChildrens(self,current = None):
        if(not current): current=self.root
        Arr = current.children.toArray()

        return Arr  #Retorna todos los valores del Children del current nodo
            

t = Tree()
nod = t.refresh("add", 17)
nod = t.refresh("add", 12)
nod = t.refresh("add", 20)
nod = t.refresh("goto",12)
nod = t.refresh("add", 15)
nod = t.refresh("goto",15)
nod = t.refresh("back")
nod = t.refresh("back")
nod = t.refresh("remove",17)

print("\nActual ruta: %s" % (t.WIA,))
print("Actual Carpeta: %s" % (nod.value,))
print("Hijos de la Actual ruta: %s\n" % (t.showMeChildrens(t.WIA.getLastValue()),))
 