# Minimum Points To Reach Destination

class Solution:
    def minPoints(self, m, n, points):
        dp = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dp[i][j] = max(1, 1 - points[i][j])
                elif i == m - 1:
                    dp[i][j] = max(1, dp[i][j + 1] - points[i][j])
                elif j == n - 1:
                    dp[i][j] = max(1, dp[i + 1][j] - points[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - points[i][j])
        return dp[0][0]

sol = Solution()
m = 3
n = 3
points = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]

result = sol.minPoints(m, n, points)
print(result)  # Output: 7
