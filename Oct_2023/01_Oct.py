# Boundary traversal of Matrix

class Solution:
    def boundaryTraversal(self, matrix, n, m):
        out = []
        i = 0
        j = 0

        for _ in range(m):
            out.append(matrix[i][j])
            j += 1

        i += 1
        j -= 1

        if n > 1:
            for _ in range(n - 1):
                out.append(matrix[i][j])
                i += 1

            i -= 1
            j -= 1

            if m > 1:
                for _ in range(m - 1):
                    out.append(matrix[i][j])
                    j -= 1

                i -= 1
                j += 1

                for _ in range(n - 2):
                    out.append(matrix[i][j])
                    i -= 1

        return out

# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

n = 3
m = 4

sol = Solution()
result = sol.boundaryTraversal(matrix, n, m)
print(result)  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5]
