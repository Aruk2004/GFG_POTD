# Move all zeroes to end of array

class Solution:
    def pushZerosToEnd(self, arr, n):
        i = 0
        for j in range(n):
            if arr[j] != 0:
                arr[i] = arr[j]
                i += 1

        for i in range(i, n):
            arr[i] = 0

# Example usage:
solution = Solution()
arr = [0, 1, 0, 3, 12]
n = len(arr)
solution.pushZerosToEnd(arr, n)
print(arr)
