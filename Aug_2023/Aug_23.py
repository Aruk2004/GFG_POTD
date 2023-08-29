#find String in Grid

class Solution:
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    def canForm(self, grid, word, i, j, dir):
        ii, jj = i, j
        for k in range(1, len(word)):
            ii = self.dx[dir] + ii
            jj = self.dy[dir] + jj
            if ii < 0 or jj < 0 or ii >= len(grid) or jj >= len(grid[0]) or grid[ii][jj] != word[k]:
                return False
        return True

    def searchWord(self, grid, word):
        out = []
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == word[0]:
                    for dir in range(8):
                        if self.canForm(grid, word, i, j, dir):
                            out.append([i, j])
                            break
        return out

# Example usage
grid = [['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']]

word = "ABCCED"
solution = Solution()
result = solution.searchWord(grid, word)
print(result)
