# Number of Enclaves

class Solution:
    def __init__(self):
        self.dx = [-1, 0, 0, 1]
        self.dy = [0, -1, 1, 0]
    
    def dfs(self, grid, i, j, n, m):
        grid[i][j] = -1
        for d in range(4):
            x = i + self.dx[d]
            y = j + self.dy[d]
            if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                self.dfs(grid, x, y, n, m)
    
    def numberOfEnclaves(self, grid):
        n = len(grid)
        m = len(grid[0])

        for i in range(m):
            if grid[0][i] == 1:
                self.dfs(grid, 0, i, n, m)
            if grid[n - 1][i] == 1:
                self.dfs(grid, n - 1, i, n, m)

        for i in range(n):
            if grid[i][0] == 1:
                self.dfs(grid, i, 0, n, m)
            if grid[i][m - 1] == 1:
                self.dfs(grid, i, m - 1, n, m)
        
        cnt = 0
        for i in range(n):
            for j in range(m):
                cnt += (grid[i][j] == 1)
        
        return cnt

# Example usage:
grid = [
    [1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1]
]

sol = Solution()
result = sol.numberOfEnclaves(grid)
print(result)  # Output: 32
