# Smallest window in a string containing all the characters of another string

from collections import Counter

class Solution:
    
    # Function to find the smallest window in the string s consisting
    # of all the characters of string p.
    def smallestWindow(self, s, p):
        if not s or not p:
            return "-1"

        p_count = Counter(p)
        s_count = Counter()

        required = len(p_count)
        formed = 0
        l, r = 0, 0
        min_len = float('inf')
        min_left = 0

        while r < len(s):
            char = s[r]
            s_count[char] += 1
            
            # Check if this character's count matches with that in p
            if char in p_count and s_count[char] == p_count[char]:
                formed += 1
            
            # Try to contract the window until it ceases to be 'desirable'
            while l <= r and formed == required:
                char = s[l]
                
                # Update the minimum window if this one is smaller
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_left = l
                
                # Remove the leftmost character from the window
                s_count[char] -= 1
                if char in p_count and s_count[char] < p_count[char]:
                    formed -= 1
                
                l += 1
            
            r += 1

        # If min_len was updated, return the smallest window; otherwise, return "-1"
        if min_len == float('inf'):
            return "-1"
        else:
            return s[min_left:min_left + min_len]

# Example usage:
sol = Solution()
print(sol.smallestWindow("timetopractice", "toc"))  # Output: "toprac"
print(sol.smallestWindow("zoomlazapzo", "oza"))     # Output: "apzo"
