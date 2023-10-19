# Level of Nodes

from collections import deque

class Solution:
    def nodeLevel(self, V, adj, X):
        visited = [False] * V
        level = [0] * V

        q = deque()
        q.append(0)
        visited[0] = True

        while q:
            current = q.popleft()

            for neighbor in adj[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    level[neighbor] = level[current] + 1
                    q.append(neighbor)

        if visited[X]:
            return level[X]
        else:
            return -1

# Example usage:
sol = Solution()
V = 6
adj = [[] for _ in range(V)]
adj[0] = [1, 2]
adj[1] = [3, 4]
adj[2] = [5]
adj[3] = []
adj[4] = []
adj[5] = []

X = 4

result = sol.nodeLevel(V, adj, X)
print(f"Level of node {X}:", result)  # Output: Level of node 4: 2
