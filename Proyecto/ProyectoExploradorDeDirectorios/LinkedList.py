from Compare import *
class Node:

    def __init__(self,value):
        self.value = value
        self.next = None
        self.children = LinkedList()
    
class LinkedList:

    def __init__(self):
        self.first = None

    def add(self, value):
        if(not self.first):
            self.first = Node(value)
            return True
        else:
            c = Compare()
            current = self.first

            if(c.compare(value,current.value) < 0):
                self.first = Node(value)
                self.first.next = current
                return True
            elif(c.compare(value,current.value) == 0):
                self.first = Node(value)
                self.first.next = current.next
                return True
            else:
                while(current.next):
                    previous = current
                    current = current.next
                    if(c.compare(value,current.value) < 0):
                        previous.next = Node(value)
                        previous.next.next = current
                        return True
                    elif(c.compare(value,current.value) == 0):
                        previous.next = Node(value)
                        previous.next.next = current.next
                        return True
                current.next = Node(value)
                return(True)

    def getNode(self, value):
        if(not self.first):
            return False
        else:
            current = self.first
            while(current.next):
                if(value == current.value):
                    return current
                current = current.next

            if(value == current.value):
                return current
            return False

    def toArray(self):
        current = self.first
        ar = []
        if(current):
            while(current.next):
                ar.append(current.value)
                current = current.next
            ar.append(current.value)

        return ar
    
    def removeForValue(self,valueToRmv):
        current=self.first
        if(current.value==valueToRmv):
            self.first=current.next
            return True
        while(current.next):
            before=current
            current=current.next
            if(current.value==valueToRmv):
                before.next=current.next
                return True
        return False

