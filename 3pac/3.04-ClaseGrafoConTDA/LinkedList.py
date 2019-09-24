from Node import Node

class LinkedList:

    def __init__(self):
        self.first = None

    def add(self, value):
        if(not self.first):
            self.first = Node(value)
            return True
        else:
            if( not self.alreadyExist(value) ):
                current = self.first
                while(current.next):
                    current = current.next
                current.next = Node(value)
                return True
            return False

    def alreadyExist(self, value):
        if(not self.first):
            return False
        else:
            current = self.first 
            while(current):
                if(value.name == current.value.name):
                    return True
                current = current.next
            return False

    def search(self,value):
        if(not self.first):
            return False
        else:
            current = self.first 
            while(current):
                if(value == current.value.name):
                    return current.value
                current = current.next
            return False

    def __str__(self):
        if(not self.first):
            return " "
        else:
            valueArray = []
            current = self.first
            while(current):
                valueArray.append(str(current.value.name) )#current.value.name
                current = current.next
            return ", ".join(valueArray)

    def __iter__(self):
        if(not self.first):
            return None
        else:
            current = self.first 
            while(current):
                yield current.value
                current = current.next
            