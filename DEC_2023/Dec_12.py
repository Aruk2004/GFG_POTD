# Gold Mine Problem

class Solution:
    def maxGold(self, n, m, M):
        dp = [[-1] * m for _ in range(n)]

        def traverse(i, j):
            if not (0 <= i < n and 0 <= j < m):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            out = M[i][j] + max(
                traverse(i - 1, j + 1),
                traverse(i, j + 1),
                traverse(i + 1, j + 1),
            )

            dp[i][j] = out
            return out

        result = 0
        for i in range(n):
            result = max(result, traverse(i, 0))

        return result

# Example usage:
n = 3
m = 4
M = [
    [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3]
]
solution = Solution()
result = solution.maxGold(n, m, M)
print(result)
