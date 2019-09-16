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

