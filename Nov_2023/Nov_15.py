# Better String

class Solution:
    def betterString(self, str1, str2):
        def countDistinctSubsequences(s):
            mod = 10**9 + 7
            n = len(s)
            last_occurrence = [-1] * 256
            dp = [0] * (n + 1)
            dp[0] = 1
    
            for i in range(1, n + 1):
                dp[i] = (2 * dp[i - 1]) % mod
    
                if last_occurrence[ord(s[i - 1])] != -1:
                    dp[i] = (dp[i] - dp[last_occurrence[ord(s[i - 1])]]) % mod
    
                last_occurrence[ord(s[i - 1])] = i - 1
    
            return (dp[n] - 1 + mod) % mod
    
        count1 = countDistinctSubsequences(str1)
        count2 = countDistinctSubsequences(str2)
    
        return str1 if count1 >= count2 else str2

# Example usage:
solution_instance = Solution()
result = solution_instance.betterString("abc", "ab")
print(result)
