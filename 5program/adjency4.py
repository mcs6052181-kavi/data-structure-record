class Graph:
    def __init__(self, vertices):
        self.graph = {}

        for i in range(vertices):
            self.graph[i] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = [start]

        print("BFS:", end=" ")

        while queue:
            vertex = queue.pop(0)

            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)

                for neighbour in self.graph[vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for neighbour in self.graph[start]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)


n = int(input("Enter number of vertices: "))

g = Graph(n)

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))

    g.add_edge(u, v)

print("\nAdjacency List:")

for vertex in g.graph:
    print(vertex, ":", g.graph[vertex])

start = int(input("\nEnter starting vertex: "))

g.bfs(start)

print()
g.dfs(start)