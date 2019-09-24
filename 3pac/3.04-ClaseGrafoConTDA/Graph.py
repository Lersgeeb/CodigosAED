from Vertex import Vertex,LinkedList
from Characteristic import Characteristic
import networkx as nx
import matplotlib.pyplot as plt
class Graph:

    def __init__(self):
        self.vertices = LinkedList()
        self.graph = {}
    
    def addVertex(self,nameVertex):
        self.vertices.add(Vertex(nameVertex))

    def addEdge(self,nameVertexOrigin,nameVertexDestination,characteristic = Characteristic()):
        vertexOrigin = self.vertices.search(nameVertexOrigin)
        vertexOrigin.setEdge(nameVertexDestination,characteristic)

    def connectedVertices(self,x):
        s = {}
        vertex_x = self.vertices.search(x)
        for edge in vertex_x.edges:
            s["%s" % edge.name] = "%s" % edge.weight
        for vertex in self.vertices:
            if(vertex.edges.alreadyExist(vertex_x)):
                for edge in vertex.edges:
                    if(edge.name == x):
                        s["%s" % vertex.name] = "%s" % edge.weight
        return s
   
    def getGraph(self):
        for vertex in self.vertices:
            self.graph[vertex.name] = self.connectedVertices(vertex.name)
        
        return self.graph

    def showGraph(self):
        G = nx.Graph()
        self.graph = self.getGraph()
        for v,edges in self.graph.items():
            G.add_node("%s" % (v))

            for e,w in edges.items():
                G.add_node("%s" % (e))
                #print(w)
                G.add_edge("%s" % v,"%s" % e,weight=w)
                #print("'%s' se conceta con '%s'" % (v,e))
        
        position = nx.spring_layout(G)
        labels={(vertex1,vertex2): weigth["weight"] for vertex1,vertex2,weigth in G.edges(data=True)}
        nx.draw(G,position, with_labels=True)
        nx.draw_networkx_edge_labels(G,position,edge_labels=labels,font_color="red")
        plt.show()
    
    #con derecho de autor 
     
x = "A"
g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addEdge("A","C",Characteristic(2))
g.addEdge("A","C",Characteristic(1))
g.addEdge("A","B",Characteristic(3))
g.addEdge("B","D",Characteristic(4))
g.addEdge("D","A",Characteristic(5))
g.addEdge("E","B",Characteristic(6))

print(g.vertices)
print(g.vertices.first.value.edges)
#print(g.connectedVertices("A"))
print("Las rutas de %s son  %s" % (x,g.connectedVertices(x)) ) 
print(g.getGraph())
g.showGraph()