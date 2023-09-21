# Stickler Theif

class Solution:
    def FindMaxSum(self, arr, n):
        dp = [0] * n
        out = 0
        
        for i in range(n):
            if i >= 2:
                dp[i] = dp[i - 2]
            if i >= 3:
                dp[i] = max(dp[i], dp[i - 3])

            dp[i] += arr[i]
            out = max(out, dp[i])
        
        return out

# Example usage:
# Create an instance of the Solution class
solution = Solution()
# Input array
arr = [1, 2, 3, 4, 5]
# Array length
n = len(arr)
# Call the FindMaxSum method
result = solution.FindMaxSum(arr, n)
# Print the result
print(result)
