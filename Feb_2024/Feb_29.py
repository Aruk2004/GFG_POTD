# Sum of bit differences

class Solution:
    def sumBitDifferences(self, arr, n):
        out = 0
        for i in range(32):
            one = sum(1 for num in arr if num & (1 << i))
            zero = n - one
            out += 2 * one * zero
        return out

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 3, 5]
    n = len(arr)
    result = sol.sumBitDifferences(arr, n)
    print(result)  # Output: 8
