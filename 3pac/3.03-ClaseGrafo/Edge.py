from LinkedList import LinkedList
class Edge:
    def __init__(self,vertexDestination,characteristic):
        self.name= vertexDestination
        self.weight = characteristic.getWeight()

    def __str__(self):
        return "vertice:%s, Peso:%s" % (self.name,self.weight)