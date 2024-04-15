# Count the elements

from bisect import bisect_right

class Solution:
    def countElements(self, a, b, n, query, q):
        b.sort()
        return [bisect_right(b, a[q]) for q in query]

# Example usage
sol = Solution()
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
n = 5
query = [1, 3]
q = 1
result = sol.countElements(a, b, n, query, q)
print(result)  # Output: [2, 4]
