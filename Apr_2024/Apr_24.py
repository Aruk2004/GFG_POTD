# Paths to reach origin

class Solution:
    def ways(self, n, m):
        mod = 10 ** 9 + 7
        x = min(n, m)
        num = n + m
        p = 1
        q = 1
        for i in range(1, x + 1):
            p *= num
            num -= 1
            q *= i
        return (p // q) % mod

sol = Solution()
n = 3
m = 2
print(sol.ways(n, m))  # Output: 10 (Number of ways to choose 3 elements from a set of 5 elements)
