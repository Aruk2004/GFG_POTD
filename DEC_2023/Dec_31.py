# New Year Resolution

class Solution:
    def solve(self, i, n, sum, coins, dp):
        if sum == 2024 or (sum and (sum % 20 == 0 or sum % 24 == 0)):
            return True

        if i == n or sum > 2024:
            return False

        if sum in dp[i]:
            return dp[i][sum]

        nt = self.solve(i + 1, n, sum, coins, dp)
        if nt:
            dp[i][sum] = nt
            return nt

        dp[i][sum] = self.solve(i + 1, n, sum + coins[i], coins, dp)
        return dp[i][sum]

    def isPossible(self, n, coins):
        dp = [{} for _ in range(n)]
        return self.solve(0, n, 0, coins, dp)


# Example usage:
n = 3
coins = [10, 12, 15]
sol = Solution()
result = sol.isPossible(n, coins)
print(result)
