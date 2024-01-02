# Largest Sum Subarray of Size at least K

class Solution:
    def maxSumWithK(self, a, n, k):
        pre = [0] * n
        pre[0] = a[0]

        for i in range(1, n):
            pre[i] = pre[i - 1] + a[i]

        _sum = pre[k - 1]
        ans = _sum

        for i in range(k, n):
            cur = pre[i] - pre[i - k]
            _sum = max(cur, _sum + a[i])
            ans = max(ans, _sum)

        return ans

# Example usage:
a = [1, 2, 3, -2, 5]
n = len(a)
k = 3
sol = Solution()
result = sol.maxSumWithK(a, n, k)
print(result)
