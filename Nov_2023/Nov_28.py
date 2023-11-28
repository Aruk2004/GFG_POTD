# Sum of dependencies in a graph

from typing import List

class Solution:
    def sumOfDependencies(self, adj: List[List[int]], V: int) -> int:
        sum = 0
        for i in range(V):
            sum += len(adj[i])
        return sum

# Example usage:
solution = Solution()
V = 4
adj = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}

result = solution.sumOfDependencies(adj, V)
print(result)
