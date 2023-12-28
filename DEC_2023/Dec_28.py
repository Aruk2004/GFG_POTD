# Wildcard string matching

class Solution:
    def solve(self, i, j, w, p, dp):
        if i == len(w):
            return j == len(p)

        if j == len(p):
            return w[i] == '*' and self.solve(i + 1, j, w, p, dp)

        if dp[i][j] != -1:
            return dp[i][j]

        ans = False

        if w[i] == p[j] or w[i] == '?':
            ans = self.solve(i + 1, j + 1, w, p, dp)
        elif w[i] == '*':
            ans = self.solve(i, j + 1, w, p, dp) or self.solve(i + 1, j, w, p, dp)

        dp[i][j] = ans
        return ans

    def match(self, w, p):
        dp = [[-1] * len(p) for _ in range(len(w))]
        return self.solve(0, 0, w, p, dp)

# Example usage:
solution_instance = Solution()
wildcard_pattern = "ab*c?d"
string_to_match = "abcd"
result = solution_instance.match(wildcard_pattern, string_to_match)
print(result)
