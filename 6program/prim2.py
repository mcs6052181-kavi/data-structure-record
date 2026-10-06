class Prim:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def find_mst(self):
        visited = [False] * self.vertices
        visited[0] = True

        mst = []
        total = 0

        while len(mst) < self.vertices - 1:

            minimum = 999
            selected_edge = None

            for u, v, weight in self.edges:

                if visited[u] and not visited[v]:
                    if weight < minimum:
                        minimum = weight
                        selected_edge = (u, v, weight)

                elif visited[v] and not visited[u]:
                    if weight < minimum:
                        minimum = weight
                        selected_edge = (u, v, weight)

            if selected_edge is None:
                break

            u, v, weight = selected_edge

            mst.append(selected_edge)
            total += weight

            visited[u] = True
            visited[v] = True

        print("\nMinimum Spanning Tree:")
        for u, v, weight in mst:
            print(u, "-", v, "=", weight)

        print("Total Cost:", total)


n = int(input("Enter number of vertices: "))

g = Prim(n)

e = int(input("Enter number of edges: "))

for i in range(e):
    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))
    w = int(input("Enter weight: "))

    g.add_edge(u, v, w)

g.find_mst()