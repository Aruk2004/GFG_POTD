# Print Matrix in snake Pattern

class Solution:
    def snakePattern(self, matrix):
        out = []
        for i, row in enumerate(matrix):
            if i % 2 == 0:
                out.extend(row)
            else:
                out.extend(row[::-1])
        return out

# Example usage:
solution = Solution()
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
result = solution.snakePattern(matrix)
print(result)  # It will print the snake pattern of the matrix
