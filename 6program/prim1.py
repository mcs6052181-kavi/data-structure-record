class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for i in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def prim(self):
        selected = [False] * self.vertices
        selected[0] = True

        total = 0

        print("\nMinimum Spanning Tree:")
        print("Edge\tWeight")

        for i in range(self.vertices - 1):

            minimum = 999
            x = 0
            y = 0

            for u in range(self.vertices):
                if selected[u]:

                    for v in range(self.vertices):
                        if not selected[v] and self.graph[u][v] != 0:
                            if self.graph[u][v] < minimum:
                                minimum = self.graph[u][v]
                                x = u
                                y = v

            print(x, "-", y, "\t", minimum)

            selected[y] = True
            total += minimum

        print("Total Cost:", total)


n = int(input("Enter number of vertices: "))

g = Graph(n)

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))
    w = int(input("Enter weight: "))

    g.add_edge(u, v, w)

g.prim()