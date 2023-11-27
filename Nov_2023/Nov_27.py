# Detect Cycle using DSU

from typing import List, Set

class Solution:
    def __init__(self):
        self.dsu = []
        self.vis = []
        self.g = []

    def findDSU(self, p):
        if self.dsu[p] < 0:
            return p
        self.dsu[p] = self.findDSU(self.dsu[p])
        return self.dsu[p]

    def merge(self, x, y):
        if self.dsu[x] > self.dsu[y]:
            x, y = y, x

        self.dsu[x] += self.dsu[y]
        self.dsu[y] = x

    def dfs(self, node, par):
        isCycle = 0
        self.vis[node] = 1

        for child in self.g[node]:
            if child != par:
                x = self.findDSU(node)
                y = self.findDSU(child)

                if x == y:
                    return 1

                self.merge(x, y)
                isCycle = isCycle or self.dfs(child, node)

        return isCycle

    def detectCycle(self, V, adj):
        self.dsu = [-1] * V
        self.vis = [0] * V
        self.g = [set() for _ in range(V)]

        for i in range(V):
            for x in adj[i]:
                self.g[i].add(x)

        isCycle = 0

        for i in range(V):
            if not self.vis[i]:
                isCycle = isCycle or self.dfs(i, -1)

        return isCycle

# Example usage:
solution = Solution()
V = 4
adj = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}

if solution.detectCycle(V, adj):
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")
