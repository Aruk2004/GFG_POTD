# Check if a given graph is tree or not

from typing import List

class Solution:
    def dfs(self, s, graph, vis):
        vis[s] = 1
        for i in graph[s]:
            if not vis[i]:
                self.dfs(i, graph, vis)

    def isTree(self, n, m, adj):
        if (n - m) != 1:
            return 0

        vis = [0] * n
        graph = [[] for _ in range(n)]

        for i in adj:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        self.dfs(0, graph, vis)

        for i in vis:
            if not i:
                return 0

        return 1

# Example usage:
solution = Solution()
n = 5
m = 4
adjacency_list = [[0, 1], [0, 2], [0, 3], [1, 4]]
result = solution.isTree(n, m, adjacency_list)

# Print the result
print(result)
