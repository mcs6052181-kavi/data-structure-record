class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = []
        queue = [start]

        while queue:
            vertex = queue.pop(0)

            if vertex not in visited:
                print(vertex, end=" ")
                visited.append(vertex)

                for neighbour in self.graph[vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour)

    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = []

        visited.append(vertex)
        print(vertex, end=" ")

        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)


g = Graph()

for i in range(5):
    g.add_vertex(i)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

print("Adjacency List:")
for vertex in g.graph:
    print(vertex, ":", g.graph[vertex])

print("\nBFS:", end=" ")
g.bfs(0)

print("\nDFS:", end=" ")
g.dfs(0)