# Party of Couples

from functools import reduce
class Solution:
    def findSingle(self, n, arr):
        return reduce(lambda x, y: x ^ y, arr, 0)

sol = Solution()
n = 7
arr = [2, 3, 5, 4, 5, 3, 4]

result = sol.findSingle(n, arr)
print(result)  # Output: 2
