# Number of distinct subsequences

class Solution:
    def distinctSubsequences(self, s):
        mod = 10**9 + 7
        n = len(s)
        
        last = [-1] * 26
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] * 2
            lastOccur = last[ord(s[i - 1]) - ord('a')]
            
            if lastOccur != -1:
                dp[i] -= dp[lastOccur]
                if dp[i] < 0:
                    dp[i] += mod
            dp[i] %= mod
            last[ord(s[i - 1]) - ord('a')] = i - 1
        
        return dp[n]

# Example usage:
s = Solution()
input_string = "your_input_string_here"
result = s.distinctSubsequences(input_string)
print(result)
