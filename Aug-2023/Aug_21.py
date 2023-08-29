#Surrounded 1's in an Given Matrix

class Solution:
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    def isValid(self, ii, jj, n, m):
        return 0 <= ii < n and 0 <= jj < m

    def Count(self, mat):
        cnt = 0
        n = len(mat)
        m = len(mat[0])

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    c = 0
                    for k in range(8):
                        ii = self.dx[k] + i
                        jj = self.dy[k] + j
                        if self.isValid(ii, jj, n, m) and mat[ii][jj] == 0:
                            c += 1
                    if c and c % 2 == 0:
                        cnt += 1

        return cnt

# Example usage
mat = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]

solution = Solution()
result = solution.Count(mat)
print(result)  # This will output the count of cells meeting the criteria
