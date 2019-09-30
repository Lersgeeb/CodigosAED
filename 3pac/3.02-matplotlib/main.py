from Graph import Graph
grafo = {"A":["B","C","D","E"],"B":["A","D","F"],"Z":[]}
grafo2 = {
    "A":["B","C","D"],
    "B":["A","C"],
    "C":["A","B","D"],
    "D":["C"]
}

g = Graph(grafo)
#g.showGraph()
print("Todos los posibles caminos entre A y D:\n")
g.findPaths(grafo2, "A", "D")