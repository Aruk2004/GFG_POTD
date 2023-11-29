# Euler circuit and Path

from typing import List

class Solution:
    def isEulerCircuit(self, v: int, adj: List[List[int]]) -> int:
        even = 0
        odd = 0

        for i in range(v):
            if len(adj[i]) % 2 == 1:
                odd += 1
            else:
                even += 1

        return 2 if even == v else (1 if odd == 2 else 0)

# Example usage:
solution = Solution()
v = 4
adj = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}

result = solution.isEulerCircuit(v, adj)
print(result)
