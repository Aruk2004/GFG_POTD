# Swap the array elements

class Solution:
    def swapElements(self, arr, n):
        for i in range(n - 2):
            arr[i], arr[i + 2] = arr[i + 2], arr[i]

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    sol.swapElements(arr, len(arr))
    print(arr)  # Output: [3, 2, 5, 4, 1]
