"""
Count the number of trees in a forest

A forest is a collection of trees. Do a DFS. If any vertex if not reachable
from any other, then it means it is not a part of that subgraph (tree). Hence
it is a different tree, so increment the count
"""

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    
    def add_edge(self, u, v):
        self.graph[v].append(u)
        self.graph[u].append(v)


    def count_trees(self):
        visited = [False] * self.vertices
        count = 0

        for s in range(self.vertices):
            if not visited[s]:
                visited[s] = True
                stack = []
                stack.append(s)
                count += 1
                
                while stack:
                    print(stack)
                    s = stack.pop()

                    for i in self.graph[s]:
                        if not visited[i]:
                            visited[i] = True
                            stack.append(i)
                
        return count


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(3, 4)

print('Count of trees - ', g.count_trees())