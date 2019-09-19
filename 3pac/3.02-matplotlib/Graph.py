import networkx as nx
import matplotlib.pyplot as plt
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

    def showGraph(self):
        G = nx.Graph()
        for v,edges in self.json.items():
            G.add_node("%s" % (v))

            for e in edges:
                G.add_node("%s" % (e))
                G.add_edge("%s" % v,"%s" % e,weight=1)
                print("'%s' se conceta con '%s'" % (v,e))

        nx.draw(G,with_labels=True)
        plt.show()

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

