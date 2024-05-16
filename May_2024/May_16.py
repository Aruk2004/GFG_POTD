# Divisibility tree

from typing import List

class Solution:
    def dfs(self, adj: List[List[int]], u: int, prt: int, ans: List[int]) -> int:
        count = 0
        for v in adj[u]:
            if v != prt:
                x = self.dfs(adj, v, u, ans)
                if x % 2 == 0:
                    ans[0] += 1
                else:
                    count += x
        return count + 1

    def minimumEdgeRemove(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[1] - 1].append(edge[0] - 1)
            adj[edge[0] - 1].append(edge[1] - 1)

        ans = [0]
        self.dfs(adj, 0, -1, ans)
        return ans[0]

# Example usage
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()

    # Define the number of vertices and edges
    n = 5
    edges = [[1, 2], [2, 3], [3, 4], [4, 5]]

    # Calculate the minimum number of edge removals
    result = solution.minimumEdgeRemove(n, edges)

    # Print the result
    print("Minimum number of edge removals:", result)
