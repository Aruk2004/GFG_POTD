# Anti Diagonal Traversal of Matrix

class Solution:
    def fill(self, i, j, mat, out):
        while i < len(mat) and j >= 0:
            out.append(mat[i][j])
            i += 1
            j -= 1

    def antiDiagonalPattern(self, mat):
        out = []
        n = len(mat)
        for j in range(n):
            self.fill(0, j, mat, out)

        for i in range(1, n):
            self.fill(i, n - 1, mat, out)

        return out

# Example usage:
solution_instance = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = solution_instance.antiDiagonalPattern(matrix)
print(result)
