class Prim:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)

    def mst(self):
        selected = [False] * self.n
        selected[0] = True

        total = 0

        print("\nMinimum Spanning Tree:")

        for i in range(self.n - 1):

            minimum = 999
            x = 0
            y = 0

            for u in range(self.n):
                if selected[u]:

                    for v in range(self.n):
                        if not selected[v] and self.graph[u][v] != 0:

                            if self.graph[u][v] < minimum:
                                minimum = self.graph[u][v]
                                x = u
                                y = v

            print(x, "-", y, "=", minimum)

            selected[y] = True
            total += minimum

        print("Total Cost:", total)


graph = [
    [0, 10, 6, 5],
    [10, 0, 0, 15],
    [6, 0, 0, 4],
    [5, 15, 4, 0]
]

p = Prim(graph)
p.mst()