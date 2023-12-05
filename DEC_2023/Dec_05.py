# Minimize the Heights II

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        out = arr[n - 1] - arr[0]

        for i in range(n - 1):
            if arr[i + 1] - k >= 0:
                nax = max(arr[i] + k, arr[n - 1] - k)
                nin = min(arr[i + 1] - k, arr[0] + k)
                out = min(out, nax - nin)

        return out

# Example usage:
solution = Solution()
arr = [1, 5, 8, 10]
n = len(arr)
k = 2
result = solution.getMinDiff(arr, n, k)
print(result)  # Output: 5
