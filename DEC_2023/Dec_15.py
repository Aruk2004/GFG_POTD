# Reach the Nth point

class Solution:
    def nthPoint(self, n):
        a, b, mod = 1, 1, 10**9 + 7

        for i in range(1, n):
            c = (a + b) % mod
            a, b = b, c

        return b

# Example usage:
solution = Solution()
result = solution.nthPoint(5)  # Replace 5 with the desired value of n
print(result)
