# Count number of substrings

class Solution:
    def countAtMostK(self, s, k):
        cnt = 0
        freq = [0] * 26
        i = 0
        diff = 0

        for j in range(len(s)):
            if freq[ord(s[j]) - ord('a')] == 0:
                diff += 1
            freq[ord(s[j]) - ord('a')] += 1

            while diff > k and i <= j:
                freq[ord(s[i]) - ord('a')] -= 1
                if freq[ord(s[i]) - ord('a')] == 0:
                    diff -= 1
                i += 1

            cnt += j - i + 1

        return cnt

    def substrCount(self, s, k):
        return self.countAtMostK(s, k) - self.countAtMostK(s, k - 1)

# Example usage:
s = "abcabc"
k = 2
sol = Solution()
result = sol.substrCount(s, k)
print(result)  # Output: 9
