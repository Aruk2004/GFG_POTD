# How Many X's?

class Solution:
    def cntX(self, n, X, cnt):
        while n:
            if n % 10 == X:
                cnt[0] += 1
            n //= 10

    def countX(self, L, R, X):
        cnt = [0]

        for i in range(L + 1, R):
            self.cntX(i, X, cnt)

        return cnt[0]

# Example usage:
solution = Solution()
L = 10
R = 30
X = 2
result = solution.countX(L, R, X)
print(result)  # Output: 10
