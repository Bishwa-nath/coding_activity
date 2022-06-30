# Breadth First Search or BFS for a Graph
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Direct Graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)

    def show_graph(self, v):
        for i in range(v):
            print(i, end='')
            for j in self.graph[i]:
                print('->', j, end=' ')
            print()

    def bfs(self, s):
        visited = [False] * (max(self.graph)+1)
        queue = []
        visited[s] = True
        queue.append(s)
        print("BFS traversal: ", end='')
        while queue:
            s = queue.pop(0)
            print(s, end=' ')
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


g = Graph()
V = 9
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(1, 5)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(3, 4)
g.add_edge(4, 8)
g.add_edge(5, 8)
g.add_edge(6, 7)
g.add_edge(7, 5)

g.show_graph(V)
g.bfs(0)
