# Making A Large Island

from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]) -> int:
        def dfs(i, j, id):
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = id
                size = 1
                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    size += dfs(i + x, j + y, id)
                return size
            return 0

        n = len(grid)
        island_size = {}
        id = 2
        max_size = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, id)
                    max_size = max(max_size, size)
                    island_size[id] = size
                    id += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    adjacent_islands = set()
                    for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        ni, nj = i + x, j + y
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            adjacent_islands.add(grid[ni][nj])
                    total_size = 1 + sum(island_size[i] for i in adjacent_islands)
                    max_size = max(max_size, total_size)

        return max_size

# Example usage:
grid = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
solution = Solution()
result = solution.largestIsland(grid)
print(result)  # Print the result
