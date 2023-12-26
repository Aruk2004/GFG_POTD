# Largest rectangular sub-matrix whose sum is 0

class Solution:
    def sumZeroMatrix(self, a):
        n = len(a)
        m = len(a[0])
        pre = [row.copy() for row in a]

        for i in range(1, n):
            for j in range(m):
                pre[i][j] += pre[i - 1][j]

        for i in range(n):
            for j in range(1, m):
                pre[i][j] += pre[i][j - 1]

        nax = {'x1': -1, 'y1': -1, 'x2': -1, 'y2': -1}
        area = 0

        for i in range(n):
            for j in range(m):
                _sum = 0
                if i > 0 and j > 0:
                    _sum += pre[i - 1][j - 1]

                y = m - 1
                while y >= j:
                    x = n - 1
                    while x >= i:
                        if area <= (x - i + 1) * (y - j + 1):
                            s = _sum + pre[x][y]
                            if i > 0:
                                s -= pre[i - 1][y]
                            if j > 0:
                                s -= pre[x][j - 1]

                            if s == 0:
                                if area != (x - i + 1) * (y - j + 1):
                                    area = (x - i + 1) * (y - j + 1)
                                    nax = {'x1': i, 'y1': j, 'x2': x, 'y2': y}
                                else:
                                    if nax['y1'] > j:
                                        area = (x - i + 1) * (y - j + 1)
                                        nax = {'x1': i, 'y1': j, 'x2': x, 'y2': y}
                                    elif nax['y1'] == j:
                                        if nax['x2'] - nax['x1'] < x - i:
                                            area = (x - i + 1) * (y - j + 1)
                                            nax = {'x1': i, 'y1': j, 'x2': x, 'y2': y}
                        else:
                            break
                        x -= 1
                    y -= 1

        out = []
        if area == 0:
            return out

        for i in range(nax['x1'], nax['x2'] + 1):
            arr = []
            for j in range(nax['y1'], nax['y2'] + 1):
                arr.append(a[i][j])
            out.append(arr)
        return out

# Example usage:
solution_instance = Solution()
matrix = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0]]
result = solution_instance.sumZeroMatrix(matrix)
print(result)
