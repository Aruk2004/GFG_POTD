# Check whether K-th bit is set or not

class Solution:
    def checkKthBit(self, n, k):
        mask = 1 << k
        return (n & mask) > 0

# Test the class and function
sol = Solution()

n = 5  # Binary: 101
k = 2  # Checking the 2nd bit from the right (0-based index)
result = sol.checkKthBit(n, k)
print(result)  # Output: True

n = 5  # Binary: 101
k = 1  # Checking the 1st bit from the right (0-based index)
result = sol.checkKthBit(n, k)
print(result)  # Output: False
