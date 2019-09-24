class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self,vertex_name):
        self.graph["%s" % (vertex_name)] = []
    
    def add_edges(self,vertex_origin,vertex_destination):
        if not (vertex_destination in self.graph["%s" % (vertex_origin)]):
            self.graph["%s" % (vertex_origin)].append(vertex_destination)
        

    def connectedVertices(self,x):
        s = {}
        graph = self.graph
        for k,v in graph.items():
            if k == x:
                for i in v:
                    s[i] = None
            elif x in v:
                s[k] = None
        return s.keys()


#g = Graph({"A":["B"],"B":[],"C":[],"D":[]})
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edges("A","B")
g.add_edges("A","C")
g.add_edges("D","A")
x = "A"
print("the graph: %s"%(g.graph))
print("the connections to the vertex '%s' are: %s"%(x,g.connectedVertices(x)))