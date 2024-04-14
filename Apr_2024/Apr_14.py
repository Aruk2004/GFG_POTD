# Xoring and Clearing

class Solution:
    def printArr(self, n, arr):
        # printing array elements with spaces
        for i in arr:
            print(i, end=" ")
        print()
    def setToZero(self, n, arr):
        # setting all elements to zero
        arr[:] = [0] * len(arr)

    def xor1ToN(self, n, arr):
        l = []
        # doing xor with indices
        for i in range(len(arr)):
            res = arr[i] ^ i
            l.append(res)
        arr[:] = l

sol = Solution()

# Example usage of printArr
arr1 = [1, 2, 3, 4, 5]
sol.printArr(len(arr1), arr1)  # Output: 1 2 3 4 5

# Example usage of setToZero
arr2 = [10, 20, 30, 40, 50]
sol.setToZero(len(arr2), arr2)
print(arr2)  # Output: [0, 0, 0, 0, 0]

# Example usage of xor1ToN
arr3 = [5, 10, 15, 20, 25]
sol.xor1ToN(len(arr3), arr3)
print(arr3)  # Output: [4, 11, 12, 23, 28]
