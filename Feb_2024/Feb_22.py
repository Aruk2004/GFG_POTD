# Distinct occurrences

class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    def sequenceCount(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        # Initialize an array to store counts of subsequences for each character of t
        dp = [0] * (m + 1)
        dp[0] = 1  # Base case: when t is empty, there is only one way to choose elements from s.

        # Dynamic programming to fill the dp array
        for char in s:
            for j in range(m - 1, -1, -1):
                if char == t[j]:
                    dp[j + 1] = (dp[j] + dp[j + 1]) % self.mod

        return dp[m]

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    s = "abcab"
    t = "ab"
    print(sol.sequenceCount(s, t))  # Output: 10
