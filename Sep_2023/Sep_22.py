# First and last occurrences of x

class Solution:
    def lower_bound(self, arr, n, x):
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] >= x:
                r = m
            else:
                l = m + 1
        return l

    def upper_bound(self, arr, n, x):
        l, r = 0, n
        while l < r:
            m = (l + r) // 2
            if arr[m] > x:
                r = m
            else:
                l = m + 1
        return r - 1

    def find(self, arr, n, x):
        first_occur = self.lower_bound(arr, n, x)
        if first_occur < n and arr[first_occur] == x:
            last_occur = self.upper_bound(arr, n, x)
            return [first_occur, last_occur]
        else:
            return [-1, -1]

# Example usage:
arr = [1, 2, 2, 2, 3, 4, 5]
x = 2
n = len(arr)
sol = Solution()
result = sol.find(arr, n, x)
print(result)  # Output: [1, 3]
