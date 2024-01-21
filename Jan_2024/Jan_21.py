# Vertex Cover

from typing import List

class Solution:
    def solve(self, i, bits, n, m, edges, out):
        if i > n:
            for i in range(m):
                if not (bits & (1 << (edges[i][0] - 1)) or bits & (1 << (edges[i][1] - 1))):
                    return
            out[0] = min(out[0], bin(bits).count('1'))
            return

        self.solve(i + 1, bits, n, m, edges, out)
        self.solve(i + 1, bits | (1 << (i - 1)), n, m, edges, out)

    def vertexCover(self, n: int, edges: List[List[int]]) -> int:
        out = [float('inf')]
        m = len(edges)
        self.solve(1, 0, n, m, edges, out)
        return out[0]

# Example usage:
sol = Solution()
n = 4
edges = [[1, 2], [2, 3], [3, 4]]
result = sol.vertexCover(n, edges)
print("Minimum Vertex Cover Size:", result)
