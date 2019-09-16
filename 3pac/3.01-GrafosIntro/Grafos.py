class Graph:
    def __init__(self,json):
        self.json = json

    def getVertex(self, vertex):
        s = {}
        for k,v in self.json.items():
            if(k == vertex):
                for i in v:
                    s[i] = None
            elif(vertex in v):
                s[k] = None
        return s

g = {
    "A":["B","C","B","B"],
    "B":["A","C"],
    "C":["A","B","D"],
    "D":["C"]
}

x = "A"
print("EL grafo inicial: %s" % (g))

myGraph = Graph(g)
s = myGraph.getVertex(x)


print("los vertices conectados a %s son:  %s" % (x,list(s.keys())))
