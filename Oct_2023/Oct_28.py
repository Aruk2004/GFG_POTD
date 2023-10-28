# Bleak Numbers

import math

class Solution:
    def is_bleak(self, n):
        for i in range(1, int(math.log2(n)) + 1):
            x = n - i
            set_bits = bin(x).count('1')
            if set_bits + x == n:
                return 0
        return 1

# Test the class and function
sol = Solution()

n = 4
result = sol.is_bleak(n)
print(result)  # Output: 1 (bleak)

n = 5
result = sol.is_bleak(n)
print(result)  # Output: 0 (not bleak)
