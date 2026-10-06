class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find_parent(self, parent, vertex):
        if parent[vertex] == vertex:
            return vertex

        return self.find_parent(parent, parent[vertex])

    def kruskal(self):
        self.edges.sort()

        parent = []

        for i in range(self.vertices):
            parent.append(i)

        mst = []
        total = 0

        for weight, u, v in self.edges:

            parent_u = self.find_parent(parent, u)
            parent_v = self.find_parent(parent, v)

            if parent_u != parent_v:

                mst.append((u, v, weight))
                total += weight

                parent[parent_v] = parent_u

        print("\nMinimum Spanning Tree:")
        print("Edge\tWeight")

        for u, v, weight in mst:
            print(u, "-", v, "\t", weight)

        print("Total Cost:", total)


n = int(input("Enter number of vertices: "))

g = Graph(n)

e = int(input("Enter number of edges: "))

for i in range(e):
    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))
    w = int(input("Enter weight: "))

    g.add_edge(u, v, w)

g.kruskal()