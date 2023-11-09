# Column with Max no of 0s

class Solution:
    def columnWithMaxZeros(self, arr, n):
        max_zeros = 0
        column_idx = -1

        for j in range(n):
            zeros_count = sum(1 for i in range(n) if arr[i][j] == 0)

            if zeros_count > max_zeros:
                max_zeros = zeros_count
                column_idx = j

        return column_idx

# Example usage:
solution = Solution()
matrix = [[1, 0, 1],
          [0, 0, 1],
          [1, 0, 0]]
n = 3
result = solution.columnWithMaxZeros(matrix, n)
print(result)  # It will print the index of the column with the maximum number of zeros
