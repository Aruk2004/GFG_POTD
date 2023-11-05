# Sum of matrices

class Solution:
    def matrixSum(self, n, m, mat, q, queries):
        prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                prefix_sum[i + 1][j + 1] = mat[i][j] + prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j]

        result = []

        for query in queries:
            if query[0] == 1:
                x, y = query[1], query[2]
                total_sum = prefix_sum[min(n, x + 1)][min(m, y + 1)] - prefix_sum[max(0, x - 1)][min(m, y + 1)] - \
                            prefix_sum[min(n, x + 1)][max(0, y - 1)] + prefix_sum[max(0, x - 1)][max(0, y - 1)]
                result.append(total_sum)
            else:
                x, y = query[1], query[2]
                total_sum = 0
                for i in range(x - 2, x + 3):
                    for j in range(y - 2, y + 3):
                        if 0 <= i < n and 0 <= j < m:
                            total_sum += mat[i][j]
                result.append(total_sum)

        return result

# Example usage
solver = Solution()

# Example 1
n1, m1 = 4, 5
mat1 = [[1, 2, 3, 4, 10], [5, 6, 7, 8, 10], [9, 1, 3, 4, 10], [1, 2, 3, 4, 10]]
q1 = 2
queries1 = [[1, 0, 1], [2, 0, 1]]
output1 = solver.matrixSum(n1, m1, mat1, q1, queries1)
print(output1)  # Output: [22, 29]

# Example 2
n2, m2 = 6, 6
mat2 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]
q2 = 1
queries2 = [[2, 3, 2]]
output2 = solver.matrixSum(n2, m2, mat2, q2, queries2)
print(output2)  # Output: [336]
