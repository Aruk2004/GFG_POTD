# Find duplicate rows in a binary matrix

class Solution:
    def repeatedRows(self, arr, m, n):
        seen_rows = set()
        duplicate_rows = []

        for i in range(m):
            row_tuple = tuple(arr[i])

            if row_tuple in seen_rows:
                duplicate_rows.append(i)
            else:
                seen_rows.add(row_tuple)

        return duplicate_rows

# Example usage:
if __name__ == "__main__":
    sol = Solution()

    matrix1 = [[1, 0], [1, 0]]
    print(sol.repeatedRows(matrix1, 2, 2))  # Output: [1]

    matrix2 = [[1, 0, 0], [1, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(sol.repeatedRows(matrix2, 4, 3))  # Output: [1, 3]
