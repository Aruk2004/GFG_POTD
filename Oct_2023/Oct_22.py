# Number of paths

class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    def modInv(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return (x1 + m0) % m0

    def numberOfPaths(self, m, n):
        out = 1

        for i in range(m - 1):
            inverse = self.modInv(i + 1, self.mod)
            out = (out * (i + n)) % self.mod
            out = (out * inverse) % self.mod

        return out

# Example usage:
sol = Solution()
m = 3
n = 3

result = sol.numberOfPaths(m, n)
print("Number of paths in a", m, "x", n, "grid:", result)  # Output: Number of paths in a 3 x 3 grid: 6
