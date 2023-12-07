# Number of subarrays with maximum values in given range

class Solution:
    def countSubarrays(self, a, n, L, R):
        out = 0
        range_size = 0
        i = 0

        for j in range(n):
            if L <= a[j] <= R:
                range_size = j - i + 1
            elif a[j] > R:
                range_size = 0
                i = j + 1

            out += range_size

        return out

# Example usage:
solution = Solution()
a = [2, 1, 4, 3]
n = len(a)
L = 2
R = 3
result = solution.countSubarrays(a, n, L, R)
print(result)  # Output: 6
