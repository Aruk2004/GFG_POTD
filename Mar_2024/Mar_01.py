# Peak element

class Solution:
    def peakElement(self, arr, n):
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 3, 20, 4, 1, 0]
    n = len(arr)
    result = sol.peakElement(arr, n)
    print(result)  # Output: 2
