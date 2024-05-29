# Geek and its Game of Coins

class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
        dp = [0] * (n + 1)
        if n >= 1:
            dp[1] = 1

        for i in range(2, n + 1):
            if i - 1 >= 0 and dp[i - 1] == 0:
                dp[i] = 1
            elif i - x >= 0 and dp[i - x] == 0:
                dp[i] = 1
            elif i - y >= 0 and dp[i - y] == 0:
                dp[i] = 1

        return dp[n]
