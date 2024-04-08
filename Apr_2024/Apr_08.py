# Optimal Strategy For A Game

class Solution:
    def optimalStrategyOfGame(self, n, arr):
        # Initialize a 2D table to store the maximum amount of money
        dp = [[0] * n for _ in range(n)]

        # Fill the diagonal elements with the coin values
        for i in range(n):
            dp[i][i] = arr[i]

        # Fill the table diagonally
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                x = 0
                if i + 2 <= j:
                    x = dp[i + 2][j]
                y = 0
                if i + 1 <= j - 1:
                    y = dp[i + 1][j - 1]
                z = 0
                if i <= j - 2:
                    z = dp[i][j - 2]
                dp[i][j] = max(arr[i] + min(x, y),
                               arr[j] + min(y, z))

        # The maximum amount the first player can win will be stored in dp[0][n-1]
        return dp[0][n - 1]

sol = Solution()
n = 4
arr = [3, 9, 1, 2]

result = sol.optimalStrategyOfGame(n, arr)
print(result)  # Output: 11
