# Sum of all substrings of a number

class Solution:
    def sumSubstrings(self, s):
        MOD = 10**9 + 7
        n = len(s)
        total_sum = 0

        multiplier = 1
        for i in range(n - 1, -1, -1):
            total_sum = (total_sum + int(s[i]) * multiplier * (i + 1)) % MOD
            multiplier = (multiplier * 10 + 1) % MOD

        return total_sum

# Example usage
solution = Solution()
s = "1234"
result = solution.sumSubstrings(s)
print("Sum of all substrings of", s, ":", result)  # Output: 1670
