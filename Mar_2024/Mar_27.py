# Find shortest safe route in a matrix

from typing import List
from collections import deque

class Solution:
    def findShortestPath(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return -1

        n, m = len(mat), len(mat[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  
        def is_blocked(x, y):
            if mat[x][y] == 0:
                return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 0:
                    return True
            return False

        queue = deque([(i, 0, 1) for i in range(n) if not is_blocked(i, 0)])
        vis = [[False for _ in range(m)] for _ in range(n)]  # Visited matrix

        while queue:
            x, y, dist = queue.popleft()
            if y == m - 1:
                return dist
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and not is_blocked(nx, ny):
                    vis[nx][ny] = True  
                    queue.append((nx, ny, dist + 1))

        return -1

solution = Solution()
matrix = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]
]

result = solution.findShortestPath(matrix)
print("Shortest safe path length:", result)
