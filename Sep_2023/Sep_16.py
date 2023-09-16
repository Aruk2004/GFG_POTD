# Count no of hops

class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    def solve(self, n, i, dp):
        if i == n:
            return 1

        if dp[i] != -1:
            return dp[i]

        cnt = 0
        for d in range(1, 4):
            if i + d <= n:
                cnt = (cnt + self.solve(n, i + d, dp)) % self.mod

        dp[i] = cnt
        return dp[i]

    def countWays(self, n):
        dp = [-1] * n
        return self.solve(n, 0, dp)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    n = 5  # You can change this value to test different staircase heights
    ways = solution.countWays(n)
    print(f"Number of ways to climb {n} stairs: {ways}")
