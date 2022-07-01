# Depth First Search or DFS for a Graph
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # directed graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        # for undirected graph, add this line
        # self.graph[v].append(u)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self, v):
        visited = set()
        self.dfs_util(v, visited)

    # Adjacency list of all nodes.
    def show_graph(self, v):
        for i in range(v):
            print(i, end='')
            for j in self.graph[i]:
                print('->', j, end=' ')
            print()


g = Graph()
V = 8
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(3, 6)
g.add_edge(4, 6)
g.add_edge(4, 7)
g.add_edge(4, 5)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(5, 7)
g.add_edge(6, 7)
print('DFS traversal: ')
g.dfs(0)
print('\nAll connected nodes:')
g.show_graph(V)
