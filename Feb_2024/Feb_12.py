# Recursive sequence

class Solution:
    def sequence(self, n):
        mod = 10**9 + 7
        out = 0
        c = 1
        for i in range(1, n + 1):
            temp = 1
            for j in range(i):
                temp *= c
                temp %= mod
                c += 1
            out = (out + temp) % mod
        return out

# Example usage:
sol = Solution()
n = 5
print(sol.sequence(n))  # Output: 65
