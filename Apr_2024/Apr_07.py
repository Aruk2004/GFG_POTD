# Maximize dot product

class Solution:
	def maxDotProduct(self, n, m, a, b):
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(min(m, i+1)):
                dp[i+1][j+1] = max(dp[i][j] + a[i]*b[j], dp[i][j+1])

        return dp[n][m]

sol = Solution()
n = 3
m = 2
a = [2, 3, -2]
b = [1, 3]

result = sol.maxDotProduct(n, m, a, b)
print(result)  # Output: 13
