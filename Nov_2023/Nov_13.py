# Shortest Common Supersequence

class Solution:
    def LCS(self, X, Y, i, j, dp):
        if i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if X[i] == Y[j]:
            dp[i][j] = 1 + self.LCS(X, Y, i - 1, j - 1, dp)
            return dp[i][j]

        dp[i][j] = max(self.LCS(X, Y, i, j - 1, dp), self.LCS(X, Y, i - 1, j, dp))
        return dp[i][j]

    def shortestCommonSupersequence(self, X, Y, m, n):
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        lcs = self.LCS(X, Y, m - 1, n - 1, dp)
        return m + n - lcs

# Test the class and function
sol = Solution()
result = sol.shortestCommonSupersequence("ABCBDAB", "BDCAB", 7, 5)
print(result)  # Output: 9
