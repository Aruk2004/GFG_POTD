# Count ways to N'th Stair

class Solution:
    def countWays(self, n):
        mod = 1000000007
        return (1+(n//2))

sol = Solution()
n = 10
result = sol.countWays(n)
print(result)  # Output: 6
