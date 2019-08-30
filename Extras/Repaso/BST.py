import math

class Node:
    
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
        self.next = None

class BST:

    def __init__(self):
        self.root = None
    
    def add(self,value):
        return self.addInner(value,self.root)
 
    def addInner(self,value,current):
        if(not current):
            self.root = Node(value)
            return True
        if(value > current.value):
            if(current.right):
                self.addInner(value,current.right)
            else:
                current.right = Node(value)
                return True
        elif(value < current.value):
            if(current.left):
                self.addInner(value,current.left)
            else:
                current.left = Node(value)
                return True
        else:
            return False 

    def bstToLinkedList(self):
        size = self.getLength()
        maxsize = int(math.pow(2,size) - 1)  
        arr =[]
        blankArr = ["None" for i in range(0,maxsize)]
        arr = self.bstToArray(self.root,blankArr)
        arr = self.clearArray(arr)
        lList = LinkedList()
        for value in arr:
            lList.add(value)
        return lList

    def clearArray(self,array):
        while(array[-1]=="None"):
            del array[-1]
        return array

    def bstToArray(self,current,ar = [],parent = 0):
        if(current): 
            ar[parent] = current.value
            if(current.left):
                self.bstToArray(current.left,ar,(2*parent + 1))
            if(current.right):
                self.bstToArray(current.right,ar,(2*parent + 2))     
        return ar 

    def getLength(self):
        return self.getLengthInner(self.root)

    def getLengthInner(self,current):
        sumLeft,sumRight,count = (0,0,0)
        if(current):
            count += 1
        if(current.left):
            sumLeft = self.getLengthInner(current.left) 
        if(current.right):
            sumRight = self.getLengthInner(current.right) 
        
        return sumLeft + sumRight + count


        
class LinkedList:
    
    def __init__(self):
        self.first = None

    def add(self,value):
        current = self.first
        if(not current):
            self.first = Node(value)
            return True
        else:
            while(current.next):
                current = current.next
            current.next = Node(value)
            return True

    def getLength(self):
        count=0
        if(self.first):
            current = self.first
            count += 1
        while(current.next):
            current = current.next
            count += 1
        
        return count
    
    def atPosition(self,n):
        count = 0
        current = self.first
        while(count<n):
            if(current):
                current = current.next
                count += 1
            else:
                return False
        if(current):        
            return current.value
        return False


class Heap:
    def __init__(self):
        pass
    def build(self,LL):
        n = LL.getLength()
        h = math.ceil( math.log2( n + 1) )
        mi = int(math.pow(2, h-1) - 1)
        mf = mi * 2 
        w = mf + 1
    
        matriz = [["&nbsp"*8 for i in range(0,w)] for j in range(0,h)]
        half = math.floor(w/2)
        count = 0

        matriz[0][half] = LL.atPosition(count)
        count += 1
        for i in range(1,h):
            bs = int (math.pow(2,h-i) - 1)
            bsi = math.floor( bs/2 )
            j=0
            while(j<w):
                if(j==0):
                    j += bsi
                    matriz[i][j] = LL.atPosition(count)
                    count += 1
                elif(j+bs < w and count<n):
                    j += bs
                    matriz[i][j] = LL.atPosition(count)
                    count += 1
                j+=1
        self.MakeHTMLHeap(matriz)

    def MakeHTMLHeap(self, matrix):
        f = open("Extras//Repaso//indexHeap.html","w")
        htmlStr = self.htmlTable(matrix)
        f.write(htmlStr)
        f.close()

    def htmlTable(self,matrix):
        htmlArr = ["<table border='5'>"]
        for r in matrix:
            row = []
            for value in r:
                row.append(str(value))
            htmlArr.append("<tr><td>")
            htmlArr.append("</td><td>".join(row))
            htmlArr.append("</td></tr>")
        htmlArr.append("</table>")
        return "".join(htmlArr)

'''
'''
t = BST()
t.add(10)
t.add(12)
t.add(11)
t.add(14)
t.add(5)
t.add(6)
t.add(13)
t.add(9)

l = t.bstToLinkedList()
h = Heap()
h.build(l)

