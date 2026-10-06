class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[0] * n for i in range(n)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def bfs(self, start):
        visited = [False] * self.n
        queue = [start]
        visited[start] = True

        print("BFS:", end=" ")

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for i in range(self.n):
                if self.graph[vertex][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)

    def dfs(self, start):
        visited = [False] * self.n

        print("DFS:", end=" ")
        self.dfs_visit(start, visited)

    def dfs_visit(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for i in range(self.n):
            if self.graph[vertex][i] == 1 and not visited[i]:
                self.dfs_visit(i, visited)


n = int(input("Enter number of vertices: "))

g = Graph(n)

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))
    g.add_edge(u, v)

print("\nAdjacency Matrix:")

for row in g.graph:
    print(row)

start = int(input("\nEnter starting vertex: "))

g.bfs(start)

print()
g.dfs(start)