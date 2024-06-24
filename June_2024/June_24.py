# Summed Matrix

class Solution:
    def sumMatrix(self, n, q):
        # Number of valid pairs (i, j) such that 1 <= i <= n and 1 <= j <= n
        if q < 2 or q > 2 * n:
            return 0
        else:
            return min(q - 1, 2 * n - q + 1)
