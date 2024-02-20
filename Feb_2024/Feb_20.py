# Word Break

class Solution:
    def wordBreak(self, n, s, dictionary):
        # Complete this function
        nn=len(s)
        dp=[0]*(nn+1)
        dp[nn]=1
        for i in range(nn-1,-1,-1) :
            for w in dictionary :
                if i+len(w) <= nn and s[i:i+len(w)] == w :
                    dp[i]=dp[i+len(w)]
                if dp[i] :
                    break
        return dp[0]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    dictionary = ["leet", "code"]
    print(sol.wordBreak(len(s), s, dictionary))  # Output: True
