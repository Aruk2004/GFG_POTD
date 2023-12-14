# Painting the Fence

class Solution:
    def countWays(self, n, k):
        mod = 10**9 + 7
        same = 0
        diff = k
        total = same + diff

        for i in range(2, n + 1):
            same = diff * 1
            diff = (total * (k - 1)) % mod
            total = same + diff

        return total % mod

# Example usage:
solution = Solution()
result = solution.countWays(5, 3)  # Replace 5 and 3 with the desired values of n and k
print(result)
