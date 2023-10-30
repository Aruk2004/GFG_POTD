# Sum of XOR of all pairs

class Solution:
    def sumXOR(self, arr, n):
        out = 0
        for i in range(32):
            ones = 0
            mask = 1 << i
            for j in range(n):
                if (arr[j] & mask) != 0:
                    ones += 1
            out += ones * (n - ones) * mask
        return out

# Example usage:
solution = Solution()
arr = [4, 8, 6]
n = len(arr)
result = solution.sumXOR(arr, n)
print(result)
