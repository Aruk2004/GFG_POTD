# Determinant of a Matrix

class Solution:
    def determinantOfMatrix(self, mat, n):
        if n == 1:
            return mat[0][0]
        if n == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

        sign = 1
        ans = 0
        m = [[0] * (n - 1) for _ in range(n - 1)]

        for row in range(n):
            k = 0
            for i in range(n):
                if i != row:
                    for j in range(1, n):
                        m[k][j - 1] = mat[i][j]
                    k += 1

            ans += sign * (mat[row][0]) * self.determinantOfMatrix(m, n - 1)
            sign *= -1

        return ans

# Example usage:
solution_instance = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = 3
result = solution_instance.determinantOfMatrix(mat, n)
print(result)
