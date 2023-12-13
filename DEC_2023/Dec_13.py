# Consecutive 1's not allowed

class Solution:
    def countStrings(self, n):
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % mod

        return dp[n]

# Example usage:
solution = Solution()
result = solution.countStrings(5)  # Replace 5 with the desired value of n
print(result)
