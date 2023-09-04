#Replace all 'O' with 'X' that are surrounded by 'X'

class Solution:
    def __init__(self):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def is_valid(self, ii, jj, n, m):
        return 0 <= ii < n and 0 <= jj < m

    def is_boundary(self, i, j, n, m):
        return i == 0 or j == 0 or i == n - 1 or j == m - 1

    def set_not_closed(self, i, j, n, m, mat):
        mat[i][j] = 'N'

        for d in range(4):
            ii = self.dx[d] + i
            jj = self.dy[d] + j
            if self.is_valid(ii, jj, n, m) and mat[ii][jj] == 'O':
                self.set_not_closed(ii, jj, n, m, mat)

    def fill(self, n, m, mat):
        for i in range(n):
            for j in range(m):
                if self.is_boundary(i, j, n, m) and mat[i][j] == 'O':
                    self.set_not_closed(i, j, n, m, mat)

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O':
                    mat[i][j] = 'X'
                elif mat[i][j] == 'N':
                    mat[i][j] = 'O'

        return mat

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    grid = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]

    n = len(grid)
    m = len(grid[0])

    result = solution.fill(n, m, grid)

    for row in result:
        print(" ".join(row))
