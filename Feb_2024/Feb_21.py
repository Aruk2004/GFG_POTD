# Boolean Parenthesization

class Solution:
    def countWays(self, n, s):
        mod = 1003
        dp_true = [[0] * n for _ in range(n)]
        dp_false = [[0] * n for _ in range(n)]

        for i in range(n):
            if s[i] == 'T':
                dp_true[i][i] = 1
            else:
                dp_false[i][i] = 1

        for length in range(3, n + 1, 2):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i + 1, j, 2):
                    if s[k] == '|':
                        dp_true[i][j] += (dp_true[i][k - 1] * dp_false[k + 1][j] +
                                          dp_false[i][k - 1] * dp_true[k + 1][j] +
                                          dp_true[i][k - 1] * dp_true[k + 1][j]) % mod
                        dp_false[i][j] += (dp_false[i][k - 1] * dp_false[k + 1][j]) % mod
                    elif s[k] == '&':
                        dp_true[i][j] += (dp_true[i][k - 1] * dp_true[k + 1][j]) % mod
                        dp_false[i][j] += (dp_false[i][k - 1] * dp_true[k + 1][j] +
                                           dp_true[i][k - 1] * dp_false[k + 1][j] +
                                           dp_false[i][k - 1] * dp_false[k + 1][j]) % mod
                    elif s[k] == '^':
                        dp_true[i][j] += (dp_true[i][k - 1] * dp_false[k + 1][j] +
                                          dp_false[i][k - 1] * dp_true[k + 1][j]) % mod
                        dp_false[i][j] += (dp_true[i][k - 1] * dp_true[k + 1][j] +
                                           dp_false[i][k - 1] * dp_false[k + 1][j]) % mod

        return dp_true[0][n - 1] % mod


# Example usage
if __name__ == "__main__":
    sol = Solution()
    s = "T|T&F^T"
    n = len(s)
    print(sol.countWays(n, s))  # Output: 4

