# Minimum distance between two numbers

class Solution:
    def minDist(self, a, n, x, y):
        lastX, lastY, out = -1, -1, float('inf')

        for i in range(n):
            if a[i] == x:
                lastX = i
            if a[i] == y:
                lastY = i

            if lastX != -1 and lastY != -1:
                out = min(out, abs(lastX - lastY))

        return -1 if out == float('inf') else out

# Example usage:
solution = Solution()
arr = [1, 2, 3, 4, 5, 6, 3, 7, 8]
n = len(arr)
x = 3
y = 8
result = solution.minDist(arr, n, x, y)
print(result)
