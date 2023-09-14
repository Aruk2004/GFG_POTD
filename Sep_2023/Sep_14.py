# Perfect Sum Problem

class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    def solve(self, arr, n, i, sum, dp):
        if sum == 0:
            return 1

        if i >= n:
            return 0

        if dp[i][sum] != -1:
            return dp[i][sum]

        t = 0
        nt = self.solve(arr, n, i + 1, sum, dp)

        if sum >= arr[i]:
            t = self.solve(arr, n, i + 1, sum - arr[i], dp)

        dp[i][sum] = (t + nt) % self.mod
        return dp[i][sum]

    def perfectSum(self, arr, n, sum):
        dp = [[-1 for _ in range(sum + 1)] for _ in range(n)]
        arr.sort()
        out = self.solve(arr, n, 0, sum, dp)
        return out

# Example usage:
arr = [1, 2, 3, 4, 5]
n = len(arr)
sum_value = 5
solution = Solution()
result = solution.perfectSum(arr, n, sum_value)
print(result)
