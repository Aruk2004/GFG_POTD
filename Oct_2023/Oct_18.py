#Eventual Safe States

from collections import defaultdict

class Solution:
    def dfs(self, i, adj, vis, safe):
        if safe[i]:
            return True
        if vis[i]:
            return False
        vis[i] = True

        isSafe = True
        for edge in adj[i]:
            isSafe &= self.dfs(edge, adj, vis, safe)

        safe[i] = isSafe
        return isSafe

    def eventualSafeNodes(self, V, adj):
        safe = [False] * V
        vis = [False] * V

        for i in range(V):
            if not vis[i]:
                self.dfs(i, adj, vis, safe)

        out = []
        for i in range(V):
            if safe[i]:
                out.append(i)

        return out

# Example usage:
sol = Solution()
V = 5
adj = defaultdict(list)
adj[0] = [2, 3]
adj[1] = [4]
adj[2] = [3, 4]
adj[3] = [4]
adj[4] = []

result = sol.eventualSafeNodes(V, adj)
print("Eventual Safe Nodes:", result)  # Output: [0, 1, 2, 3, 4]
