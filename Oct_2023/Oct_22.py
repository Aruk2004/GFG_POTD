# Sum of all divisors from 1 to n

class Solution:
    def sumOfDivisors(self, N):
        out = 0
        for i in range(1, N + 1):
            out += (N // i) * i
        return out

# Example usage:
sol = Solution()
N = 6

result = sol.sumOfDivisors(N)
print("Sum of divisors of", N, "is:", result)  # Output: Sum of divisors of 6 is: 12
