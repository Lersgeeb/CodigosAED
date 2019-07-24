from Node import *

class Shelf:
    def __init__(self):
        self.first = None

    def push(self,value):
        temp = self.first
        self.first = Node(value)
        self.first.next = temp
        return True

    def pop(self):
        temp = self.first
        self.first= self.first.next
        return temp.value
    
    def nBoxes(self):
        count = 0
        temp = self.first
        while temp:
            count +=1
            temp = temp.next
        return "---------------------------\nCajas: %s\n---------------------------" % count
