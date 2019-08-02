class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None
        self.before = None

class LinkedList:

    def __init__(self):
        self.first = None

    def add(self, value):
        if(not self.first):
            self.first = Node(value)
        else:
            current = self.first
            while(current.next):
                current = current.next

            current.next = Node(value)
            current.next.before = current
    
    def _print(self):

        if(not self.first):
            print("N.A")
        else:
            current = self.first
            while(current.next):
                
                print("\n\nValor nodo Actual: %s" % (current.value,))
                print("\nValor nodo siguiente: %s" % (current.next.value,))
                
                if(current.before):
                    print("\nValor nodo Anterior: %s\n\n" % (current.before.value,))
                else:
                    print("\nValor nodo Anterior: %s\n\n" % ("No existe",))
              
                current = current.next
         
            print("\n\nValor nodo Actual: %s" % (current.value,))
            print("\nValor nodo Siguiente: %s" % ("No existe",))
            print("\nValor nodo Anterior: %s\n\n" % (current.before.value,))
    

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(6)
l._print()
            
        

