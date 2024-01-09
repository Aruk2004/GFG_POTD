# Search Pattern (KMP-Algorithm)

class Solution:
    def getLSP(self, pat):
        sz, i = 0, 1
        lsp = [0] * len(pat)
        while i < len(pat):
            if pat[i] == pat[sz]:
                lsp[i] = sz + 1
                i += 1
                sz += 1
            elif sz == 0:
                lsp[i] = 0
                i += 1
            else:
                sz = lsp[sz - 1]
        return lsp

    def search(self, pat, txt):
        n, m = len(pat), len(txt)
        ls = self.getLSP(pat)
        ans = []

        i, j = 0, 0
        while i < m:
            if txt[i] == pat[j]:
                i += 1
                j += 1
            if j == n:
                ans.append(i - j + 1)
                j = ls[j - 1]
            elif i < m and txt[i] != pat[j]:
                if not j:
                    i += 1
                else:
                    j = ls[j - 1]
        return ans

# Example usage:
# Create an instance of the Solution class
sol = Solution()

# Call the search function with specific patterns and text
pattern = "abab"
text = "ababcabab"
result = sol.search(pattern, text)

# Print the result
print(result)

