# Matrix sum

class Solution:
    def matrixSum(self, n, m, mat, q, queries):
        out = []

        for k in range(q):
            sum_val = 0
            hop = queries[k][0]
            x = queries[k][1]
            y = queries[k][2]

            for i in range(x - hop, x + hop + 1):
                if i >= 0 and i < n:
                    if y - hop >= 0:
                        sum_val += mat[i][y - hop]
                    if y + hop < m:
                        sum_val += mat[i][y + hop]

            for i in range(y - hop + 1, y + hop):
                if i >= 0 and i < m:
                    if x - hop >= 0:
                        sum_val += mat[x - hop][i]
                    if x + hop < n:
                        sum_val += mat[x + hop][i]

            out.append(sum_val)

        return out

# Example usage:
solution = Solution()
n = 4
m = 4
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
q = 3
queries = [(1, 1, 1), (2, 2, 1), (0, 0, 2)]
result = solution.matrixSum(n, m, mat, q, queries)
print(result)  # It will print the sums for the provided queries
