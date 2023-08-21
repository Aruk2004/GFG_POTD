#Number of occurrence in an Given Array

class Solution:
    def lower_bound(self, arr, n, x):
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if x <= arr[m]:
                r = m
            else:
                l = m + 1
        return l
    
    def upper_bound(self, arr, n, x):
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if x >= arr[m]:
                l = m + 1
            else:
                r = m
        if l < n and arr[l] <= x:
            l += 1
        return l
    
    def count(self, arr, n, x):
        start = self.lower_bound(arr, n, x)
        if arr[start] != x:
            return 0
        last = self.upper_bound(arr, n, x)
        return last - start

# Example usage
arr = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5]
x = 2
n = len(arr)
sol = Solution()
print(sol.count(arr, n, x))  # Output: 3 (x appears 3 times in the array)
