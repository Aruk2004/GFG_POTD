# Boolean Matrix

class Solution:
    def booleanMatrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        rows_to_update = [False] * n
        cols_to_update = [False] * m

        # Find rows and columns that need to be updated
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    rows_to_update[i] = True
                    cols_to_update[j] = True

        # Update the matrix based on rows_to_update and cols_to_update
        for i in range(n):
            if rows_to_update[i]:
                for j in range(m):
                    matrix[i][j] = 1

        for j in range(m):
            if cols_to_update[j]:
                for i in range(n):
                    matrix[i][j] = 1

# Example usage:
matrix = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]

sol = Solution()
sol.booleanMatrix(matrix)

# Print the updated matrix
for row in matrix:
    print(row)
