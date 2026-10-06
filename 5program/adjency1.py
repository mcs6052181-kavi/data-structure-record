class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for i in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def bfs(self, start):
        visited = [False] * self.vertices
        queue = [start]
        visited[start] = True

        print("BFS:", end=" ")

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for i in range(self.vertices):
                if self.graph[vertex][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)

    def dfs(self, start):
        visited = [False] * self.vertices

        print("DFS:", end=" ")
        self.dfs_helper(start, visited)

    def dfs_helper(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for i in range(self.vertices):
            if self.graph[vertex][i] == 1 and not visited[i]:
                self.dfs_helper(i, visited)


g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

print("Adjacency Matrix:")

for row in g.graph:
    print(row)

g.bfs(0)

print()
g.dfs(0)