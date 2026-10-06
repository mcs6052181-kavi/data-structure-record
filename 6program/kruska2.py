class Kruskal:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self):
        u = int(input("Enter first vertex: "))
        v = int(input("Enter second vertex: "))
        w = int(input("Enter weight: "))

        self.edges.append((w, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i

        return self.find(parent, parent[i])

    def create_mst(self):
        self.edges.sort()

        parent = list(range(self.vertices))

        total = 0
        count = 0

        print("\nMinimum Spanning Tree:")
        print("Edge\tWeight")

        for weight, u, v in self.edges:

            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:

                print(u, "-", v, "\t", weight)

                parent[root_v] = root_u

                total += weight
                count += 1

                if count == self.vertices - 1:
                    break

        print("Total Cost:", total)


n = int(input("Enter number of vertices: "))

g = Kruskal(n)

e = int(input("Enter number of edges: "))

for i in range(e):
    print("\nEdge", i + 1)
    g.add_edge()

g.create_mst()