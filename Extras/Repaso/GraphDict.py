import networkx as nx 
import matplotlib.pyplot as plt
class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self,vertexName):
        self.graph["%s" % vertexName] = []
    
    def addEdge(self,fromVertex,toVertex):
        if(not toVertex in self.graph[fromVertex]):
            self.graph[fromVertex].append(toVertex)

    def connectedVertices(self,x):
        s = {}
        for k,v in self.graph.items():
            if(k==x):
                for edge in v:
                    s[edge] = None
            elif(x in v):
                s[k] = None
        return s

    def findPath(self,fromVertex,toVertex):
        paths = []
        self.findPathInner(fromVertex,toVertex,paths)
        return paths

    def findPathInner(self,fromVertex,toVertex,paths = [],visited = [],):
        visited.append(fromVertex)
        if(not fromVertex == toVertex):
            for edge in self.graph[fromVertex]:
                if(not edge in visited):
                    self.findPathInner(edge,toVertex,paths,visited)
        else:
            paths.append(visited.copy())
        visited.pop()
        
    def showGraph(self):
        g = nx.DiGraph()
        graph = self.graph
        for vertex,edges in graph.items():
            g.add_node(vertex)
            for edge in edges:
                g.add_edge(vertex,edge,weigth = 1)
        pos = nx.circular_layout(g)
        nx.draw(g,pos,with_labels=True)
        plt.show()

        
    
        


g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addEdge("A","B")
g.addEdge("A","C")
g.addEdge("B","C")
g.addEdge("B","D")
g.addEdge("A","D")
g.addEdge("D","A")
g.addEdge("C","B")
g.addVertex("E")
g.addVertex("F")
g.addEdge("E","F")
g.addEdge("F","D")
g.addEdge("A","E")


x = "A"
print("the graph: %s"%(g.graph))
print("the connections to the vertex '%s' are: %s"%(x,g.connectedVertices(x)))

print(g.findPath("A","D"))
g.showGraph()