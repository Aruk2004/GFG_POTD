# Minimum Cost To Make Two Strings Identical

class Solution:
    def findMinCost(self, x, y, costX, costY):
        m, n = len(x), len(y)
        prv = [0 for _ in range(m + 1)]
        cur = [0 for _ in range(m + 1)]
        for b in range(1, n + 1):
            for a in range(1, m + 1):
                if x[a - 1] == y[b - 1]:
                    cur[a] = prv[a - 1] + 1
                cur[a] = max(cur[a], prv[a], cur[a - 1])
            prv = cur[:]
        mx = cur[-1]
        return (m - mx) * costX + (n - mx) * costY
