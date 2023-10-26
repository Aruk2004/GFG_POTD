# Minimum number of operations required to reach N starting from 0

class Solution:
    def minOperation(self, n):
        out = 0
        while n > 0:
            if n % 2 == 1:
                n -= 1
            else:
                n //= 2
            out += 1
        return out

# Example usage:
sol = Solution()
n = 15  # Replace with the integer you want to reduce to 0
result = sol.minOperation(n)
print("Minimum operations to reduce", n, "to 0:", result)
