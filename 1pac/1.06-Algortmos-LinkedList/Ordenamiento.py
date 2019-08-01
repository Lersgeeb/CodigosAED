class Node:

    def __init__(self, value):
        self.value = value 
        self.next = None

class LinkedList:

    def __init__(self):
        self.first = None

    def add(self, value):
        
        if(not self.first):
            self.first = Node(value)

            return True
            
        else:
            current = self.first
            if(value >= current.value):
                self.first = Node(value)
                self.first.next = current

                return True
            else:
                while(current.next):
                    before = current
                    current = current.next
                    if(value >= current.value):
                        before.next = Node(value)
                        before.next.next = current
                        return True
                
                current.next = Node(value)
                return True


    def _print(self):
        current = self.first
        while(current.next):
            print(current.value)
            current=current.next
        print(current.value)
        

                    


                
print("hola") 
Lista = LinkedList()
Lista.add(1)     
Lista.add(2)     
Lista.add(3)     
Lista.add(6)      
Lista.add(5)
Lista.add(5)
Lista.add(2)
Lista.add(1)
Lista._print()      