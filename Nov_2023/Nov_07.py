# Sum of upper and lower triangles

class Solution:
    def sumTriangles(self, matrix, n):
        upper_triangle_sum = sum(matrix[i][j] for i in range(n) for j in range(i, n))
        lower_triangle_sum = sum(matrix[i][j] for i in range(n) for j in range(i + 1))

        return [upper_triangle_sum, lower_triangle_sum]

# Example usage:
solution = Solution()
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
n = 3
result = solution.sumTriangles(matrix, n)
print(result)  # It will print the sums of upper and lower triangles of the matrix
