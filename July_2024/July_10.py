# Largest square formed in a matrix

from typing import List

class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        memo = {}
        def dp(i,j):
            if i >= n or j >= m:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if mat[i][j] == 1:
                ans = min(dp(i+1,j), dp(i,j+1), dp(i+1,j+1)) + 1
                memo[(i,j)] = ans
                return ans
            memo[(i,j)] = 0
            return 0

        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dp(i,j))

        return ans
