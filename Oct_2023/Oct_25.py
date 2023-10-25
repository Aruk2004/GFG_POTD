# Knapsack with Duplicate Items

class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [0] * (W + 1)
        for i in range(N):
            for w in range(W, wt[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - wt[i]] + val[i])
        return dp[W]

# Example usage:
sol = Solution()
N = 3  # Number of items
W = 50  # Knapsack capacity
val = [60, 100, 120]  # Values of items
wt = [10, 20, 30]  # Weights of items

result = sol.knapSack(N, W, val, wt)
print("Maximum value that can be obtained:", result)
