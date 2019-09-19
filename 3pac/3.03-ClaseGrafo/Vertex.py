from LinkedList import LinkedList
from Edge import Edge

class Vertex:
    def __init__(self,name):
        self.name = name
        self.edges = LinkedList()
    
    def setEdge(self,vertex,characteristic):
        self.edges.add(Edge(vertex,characteristic)) 