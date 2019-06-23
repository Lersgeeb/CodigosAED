class Node:

    def __init__(self,value):
        self.value = value
        self.next = None
        

class LinkedList:
    
    def __init__(self):
        self.first = None
    
    def add(self,value):
        if(not self.first):
            self.first = Node(value)
            return True
        else:
            current=self.first
            while(current.next):
                current=current.next
            current.next= Node(value)
            return True
        
    def _print(self):
        current=self.first
        while(current.next):
            print(current.value)
            current=current.next
        print(current.value)

    def addInPosition(self,value,n):
        if(n==0):
            queue=self.first
            self.first=Node(value)
            self.first.next=queue
            return True
        else:
            count=0
            queue=self.first
            while(queue.next):
                beforeQ=queue
                queue=queue.next
                count += 1
                if(count == n):
                    beforeQ.next=Node(value)
                    beforeQ.next.next=queue
                    return True
            count+=1
            if(count == n):
                queue.next=Node(value)
                return True
            print("No se encontro Posicion")
            return False
    
    def getFirst(self):
        return self.first.value

    def getLast(self):
        current = self.first
        while(current.next):
            current=current.next
        return current.value
    
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

    def removeForPosition(self,n):
        current=self.first
        if(n==0):
            self.first=current.next
            return True
        else:
            count=0
            while(current.next):
                before=current
                current=current.next
                count +=1
                if(count==n):
                    before.next=current.next
                    return True
            return False
                
