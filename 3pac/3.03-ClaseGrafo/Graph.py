from LinkedList import LinkedList
from Vertex import Vertex
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
    '''
    def findPaths(self, graph, vertex, destination, path = [], visited = []):
        #Agrego el vertice actual a la ruta y lo marco como visitado(para evitar ciclos)
        visited.append(vertex)
        path.append(vertex)

        #Si el vertice actual es mi destino, imprimo la ruta seguida
        if (vertex == destination):
            print(path)

        #Si no es el destino, se iteran las aristas del vertice actual
        else:
            for edge in graph[vertex]:
                #Si la arista actual no se encuentra en los visitados, se llama recursivamente la función 
                #para seguir avanzando
                if(not edge in visited):
                    self.findPaths(graph, edge, destination, path, visited)

        #Luego de encontrar el destino, se retrocede un paso para poder buscar mas posibles caminos
        path.pop()
        visited.pop()
    '''
'''
        currentVertex,s = self.vertices,{}
        current = currentVertex.first
        while(current):
            
            if(current.value.name == x):
                edge = current.value.edges
                current_edge = edge.first
                while(current_edge):
                    s["%s" % current_edge.value.name] = None
                    current_edge = current_edge.next
            
            if(current.value.edges.alreadyExist(vertex_x)):
                s["%s" % current.value.name] = None
            current = current.next
        return list(s.keys())
'''       
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