# Find Transition Point

class Solution:
    def transitionPoint(self, arr, n):
        l = 0
        r = n - 1

        while l < r:
            m = (l + r) // 2

            if arr[m] < 1:
                l = m + 1
            else:
                r = m

        return l if arr[l] else -1

# Example usage:
solution = Solution()
arr = [0, 0, 0, 1, 1]
n = len(arr)
result = solution.transitionPoint(arr, n)
print(result)  # It will print the index of the transition point (in this case, 3)
