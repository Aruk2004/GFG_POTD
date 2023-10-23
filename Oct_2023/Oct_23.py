# Maximum sum increasing subsequence
class Solution:
    def maxSumIS(self, arr, n):
        dp = list(arr)

        for i in range(1, n):
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j] + arr[i])

        out = 0
        for i in dp:
            out = max(out, i)
        return out

# Example usage:
sol = Solution()
arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)

result = sol.maxSumIS(arr, n)
print("Maximum sum of increasing subsequence:", result)  # Output: Maximum sum of increasing subsequence: 106
