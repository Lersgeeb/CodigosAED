class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    #override
    def __str__(self):
        #se acepta en la impresion el uso de LIST para guardar los elementos
        #a imprimir
        p = []
        current = self.first
        while(current):
            p.append(current.value.name)
            current = current.next
        return ",".join(p)

    def add(self,value):
        if not self.first:
            self.first = Node(Vertex(value))
            return True
        else:
            if not self.alreadyExist(value):
                current = self.first
                while(current.next):
                    current = current.next
                current.next = Node(Vertex(value))
                return True
        return False
    
    def alreadyExist(self,value):

        current = self.first
        while(current):

           if current.value.name == value:
               return True
           current = current.next
        return False

    def search(self,value):
        current = self.first
        while(current):
            if current.value.name == value:
                return current.value
            current = current.next
        return False
class Edge:
    pass

class Vertex:
    def __init__(self,name):
        self.name = name
        self.edges = LinkedList()

    def setEdge(self,vertex_name):
        self.edges.add(vertex_name)

class Graph:
    def __init__(self):
        self.vertex = LinkedList()

    def add_vertex(self,vertex_name):
        self.vertex.add(vertex_name)

    def add_edge(self,vertex_origin,vertex_destination):
        vertex = self.vertex.search(vertex_origin)
        if not vertex.edges.alreadyExist(vertex_destination):
            vertex = self.vertex.search(vertex_origin)
            vertex.setEdge(vertex_destination)



    def connectedVertices(self,x):
        vertex,s = self.vertex,{}

        current = vertex.first
        while(current):
            if current.value.name == x:
                edges = current.value.edges
                current_edge = edges.first
                while(current_edge):
                    s[current_edge.value.name] = None
                    current_edge = current_edge.next
            elif current.value.edges.alreadyExist(x):
                s[current.value.name] = None
            current = current.next

        return list(s.keys())

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edge("A","B")
g.add_edge("B","A")

x = "A"

print("The graph is: %s" % (g.vertex))
print("the vertices connected to '%s' are: %s " % (x,g.connectedVertices(x)))
            