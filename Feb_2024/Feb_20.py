# Word Break

class Solution:
    def wordBreak(self, n, s, dictionary):
        # Create a set for faster lookup
        dictionary_set = set(dictionary)
        
        # Initialize a boolean array to track if substrings from 0 to i can be segmented
        dp = [False] * (n + 1)
        dp[0] = True
        
        # Iterate through the string
        for i in range(1, n + 1):
            # Check if the substring from 0 to i can be segmented
            for j in range(i):
                if dp[j] and s[j:i] in dictionary_set:
                    dp[i] = True
                    break
        
        # Return True if the entire string can be segmented
        return dp[n]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    dictionary = ["leet", "code"]
    print(sol.wordBreak(len(s), s, dictionary))  # Output: True
