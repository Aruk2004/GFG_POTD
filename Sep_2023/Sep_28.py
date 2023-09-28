# Wave Array

class Solution:
    def convertToWave(self, n, arr):
        for i in range(0, n - 1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Example usage:
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
sol = Solution()
sol.convertToWave(n, arr)
print(arr)  # Output: [2, 1, 4, 3, 6, 5]
