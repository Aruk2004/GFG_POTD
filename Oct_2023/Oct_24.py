# Palindromic Partitioning

class Solution:
    def isPalin(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def check(self, i, j, s, dp):
        if i >= j:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        if self.isPalin(i, j, s):
            dp[i][j] = 0
            return 0
        
        out = float('inf')
        for k in range(i, j):
            if self.isPalin(i, k, s):
                out = min(out, 1 + self.check(k + 1, j, s, dp))
        
        dp[i][j] = out
        return out
    
    def palindromicPartition(self, s):
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        self.check(0, n - 1, s, dp)
        return self.check(0, n - 1, s, dp)

# Example usage:
sol = Solution()
str = "aab"
result = sol.palindromicPartition(str)
print("Minimum cuts to partition the string into palindromic substrings:", result)
