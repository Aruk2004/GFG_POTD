# Count possible ways to construct buildings

class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    def TotalWays(self, N):
        curr = prev = 1

        for i in range(1, N + 1):
            next_val = (curr + prev) % self.mod
            prev, curr = curr, next_val

        return (curr * curr) % self.mod

# Example usage:

sol = Solution()
result = sol.TotalWays(5)  
print(result)
