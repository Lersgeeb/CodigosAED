class Node:
    def __init__(self,value):
        self.value = value
        self.rigth = None
        self.left = None

class EBST():

    def __init__(self):
        self.root = None

    def add(self, value, current = None):
        if(not self.root):
            self.root = Node(value)
            return True
        elif(not current):
            return self.add(value,self.root)
        else:
            if(value > current.value):
                if(current.rigth):
                    return self.add(value,current.rigth)
                else:
                    current.rigth = Node(value)
                    return True
            
            elif(value < current.value):
                if(current.left):
                    return self.add(value,current.left)
                else:
                    current.left = Node(value)
                    return True
            else: 
                return False

    def getNode(self, value, current = None):
        if(not self.root):
            return False
        elif(not current):
            return self.getNode(value,self.root)
        else:
            if(value > current.value):
                if(current.rigth):
                    return self.getNode(value,current.rigth)
                else:
                    return False
               
            elif(value < current.value):
                if(current.left):
                    return self.getNode(value,current.left)
                else:
                    return False
            else: 
                return current

    def getPrevNode(self, value, current = None ,prev = None):
        if(not self.root):
            return False
        elif(not current):
            return self.getPrevNode(value,self.root)
        else:
            if(value > current.value):
                if(current.rigth):
                    return self.getPrevNode(value,current.rigth, current)
                else:
                    return False
               
            elif(value < current.value):
                if(current.left):
                    return self.getPrevNode(value,current.left, current)
                else:
                    return False
            else: 
                return prev

    def addDown(self,node):
        if(node.rigth):
            self.add(node.rigth.value)
            current = self.getNode(node.rigth.value)
            current.rigth = node.rigth.rigth
            current.left = node.rigth.left
        if(node.left):
            self.add(node.left.value)
            current = self.getNode(node.left.value)
            current.rigth = node.left.rigth
            current.left = node.left.left
        
        return True
    
    def remove(self, value, current = None, prev = None):
        if(not self.root):
            return False            
        elif(not current):
            return self.remove(value,self.root)
        else:
            if(value > current.value):
                if(current.rigth):
                    return self.remove(value,current.rigth,current)
                else:
                    return False
            
            elif(value < current.value):
                if(current.left):
                    return self.remove(value,current.left,current)
                else:
                    return False
            else: 
                if(prev.rigth == current):
                    prev.rigth = None
                else:
                    prev.left = None
                self.addDown(current)
                return True

    def showTree(self,current = None):
        if(not self.root):
            print("Nada que Mostrar")
        elif(not current):
            current = self.root
            self.showTree(current)
        else:
            print("\n---------------------\nValor actual: %s" % (current.value,))
            if(current.rigth or current.left):
                if(current.left and  not current.rigth):
                    if(self.getPrevNode(current.value)):
                        bVal = self.getPrevNode(current.value).value
                    else:
                        bVal = "N.A"
                    ans = input(("\nl: ir izquierda (%s)\nb: ir atras (%s)\ne: salir del programa\nOpcion: ") % (current.left.value,bVal)) 
                    if(ans == 'b'):
                        self.showTree(self.getPrevNode(current.value))
                    elif(ans == 'l'):
                        self.showTree(current.left)
                    elif(ans == 'e'):
                        print("Salir")
                    else:
                        print("\nValor Indefinido\n")
                        self.showTree(current)

                elif(current.rigth and  not current.left):
                    if(self.getPrevNode(current.value)):
                        bVal = self.getPrevNode(current.value).value
                    else:
                        bVal = "N.A"
                    ans = input(("\nr: ir derecha (%s)\nb: ir atras (%s)\ne: salir del programa\nOpcion: ") % (current.rigth.value,bVal)) 
                    if(ans == 'b'):
                        self.showTree(self.getPrevNode(current.value))
                    elif(ans == 'r'):
                        self.showTree(current.rigth)
                    elif(ans == 'e'):
                        print("Salir")
                    else:
                        print("\nValor Indefinido\n")
                        self.showTree(current)
                else:
                    if(self.getPrevNode(current.value)):
                        bVal = self.getPrevNode(current.value).value
                    else:
                        bVal = "N.A"
                    ans = input(("\nr: ir derecha (%s)\nl: ir izquierda (%s)\nb: ir atras (%s)\ne: salir del programa\nOpcion: ") % (current.rigth.value,current.left.value,bVal)) 
                    if(ans == 'b'):
                        self.showTree(self.getPrevNode(current.value))
                    elif(ans == 'r'):
                        self.showTree(current.rigth)
                    elif(ans == 'l'):
                        self.showTree(current.left)
                    elif(ans == 'e'):
                        print("Salir")
                    else:
                        print("\nValor indefinido")
                        self.showTree(current)
            else:
                if(self.getPrevNode(current.value)):
                    bVal = self.getPrevNode(current.value).value
                else:
                    bVal = "N.A"
                print("\nYa no hay mas valores que mostrar")
                ans = input(("\nb: ir atras (%s)\ne: salir del programa\nOpcion: ") % (bVal,)) 
                if(ans == 'b'):
                    self.showTree(self.getPrevNode(current.value))
                elif(ans == 'e'):
                    print("Salir")
                else:
                    print("\nValor indefinido\n")
                    self.showTree(current)

t = EBST()
t.add(1)
t.add(3)
t.add(5)
t.add(0)
t.add(2)
t.add(4)
t.add(6)
t.add(15)
t.add(7)
t.add(11)
t.add(10)
t.remove(3)
t.showTree()