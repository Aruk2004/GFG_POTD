# Frequencies of Limited Range Array Elements

class Solution:
    def frequencyCount(self, arr, N, P):
        offset = P + 1

        for i in arr:
            val = (i - 1) % offset
            if val < N:
                arr[val] += offset

        for i in range(N):
            arr[i] //= offset

# Example usage:
solution = Solution()
arr = [2, 3, 3, 2, 2]
N = 5
P = 3
solution.frequencyCount(arr, N, P)
print(arr)
