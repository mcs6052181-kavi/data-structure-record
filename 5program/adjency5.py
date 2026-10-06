class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        print("\nAdjacency List:")

        for i in range(self.vertices):
            print(i, ":", self.graph[i])

    def bfs(self, start):
        visited = [False] * self.vertices
        queue = [start]

        visited[start] = True

        print("BFS:", end=" ")

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbour in self.graph[vertex]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

    def dfs(self, start):
        visited = [False] * self.vertices

        print("DFS:", end=" ")
        self.dfs_helper(start, visited)

    def dfs_helper(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for neighbour in self.graph[vertex]:
            if not visited[neighbour]:
                self.dfs_helper(neighbour, visited)


n = int(input("Enter number of vertices: "))

g = Graph(n)

while True:

    print("\n--- GRAPH MENU ---")
    print("1. Add Edge")
    print("2. Display Graph")
    print("3. BFS")
    print("4. DFS")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        u = int(input("Enter first vertex: "))
        v = int(input("Enter second vertex: "))

        g.add_edge(u, v)
        print("Edge added.")

    elif choice == 2:
        g.display()

    elif choice == 3:
        start = int(input("Enter starting vertex: "))
        g.bfs(start)
        print()

    elif choice == 4:
        start = int(input("Enter starting vertex: "))
        g.dfs(start)
        print()

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")