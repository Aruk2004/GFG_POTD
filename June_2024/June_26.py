# Coverage of all Zeros in a Binary Matrix

class Solution:
    def findCoverage(self, matrix):
        count, row, col = 0, len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j]:
                    count += int(-1 < i - 1 < row and not matrix[i - 1][j])
                    count += int(-1 < j - 1 < col and not matrix[i][j - 1])
                    count += int(-1 < i + 1 < row and not matrix[i + 1][j])
                    count += int(-1 < j + 1 < col and not matrix[i][j + 1])

        return count
