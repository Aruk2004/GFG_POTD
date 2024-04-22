# Row with minimum number of 1's

class Solution:
    def minRow(self,n,m,a):
        ans = {}
        for i in range(n):
            ans[i+1] = a[i].count(1)
        return sorted(ans.items(), key = lambda t:t[1])[0][0]

sol = Solution()
n = 3
m = 4
a = [
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 0, 1, 0]
]
print(sol.minRow(n, m, a))  # Output: 3 (The third row has the minimum number of 1s)
