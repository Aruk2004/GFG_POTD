#Longest K unique characters substring

class Solution:
    def longestKSubstr(self, s, k):
        cnt = {}
        i = 0
        n = len(s)
        c = 0
        out = -1

        for j in range(n):
            if s[j] not in cnt or cnt[s[j]] == 0:
                c += 1
        
            if s[j] not in cnt:
                cnt[s[j]] = 1
            else:
                cnt[s[j]] += 1

            while c > k and i < j:
                cnt[s[i]] -= 1
                if cnt[s[i]] == 0:
                    c -= 1
                i += 1

            if c == k:
                out = max(out, j - i + 1)

        return out

# Create an instance of the Solution class
solution = Solution()
# Call the longestKSubstr method with appropriate arguments
result = solution.longestKSubstr("aabbcc", 2)
print(result)  # Output should be 4
