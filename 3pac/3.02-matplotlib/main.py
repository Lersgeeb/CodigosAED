from Graph import Graph
grafo = {"A":["B","C","D","E"],"B":["A","D","F"],"Z":[]}
grafo2 = {
    "A":["B","C","B","B"],
    "B":["A","C"],
    "C":["A","B","D"],
    "D":["C"]
}

g = Graph(grafo)
g.showGraph()