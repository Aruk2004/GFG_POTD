#Pascal Triangle

class Solution:
    mod = 10**9 + 7

    def nthRowOfPascalTriangle(self, n):
        out = [1] * n
        prev = [1] * n

        for i in range(1, n):
            for j in range(1, i):
                out[j] = (prev[j] + prev[j - 1]) % self.mod
            prev = out.copy()

        return out

# Example usage:
solution = Solution()
n = 5
result = solution.nthRowOfPascalTriangle(n)
print(result)
