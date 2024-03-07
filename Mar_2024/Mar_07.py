# Longest repeating and non-overlapping substring

class Solution:
    def longestSubstring(self, s: str, n: int) -> str:
        nax = 0
        i = 0
        j = 0
        out = "-1"
        
        while i < n and j < n:
            substr = s[i:j + 1]
            
            if nax < len(substr) and s.find(substr, j + 1) != -1:
                nax = len(substr)
                out = substr
            else:
                i += 1
            
            j += 1
        
        return out

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    n = len(s)
    result = sol.longestSubstring(s, n)
    print(result)  # Output: "abc"
